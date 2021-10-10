from selenium import webdriver

driver = webdriver.Chrome("/Users/jji/Desktop/crawling_python/chromedriver")

driver.implicitly_wait(3)

driver.get("https://sports.news.naver.com/wfootball/record/index?category=epl&league=100&tab=player")

import bs4

html = driver.page_source
soup = bs4.BeautifulSoup(html, 'html.parser')

players = soup.find_all("span", {"class":"name"})

for player in players:
    print(player.text)