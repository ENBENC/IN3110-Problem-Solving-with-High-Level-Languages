from bs4 import BeautifulSoup
import requests as req
import re
from requesting_urls import*
from collect_dates import*

def extract_events(url):
    """Read information from a wikipedia table
    Read each row of the table and save information in a list of:
    (event,date,venue,discipline)

    And each row is saved in list events

    Args: url(String)
    Return: events(List)
    """
    disciplines = {
        "DH":"Downhill",
        "SL":"Slalom",
        "GS":"Giant Slalom",
        "SG":"Super Giant Slalom",
        "AC":"Alpine Combined",
        "PG":"Parallel Giant Slalom",
    }
    html = get_html(url)
    soup = BeautifulSoup(html, "html.parser")
    calendar_header = soup.find(id="Calendar")

    #calendar_table is the table that we are going to working on
    calendar_table = calendar_header.find_all_next("table")[0]
    table_header = calendar_table.find_all("th")

    #Build up the index to each column
    #{'#': 0, 'Event': 1, 'Date': 2, 'Venue': 3,
    #'Type': 4, 'Winner': 5, 'Second': 6, 'Third': 7, 'Details': 8}
    table_index = {}
    i = 0
    for head in table_header:
        title = head.get_text(strip=True)
        table_index[title] = i
        i+=1
    #This give a list that have all rows, row in a table have tag <tr>
    rows = calendar_table.find_all("tr")

    found_event = None
    found_venue = None
    found_discipline = None
    found_date = None
    events = []

    #The full length of each row is 9

    #The short length have 8, because of the same venue
    #If the length of a row is 8, that means this event have same venue as the previous row

    #There is also other row that have less then 8, this means the event was cancelled
    #We ignore these row

    full_row_length = len(table_header)
    short_row_length = full_row_length-1
    for row in rows:
        cells = row.find_all("td")
        #Dealing with the short row
        #Since a short row can have venue that span over columns
        if len(cells) not in {full_row_length,short_row_length}:
            #For short row, we still need to find the venue, since it can span over columns
            #Since the short cell can have irregular length
            #But the venue cell is always after a date cell that have format DMY and before discipline cell
            regex_dmy = month_regex("DMY")
            discipline_regex = r"\b[A-Z][A-Z]\b"
            prev_cell_is_date = False

            for cell in cells:
                discipline_macth = re.search(discipline_regex,cell.text.strip())
                #If this cell is discipline, then do nothing
                #There is no venus in this row
                if discipline_macth:
                    break

                #We found the venue cell and update found_venue
                if prev_cell_is_date:
                    found_venue = cell.text.strip()
                    break
                #If we find a cell in DMY format, then the next must be a venue cell or discipline
                date_macth = re.search(regex_dmy,cell.text.strip())
                if date_macth:
                    prev_cell_is_date = True
            continue

        #The event will be on the 2.cell
        event = cells[table_index.get('Event')]
        if re.match(r"\d{1,3}", event.text.strip()):
            found_event = event.text.strip()
        else: found_event = None

        #Find date
        date = cells[table_index.get('Date')]
        regex_dmy = month_regex("DMY")
        date_macth = re.search(regex_dmy,date.text.strip())
        if date_macth:
            found_date = date_macth.group()
        else:
            found_date = None

        #If the cells have full row then the discipline_index is in the 4
        #If the cells is a short row then the discipline_index is 3
        if len(cells) == full_row_length:
            venue_cell = cells[table_index.get('Venue')]
            found_venue = venue_cell.text.strip()
            discipline_index = table_index.get('Type')
        else:
            discipline_index = table_index.get('Type')-1

        discipline = cells[discipline_index]

        #The discipline should be a length of 2 with only upper case from A-Z
        discipline_regex = r"\b[A-Z][A-Z]\b"
        discipline_macth = re.search(discipline_regex,discipline.text.strip())
        if discipline_macth:
            found_discipline = disciplines.get(discipline_macth.group())
        else:
            found_discipline = None

        if found_venue and found_event and found_discipline:
            events.append((found_event,found_date,found_venue,found_discipline))

    return events

def create_betting_slip(events, save_as):
    """Create a betting slip Markdown
        Save a betting slip that have date, vemie, discipline and empty who wins
        The file is saved as input.md under folder datetime_filter

        Args: events(List), save_as(String)
        Return:None
    """
    os.makedirs("datetime_filter", exist_ok=True)

    with open(f"./datetime_filter/{save_as}.md", "w") as out_file :
        out_file.write(f"#BETTING SLIP({save_as})\n\nName:\n\n")
        out_file.write("Date|Venue|Discipline|Who wins?\n")
        out_file.write(" --- | --- | --- | --- \n")
        for e in events:
            event,date,venue,type = e
            out_file.write(f"{date}|{venue}|{type}|\n")

        out_file.close()

if __name__=='__main__':
    url = "https://en.wikipedia.org/wiki/2020%E2%80%9321_FIS_Alpine_Ski_World_Cup"
    events = extract_events(url)
    create_betting_slip(events, "betting_slip_empty")
