import requests as req
import os
def get_html(url, params=None, output=None):
    """ Get html string from a given url. The argument params and output is optional.
    If the output is given, then save the url and html string in output.

    Args: url(String), params(dictionary), output(String)
    Return: html(String)
    """
    response = req.get(url, params=params)
    #if the response is correct then status_code should be 200
    try:
        assert response.status_code == 200
    except AssertionError:
        print("Response error: " + url)

    html_str = response.text

    if output != None:
        txt = open(output,"w",encoding="utf-8")
        txt.write("url: " + response.url + '\n')
        txt.write(html_str)
        txt.close()

    return html_str

#get_html("https://en.wikipedia.org/wiki/Studio_Ghibli",None,"Studio_Ghibli.txt")
#get_html("https://en.wikipedia.org/wiki/Star_Wars",None,"Star_Wars.txt")
#get_html("https://en.wikipedia.org/w/index.php",{"title":"Main_Page","action":"info"},"index.txt")
