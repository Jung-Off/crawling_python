#pip3 install bs4
import bs4

import urllib.request

url = "http://naver.com"

html = urllib.request.urlopen(url)

bsObj = bs4.BeautifulSoup(html, "html.parser")
#print(bsObj)

realtime_hotnews = bsObj.find("div", {"class":"list_issue"})
#print(realtime_hotnews)

realtime_hotnew = bsObj.find_all("a", {"class" : "issue"})
#print(realtime_hotnews)

for keyword in realtime_hotnew:
    print(keyword.text)