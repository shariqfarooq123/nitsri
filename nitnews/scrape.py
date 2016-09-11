import urllib2
from bs4 import BeautifulSoup
import re
import json

#get html
response = urllib2.urlopen('http://www.nitsri.net/indexo.htm')
html = response.read()
#parse html
soup = BeautifulSoup(html)
lies = soup.find_all(class_=re.compile("_news"))
count=0
news_container= []
root_link="www.nitsri.net/"

for li in lies:
    link_type=li.a.get('href').split('.')[-1]
    news_container.append({'doctype':str(link_type),'headline':str((li.find(class_="news_headline").text).encode('ascii','ignore').decode('ascii')),'text':str((li.find(class_="news_text").text).encode('ascii','ignore').decode('ascii')),'link':root_link+str((li.a.get('href').encode('ascii','ignore').decode('ascii'))),'age':str(li.get('class')[0].split('_')[0])})
    #print("headline %d: "%count +(li.find(class_="news_headline").text))
    #print("text: "+(li.find(class_="news_text").text))
    count+=1
    print(news_container)

#Encode to json
j_obj = json.dumps(news_container)

def get_news_json():
    return j_obj
#print(news_container)
#print(count)
#print(len(news_container))
    
