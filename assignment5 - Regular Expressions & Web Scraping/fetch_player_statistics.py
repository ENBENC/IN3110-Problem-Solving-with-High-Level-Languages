from bs4 import BeautifulSoup
from requesting_urls import get_html
import re
from filter_urls import*

def extract_teams():
    """Extract team names and urls from the NBA Playoff 'Bracket' section table.
    Returns:
        team_names (list): A list of team names that made it to the conference
            semifinals.
        team_urls (list): A list of absolute Wikipedia urls corresponding to team_names.
    """

    # get html using for example get_html from requesting_urls
    html = get_html("https://en.wikipedia.org/wiki/2021_NBA_playoffs")

    # create soup
    soup = BeautifulSoup(html, "html.parser")
    # find bracket we are interested in
    bracket_header = soup.find(id="Bracket")
    bracket_table = bracket_header.find_next("table")
    rows = bracket_table.find_all("tr")

    # create list of teams
    team_list = []
    url_list = []
    url_dir = {}
    for i in range(1, len(rows)):
        cells = rows[i].find_all("td")
        cells_text = [cell.get_text(strip=True) for cell in cells]

        # Filter out the cells that are empty
        cells_text = [cell for cell in cells_text if cell]
        #Cell that contain information will have a format
        #Length 3, (seeding,team_name,game_won)

        # Find the rows that contain seeding, team name and games won
        #Regex for delete "*" at end of some name
        name_regex = r"\b([A-Za-z]+\s[A-Za-z]+|[A-Za-z]+)\b"
        if len(cells_text) >= 3:
            name = re.findall(name_regex,cells_text[1])
            team_list.append([cells_text[0],name[0],cells_text[2]])

            #Here we find the url to each team
            for cell in cells:
                team_wiki_side = find_articles(str(cell))
                if len(team_wiki_side) != 0:
                    url_dir[name[0]] = team_wiki_side[0]

    # Filter out the teams that appear more than once, which means they made it
    # to the conference semifinals
    team_list_filtered = []
    for cell in team_list:
        i = 0
        for cheak_cell in team_list:
            if cell[1] == cheak_cell[1]:
                i += 1

        if i > 1 and cell[1] not in team_list_filtered:
            team_list_filtered.append(cell[1])
    #Get the url to the teams
    for key in team_list_filtered:
        url_list.append(url_dir[key])

    # create lists of team names and urls to the team website
    team_names = team_list_filtered
    team_urls = url_list

    return team_names, team_urls

def extract_players(team_url):
    """Extract players that played for a specific team in the NBA playoffs.
    Args:
        team_url (str): URL to the Wikipedia article of the season of a given
            team.
    Returns:
        player_names (list): A list of players names corresponding to the team whos URL was passed.
            semifinals.
        player_urls (list): A list of Wikipedia URLs corresponding to
            player_names of the team whos URL was passed.
    """

    # keep base url
    base_url = "https://en.wikipedia.org"

    # get html for each page using the team url you extracted before
    html = get_html(team_url)

    # make soup
    soup = BeautifulSoup(html, "html.parser")
    # get the header of the Roster
    roster_header = soup.find(id="Roster")
    # identify table
    roster_table = roster_header.find_next("table")
    rows = roster_table.find_all("tr")

    # prepare lists for player names and urls
    player_names = []
    player_urls = []

    for i in range(0, len(rows)):
        cells = rows[i].find_all("td")
        cells_text = [cell.get_text(strip=True) for cell in cells]
        if len(cells_text) == 7:
            rel_url = cells[2].find_next("a").attrs["href"]
            # Use e.g. regex to remove information in parenthesis following the name
            #The regex for names, a name can contain special symbol . and _ else no
            regex = r".*[\/]([A-Za-z._]+)"
            name = re.findall(regex,rel_url)[0]
            name = re.sub("_", " ",name)

            # create urls to each player
            # need to create absolute urls combining the base and the relative url
            player_names.append(name)
            player_urls.append(base_url + rel_url)
    return player_names, player_urls

