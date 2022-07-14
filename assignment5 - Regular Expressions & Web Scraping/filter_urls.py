import re
from requesting_urls import*

def find_urls(html_string,base_url=None,output=None):
    """This function take a html string. And 2 optional argument.
        All found urls in a txt file, if output given, then save under the given name.

        Args: html_string(String), base_url(String), output(String)
        Returns: list(List)
    """
    #the regex is, start from a tag <a , .* select everything to href=.
    #Then match a " and everything between to we come to another " or #.
    comp = re.compile(r"<a.*href=[\"](.*?)(?:[\"]|[#])")
    list = []

    #find all url in html_string
    for url in comp.findall(html_string):
        if url != "":
            if url[1] == '/':
                url = "https:"+url
            elif url[0] == '/' and base_url != None:
                url = base_url+url

            list.append(url)

    #save urls in a txt
    if output != None:
        txt = open(output,"w",encoding="utf-8")

        for url in list:
            txt.write(url + '\n')
        txt.close()

    return list;

def find_articles(html_string,output=None):
    """This function take in a url html_string.
        Then find all wikipedia url that is inside tag <a> and under the attribute href.

        Args: html_string(String),output(String)
        Returns: wiki_side(List)
    """

    urls = find_urls(html_string)

    #The comp , for full wikipedia adress
    #The comp2, for relative wikipedia adress
    comp = re.compile(r".*wikipedia.org.*")
    comp2 = re.compile(r".*([\/]wiki.*)")

    """from bs4 import BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')
    h = []
    for link in soup.find_all('a'):
        h.append(link.get('href'))
    print(len(urls))
    print(len(h))"""

    #Find the wikipedia url in urls
    wiki_side = []
    base_url = "https://wikipedia.org"
    for url in urls:
        if len(comp.findall(url)) != 0:
            wiki_side.append(comp.findall(url)[0])
        elif len(comp2.findall(url)) != 0:
            wiki_side.append(base_url+comp2.findall(url)[0])

    #save urls in a txt
    if output != None:
        txt = open(output,"w",encoding="utf-8")

        for url in wiki_side:
            txt.write(url + '\n')
        txt.close()
    return wiki_side


def test_find_articles():
    pass
    #find_articles(get_html("https://en.wikipedia.org/wiki/Nobel_Prize"),"1.txt")
    #find_articles(get_html("https://en.wikipedia.org/wiki/Bundesliga"),"2.txt")
    #find_articles(get_html("https://en.wikipedia.org/wiki/2019%E2%80%9320_FIS_Alpine_Ski_World_Cup"),"3.txt")
    #find_articles(get_html("https://en.wikipedia.org/wiki/Studio_Ghibli"),"4.txt")
    #find_articles(get_html("https://en.wikipedia.org/wiki/Star_Wars"),"5.txt")
    #find_articles(get_html("https://en.wikipedia.org/w/index.php"),"6.txt")


if __name__=='__main__':
    test_find_articles()
