#### A simple program that collect url from a wikipedia site, find date of html string. 
#### At the end fetch NBA player statistics in wikipedia and write result in a bar chart.

## Install python library:
  pip install requests
  pip install beautifulsoup4
  pip install regex
  pip install matplotlib

test.py includ simple test of function find_urls and test of regex to dmy,mdy,ymd,iso format.

## 5.1: requesting_urls.py
corresponding output in "requesting urls".

## 5.2: filter_urls.py(script)
corresponding output in "filter_urls". Run pytest test.py for tesing function find_urls in filter_urls.py.

## 5.3: collect_date.py(script)
corresponding output in "collect_date_regex". To test that the regex expression of each format is correct, run pytest test.py

## 5.4: time_planner.py(script)
corresponding output in "datetime_filter"

## 5.5: fetch_player_statistics.py(script)
corresonding output in NBA_player_statistics.
This script migth take some time to plot the figure. The matplotlib must be ver 3.4 or after, so make sure you have the correct ver. of matplotlib.