def extract_player_statistics(player_url):
    """Extract player statistics for NBA player.
    # Note: Make yourself familiar with the 2020-2021 player statistics wikipedia page and adapt the code accordingly.
    Args:
        player_url (str): URL to the Wikipedia article of a player.
    Returns:
        ppg (float): Points per Game.
        bpg (float): Blocks per Game.
        rpg (float): Rebounds per Game.
    """
    # As some players have incomplete statistics/information, you can set a default score, if you want.

    ppg = 0.0
    bpg = 0.0
    rpg = 0.0

    # get html
    html = get_html(player_url)

    # make soup
    soup = BeautifulSoup(html, "html.parser")

    # find header of NBA career statistics
    nba_header = soup.find(id="NBA_career_statistics")

    # check for alternative name of header
    if nba_header is None:
        nba_header = soup.find(id="NBA")

    try:
        # find regular season header
        # You might want to check for different spellings, e.g. capitalization
        # You also want to take into account the different orders of header and table
        regular_season_header = nba_header.find_next(id="Regular_season")

        # next we should identify the table
        nba_table = regular_season_header.find_next("table")


    except:
        try:
            # table might be right after NBA career statistics header
            nba_table = nba_header.find_next("table")

        except:
            return ppg, bpg, rpg

    # find nba table header and extract rows
    table_header = nba_table.find_all("th")
    #Build a dictionary
    #{'Year': 0, 'Team': 1, 'GP': 2, 'GS': 3,
    #'MPG': 4, 'FG%': 5, '3P%': 6, 'FT%': 7, 'RPG': 8, 'APG': 9, 'SPG': 10, 'BPG': 11, 'PPG': 12}
    table_index = {}
    i = 0
    for head in table_header:
        title = head.get_text(strip=True)
        table_index[title] = i
        i+=1

    #Find the correct row for nba 2020-21
    rows = nba_table.find_all("tr")
    row_2020_2021 = None
    regex = r"2020–21"
    for row in rows:
        title = row.get_text(strip=True)
        match = re.search(regex,title)
        if match:
            row_2020_2021 = row

    # find the columns for the different categories
    #If the row_2020_2021 is None, then this player dont have row corresponding to 2020-21
    #Then we just return all 0.0
    if row_2020_2021 != None:
        row_2020_2021 = row_2020_2021.find_all("td")
    else:
        return 0.0,0.0,0.0

    ppg_column = row_2020_2021[table_index.get('PPG')]
    bpg_column = row_2020_2021[table_index.get('BPG')]
    rpg_column = row_2020_2021[table_index.get('RPG')]
    # Extract the scores from the different categories
    ppg = ppg_column.get_text(strip=True)
    bpg = bpg_column.get_text(strip=True)
    rpg = rpg_column.get_text(strip=True)


    # Convert the scores extracted to floats
    # Note: In some cases the scores are not defined but only shown as '-'. In such cases you can just set the score to zero or not defined.
    try:
        ppg = float(ppg)
        bpg = float(bpg)
        rpg = float(rpg)
    except ValueError:
        ppg = 0.0
        bpg = 0.0
        rpg = 0.0

    return ppg, bpg, rpg


import matplotlib.pyplot as plt

teams = {
    "UiO": [
        {
            "name": "Lisa",
            "ppg": 10.0,
        },
        {
            "name": "Vegard",
            "ppg": 9.2,
        },
    ],
    "Simula": [
        {
            "name": "Ingeborg",
            "ppg": 11.2,
        },
        {
            "name": "Min",
            "ppg": 4.5,
        },
    ],
}

# a matplotlib color for each team name (could be a name or a #rrggbb web color string)
color_table = {
    "Team1": 'b',
    "Team2": 'g',
    "Team3": 'r',
    "Team4": 'c',
    "Team5": 'm',
    "Team6": 'y',
    "Team7": 'b',
    "Team8": 'tan',
}

