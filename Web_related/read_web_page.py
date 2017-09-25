from bs4 import BeautifulSoup
import re
import urllib.request as ur
page=ur.urlopen("http://www.fb.com")
soup=BeautifulSoup(page,"lxml")
print(soup)
# for a in page:
#     deco=str(a,encoding='UTF_8')
#     if(re.match('^http',deco)):
#         print(re.match('http',deco).group())
# a=[]
# b={}
# for link in soup.findAll('a', attrs={'href': re.compile("^http")}):
#     a.append(link.get("href"))
# for x in a[:2]:
#     page = ur.urlopen(x)
#     soup = BeautifulSoup(page, "lxml")
#     print(soup)
#     for link in soup.findAll('a', attrs={'href': re.compile("^http")}):
#         a.append(link.get("href"))
#     b[x] = a

# print(b)