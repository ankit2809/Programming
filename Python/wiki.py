'''import wikipedia
import bs4
query = input("What do you want to search ? : ")
print(wikipedia.summary(query))

import urllib.request
from bs4 import BeautifulSoup
site= "http://en.wikipedia.org/wiki/Brussels"
hdr = {'User-Agent': 'Mozilla/5.0'}
req = urllib.request.urlopen(site)
soup = BeautifulSoup(req.read())
table = soup.find('table', class_='infobox vcard')
result = {}
exceptional_row_count = 0
for tr in table.find_all('tr'):
    if tr.find('th'):
        result[tr.find('th').text] = tr.find('td').text
    else:
        # the first row Logos fall here
        exceptional_row_count += 1
if exceptional_row_count > 1:
    print ('WARNING ExceptionalRow>1: ', table)
print(result)'''
import urllib.request
from bs4 import BeautifulSoup as bs
query = 'Apple_Inc.'
url = 'https://en.wikipedia.org/wiki/'+query
raw = urllib.request.urlopen(url)
soup = bs(raw)
table = soup.find('table',{'class':'infobox vcard'})
for tr in table.find_all('tr') :
    print(tr.text)