def plot_NBA_player_statistics(teams,type):
    """Plot NBA player statistics. For given type.
        Argument teams is a dictionary, the key is a team name string, key is a list
        that contain a dictionary. The dictionary contain name and type.
        and mapped to the corresponding type.

        Args: teams (dictionary), type (String)
        Return: None
    """
    if type not in ["ppg","bpg","rpg"]:
        raise Exception('Input plot type: ppg, bpg, rpg')
    print("Begin plotting ...")
    #Clear plot
    plt.clf()
    count_so_far = 0
    all_names = []

    # iterate through each team and the
    for team, players in teams.items():
        # pick the color for the team, from the table above
        color = color_table[team]
        # collect the ppg and name of each player on the team
        # you'll want to repeat with other stats as well
        point = []
        names = []
        for player in players:
            names.append(player["name"])
            point.append(player[type])
        # record all the names, for use later in x label
        all_names.extend(names)

        # the position of bars is shifted by the number of players so far
        x = range(count_so_far, count_so_far + len(players))
        count_so_far += len(players)
        # make bars for this team's players point,
        # with the team name as the label
        bars = plt.bar(x, point, color=color, label=team)
        # add the value as text on the bars
        plt.bar_label(bars)

    # use the names, rotated 90 degrees as the labels for the bars
    plt.xticks(range(len(all_names)), all_names, rotation=90)
    # add the legend with the colors  for each team
    plt.legend(bbox_to_anchor = (1.05, 0.6))
    # turn off gridlines
    plt.grid(False)
    # set the title
    if type == "ppg":
        plt.title("points per game")
    elif type == "bpg":
        plt.title("Blocks per Game")
    else:
        plt.title("Rebounds per Game")
    plt.tight_layout()
    # save the figure to a file
    plt.savefig(type + ".png")
    print("Done!")


if __name__=='__main__':
    import matplotlib
    print("Current matplotlib ver: " + matplotlib.__version__)
    print("You need matplotlib ver: 3.4")
    #Get teams that med to conference semifinals
    #team_names[i] have the corresponding url in team_urls[i]
    team_names,team_urls = extract_teams()
    color_list = ['b','g','r','c','m','y','olive','tan']
    color_table = {}
    team_table_ppg = {}
    team_table_bpg = {}
    team_table_rpg = {}

    for i in range(len(team_names)):
        color_table[team_names[i]] = color_list[i]
        #Get player in the current team
        #player_names[i] have the corresponding url in player_urls[i]
        player_names, player_urls = extract_players(team_urls[i])

        top_3_list_ppg = [{"name":None,"ppg":0.0},{"name":None,"ppg":0.0},{"name":None,"ppg":0.0}]
        top_3_list_bpg = [{"name":None,"bpg":0.0},{"name":None,"bpg":0.0},{"name":None,"bpg":0.0}]
        top_3_list_rpg = [{"name":None,"rpg":0.0},{"name":None,"rpg":0.0},{"name":None,"rpg":0.0}]
        for i_player in range(len(player_names)):
            #Get the ppg, bpg and rpg from current player
            ppg, bpg, rpg = extract_player_statistics(player_urls[i_player])
            player_table_ppg = {"name" : player_names[i_player],
                            "ppg" : ppg,}

            player_table_bpg = {"name" : player_names[i_player],
                            "bpg" : bpg,}

            player_table_rpg = {"name" : player_names[i_player],
                            "rpg" : rpg,}

            #print(player_table_rpg)
            #Find the smallest in the top_3_list_ppg
            tmp_min_ppg = top_3_list_ppg[0]
            tmp_min_bpg = top_3_list_bpg[0]
            tmp_min_rpg = top_3_list_rpg[0]

            for table in top_3_list_ppg:
                if tmp_min_ppg["ppg"] >= table["ppg"]:
                    tmp_min_ppg = table

            for table in top_3_list_bpg:
                if tmp_min_bpg["bpg"] >= table["bpg"]:
                    tmp_min_bpg = table

            for table in top_3_list_rpg:
                if tmp_min_rpg["rpg"] >= table["rpg"]:
                    tmp_min_rpg = table

            if ppg >= tmp_min_ppg["ppg"]:
                top_3_list_ppg.remove(tmp_min_ppg)
                top_3_list_ppg.append(player_table_ppg)

            if bpg >= tmp_min_bpg["bpg"]:
                top_3_list_bpg.remove(tmp_min_bpg)
                top_3_list_bpg.append(player_table_bpg)

            if rpg >= tmp_min_rpg["rpg"]:
                top_3_list_rpg.remove(tmp_min_rpg)
                top_3_list_rpg.append(player_table_rpg)

        team_table_ppg[team_names[i]] = top_3_list_ppg
        team_table_bpg[team_names[i]] = top_3_list_bpg
        team_table_rpg[team_names[i]] = top_3_list_rpg
        #print(top_3_list_rpg)
        #print()
    #print(team_table_ppg)
    plot_NBA_player_statistics(team_table_ppg,"ppg")
    plot_NBA_player_statistics(team_table_bpg,"bpg")
    plot_NBA_player_statistics(team_table_rpg,"rpg")
