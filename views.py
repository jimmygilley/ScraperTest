from bs4 import BeautifulSoup
import urllib

#Scrape Code Begin:

#get and parse url in BS4
r = urllib.urlopen('http://www.footballlocks.com/nfl_odds.shtml').read()
soup = BeautifulSoup(r, 'html.parser')

#filter html to find tables I want
tables = soup.find_all("table", cols='6')
table1 = tables[0].find_all("tr")
table2 = tables[1].find_all("tr")

#scrape through content and display scraped lines of html
for row in table1:
  cells = row.find_all("td")
  fav = cells[1].get_text()
  spread = cells[2].get_text().strip()
  under = cells[3].get_text()
  total = cells[4].get_text()
  if fav <> "" and fav <> "Favorite":
    print (fav + ", " + spread + ", " + under + ", " + total + ", ")
#scrape through second table (Monday night game)
for row in table2:
  cells = row.find_all("td")
  fav = cells[1].get_text()
  spread = cells[2].get_text().strip()
  under = cells[3].get_text()
  total = cells[4].get_text()
  if fav <> "" and fav <> "Favorite":
    print (fav + ", " + spread + ", " + under + ", " + total + ", ")

