from requesting_urls import*
from filter_urls import*
from collect_dates import*

def test_find_urls():
    html = """
    <a href="#fragment-only" > anchor link </a>
    <a id="some-id" href="/relative/path#fragment">relative link </
    a>
    <a href="//other.host/same-protocol">same-protocol link</a>
    <a href="https://example.com">absolute URL</a>
    """
    urls = find_urls(html, base_url = "https://en.wikipedia.org")

    assert urls == [
    "https://en.wikipedia.org/relative/path",
    "https://other.host/same-protocol",
    "https://example.com",
    ]

def test_get_date():
    text = """
    DMY : 13 October 2020
    MDY : October 13, 2020
    YMD : 2020 October 13
    ISO : 2020-10-13
        """
    assert get_date_DMY(text)[0] == "13 October 2020"
    assert get_date_MDY(text)[0] == "October 13, 2020"
    assert get_date_YMD(text)[0] == "2020 October 13"
    assert get_date_ISO(text)[0] == "2020-10-13"
    assert find_dates(text) == ['2020/10/13','2020/10/13','2020/10/13','2020/10/13']
