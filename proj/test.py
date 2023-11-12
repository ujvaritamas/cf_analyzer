from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "https://games.crossfit.com/leaderboard/open/2022?view=0&division=2&region=0&scaled=0&sort=0"
page = urlopen(url)
html_bytes = page.read()
html = html_bytes.decode("utf-8")


#print(page)

soup = BeautifulSoup(html, "html.parser")

#import pdb; pdb.set_trace()
#table = soup.find(lambda tag: tag.name=='table' and tag.has_attr('id') and tag['id']=="Table1") 
#rows = table.findAll(lambda tag: tag.name=='tr'


import pdb; pdb.set_trace()
for a in soup.find_all("div", {"id": "leaderboardSponsorVisible"}):
    for b in a.find_all("div", {"class": "inner desktop"}):
        print(b)

for a in soup.find_all('tbody'):
    
    print(a)
    #print(data)
print("haha")