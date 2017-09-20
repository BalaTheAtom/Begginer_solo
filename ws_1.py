from bs4 import BeautifulSoup
import requests
import pandas as pb
import re
# html= open("C:\\Users\\balaswamy\\Desktop\\Python\\Ex_Files_Python_Data_Science_EssT\\Ex_Files_Python_Data_Science_EssT\\Exercise Files\\Ch10\\10_01\\DSFD_Listing.html",'+r')
# html_doc=html.read()
# soup=BeautifulSoup(html_doc,"lxml")
# tag=BeautifulSoup("<html><head><title>Best Books</title></head>","html.parser")
# # print(tag.name)
# # tag.name="bestBooks"
# k=soup.get_text()
# # print(soup.findAll(id="link 3"))
# # print(soup.findAll('a'))
# # for tag in soup.findAll('a'):
# #     print(tag.get('href'))
# a=re.compile("data")
# print(soup.findAll(string=a))
# r=urllib('https://fb.com').read()
r=requests.get('http://www.gmail.com')
# print(r.text)
data = r.content
# print(data)x`
a=set()
soup = BeautifulSoup(data,"lxml")
# for tag in soup.findAll(True):
#    a.add(str(tag.name))
# print((a))
for link in soup.findAll('a', attrs={'href': re.compile("^http")}): print (link.get("href"))
# for link in soup.find_all('a'):
#         a=link.get("href")
#         print(not a)
#         if(re.match("\w+.com",a)):
#             print(a)
