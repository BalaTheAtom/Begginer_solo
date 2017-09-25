import urllib.request
from bs4 import BeautifulSoup
import re
import urllib.request as ur
page=ur.urlopen("https://www.facebook.com/balaswamypagolu").read()
soup=BeautifulSoup(page,"lxml")
# print(soup)
a=[]
for link in soup.findAll('img', attrs={'src': re.compile("^http")}):
    a.append(link.get("src"))
print(a)
for i,j in enumerate(a):
    local_name="img"+str(i)+".png"
    urllib.request.urlretrieve(j, local_name)