# import httplib2
# from BeautifulSoup import BeautifulSoup, SoupStrainer
#
# http = httplib2.Http()
# status, response = http.request('https://www.whitehouse.gov/briefing-room/speeches-and-remarks?term_node_tid_depth=31&page=5')
#
# for link in BeautifulSoup(response, parseOnlyThese=SoupStrainer('a')):
#     if link.has_attr('href'):
#         print(link['href'])


from bs4 import BeautifulSoup
import urllib.request
import re

resp = urllib.request.urlopen("https://www.whitehouse.gov/briefing-room/speeches-and-remarks?term_node_tid_depth=31&page=52")
soup = BeautifulSoup(resp, from_encoding=resp.info().get_param('charset'))

for link in soup.find_all('a', href=True):
    print(link['href'])


# get all the links /the-press-office/
