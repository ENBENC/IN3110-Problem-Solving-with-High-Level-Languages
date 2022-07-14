import re
from requesting_urls import*
def get_date_DMY(html_string):
    """This function get time from html side with format DMY.
        DMY : 13 October 2020

        Args: html_string(String)
        Return: date(List)
    """
    comp = re.compile(month_regex("DMY"))
    date = comp.findall(html_string)
    return date

def get_date_MDY(html_string):
    """This function get time from html side with format MDY.
        MDY : October 13, 2020

        Args: html_string(String)
        Return: date(List)
    """
    comp = re.compile(month_regex("MDY"))
    date = comp.findall(html_string)
    return date

def get_date_YMD(html_string):
    """This function get time from html side with format MDY.
        YMD : 2020 October 13

        Args: html_string(String)
        Return: date(List)
    """
    comp = re.compile(month_regex("YMD"))
    date = comp.findall(html_string)
    return date

def get_date_ISO(html_string):
    """This function get time from html side with format ISO.
        ISO : 2020-10-13

        Args: html_string(String)
        Return: date(List)
    """
    comp = re.compile(month_regex("ISO"))
    date = comp.findall(html_string)
    return date

def month_regex(format, sub = None, month=None):
    """Get the regex format based on the argument "format"
        Format take a string that should be DMY, MDY, YMD or ISO, and return a regex based on that.
        The sub argument is optional, and it will return a grouping version of the regex.
        The month argument is optional, and return only the months regex

        Args: format(String), sub(boolean), month(boolean)
        Return: a regex string
    """
    if format!="DMY" and format!="MDY" and format!="YMD" and format!="ISO":
        raise Exception("Wrong input: Format")

    #Regex expression of months
    jan = r"\b[jJ]an(?:uary)?\b"
    feb = r"\b[Ff]eb(?:ruary)?\b"
    mar = r"\b[mM]ar(?:ch)?\b"
    apr = r"\b[aA]pr(?:il)?\b"
    may = r"\b[Mm]ay?\b"
    jun = r"\b[jJ]un(?:e)?\b"
    jul = r"\b[jJ]ul(?:y)?\b"
    aug = r"\b[aA]ug(?:ust)?\b"
    sep = r"\b[Ss](?:ep|ept)(?:tember|ember)?\b"
    oct = r"\b[oO]ct(?:ober)?\b"
    nov = r"\b[Nn]ov(?:ember)?\b"
    dec = r"\b[Dd]ec(?:ember)?\b"

    #This means 01 or 02 or 03 or ...
    #This allow also 1 or 2 or 3 or ...
    iso_month = r"\b(?:[1-9]|0[1-9]|1[0-2])\b"

    day = r"\b(?:[1-9]|0[1-9]|[1-2][0-9]|30|31)\b"
    #assum that year is a 4 digit number
    year = r"\b(?:\d{4})\b"

    #This means jun or feb or mar or ...
    months = rf"(?:{jan}|{feb}|{mar}|{apr}|{may}|{jun}|{jul}|{aug}|{sep}|{oct}|{nov}|{dec})"

    if month:
        return months

    #Return the format, based on input
    if format == "DMY":
        if sub:
            return rf"({day})\s({months})\s({year})"

        return rf"{day}\s{months}\s{year}"
    elif format == "MDY":
        if sub:
            return rf"({months})\s({day}),\s({year})"

        return rf"{months}\s{day},\s{year}"
    elif format == "YMD":
        if sub:
            return rf"({year})\s({months})\s({day})"

        return rf"{year}\s{months}\s{day}"
    else:
        if sub:
            return rf"({year})-({iso_month})-({day})"

        return rf"{year}-{iso_month}-{day}"



def find_dates(html_string,output=None):
    """Finds all dates in a html string
        And return a list with date of the format:
        - Year/month/day

        This function will find date that have format: DMY, MDY,YMD,ISO:
        DMY : 13 October 2020
        MDY : October 13, 2020
        YMD : 2020 October 13
        ISO : 2020-10-13

        Args: html_string(String), output(String)
        Returns: result(list)
    """

    #Get date from 4 formats, and save them in 4 lists
    dmy_dates = get_date_DMY(html_string)
    mdy_dates = get_date_MDY(html_string)
    ymd_dates = get_date_YMD(html_string)
    iso_dates = get_date_ISO(html_string)

    results = []

    map_Months = {"jan":"01","feb":"02","mar":"03","apr":"04","may":"05",
    "jun":"06","jul":"07","aug":"08","sep":"09","oct":"10","nov":"11","dec":"12"}

    #Change elements in all 4 lists to the format to return
    for date in dmy_dates:
        #get month regex
        month = re.findall(month_regex("DMY",month=True),date)

        if len(month) != 0:
            #get the month from date
            month = re.findall(month_regex("DMY",month=True),date)[0]
            #Here lower the first 3 char in month string, and get the digital version of it
            dig_month = map_Months.get(month[0:3].lower())

        date_element = re.sub(month_regex("DMY",sub=True),r"\3/\2/\1",date)
        date_element = re.sub(month_regex("DMY",month=True),dig_month,date_element)
        results.append(date_element)

    for date in mdy_dates:
        month = re.findall(month_regex("MDY",month=True),date)

        if len(month) != 0:
            month = re.findall(month_regex("MDY",month=True),date)[0]
            dig_month = map_Months.get(month[0:3].lower())

        date_element = re.sub(month_regex("MDY",sub=True),r"\3/\1/\2",date)
        date_element = re.sub(month_regex("MDY",month=True),dig_month,date_element)
        results.append(date_element)

    for date in ymd_dates:
        month = re.findall(month_regex("YMD",month=True),date)

        if len(month) != 0:
            month = re.findall(month_regex("YMD",month=True),date)[0]
            dig_month = map_Months.get(month[0:3].lower())

        date_element = re.sub(month_regex("YMD",sub=True),r"\1/\2/\3",date)
        date_element = re.sub(month_regex("YMD",month=True),dig_month,date_element)
        results.append(date_element)

    #This is ok, just change the - to /
    for date in iso_dates:
        date_element = re.sub(month_regex("ISO",sub=True),r"\1/\2/\3",date)
        results.append(date_element)

    #Sort the date and save the file if the output was given
    results.sort()

    if output != None:
        txt = open(output,"w",encoding="utf-8")

        for date in results:
            txt.write(date + '\n')
        txt.close()

    return results

if __name__=='__main__':
    find_dates(get_html("https://en.wikipedia.org/wiki/J._K._Rowling"),"date_J._K._Rowling.txt")
    find_dates(get_html("https://en.wikipedia.org/wiki/Richard_Feynman"),"date_Richard_Feynman.txt")
    find_dates(get_html("https://en.wikipedia.org/wiki/Hans_Rosling"), "date_Hans_Rosling.txt")
