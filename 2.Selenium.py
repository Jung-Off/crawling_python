#간혹가다 소스가 안보이는데 웹페이지가 보이는 경우
#자바스크립트로 되어있는 프레임워크 들을 이용해서 동적으로 생성된 html 파일
#angular js react js 동적 page.. >> Selenium

#pip3 install selenium

from selenium import webdriver
# 패키지를 로드 할 수 있음 
# driver 드라이빙 조정하고 운전.. >> web broswer을 조정하다
#selenium은 webbroswer 을 띄워서 작업
#웹크롤링 용 x >> ui test용

driver = webdriver.Chrome("/Users/jji/Desktop/crawling_python/chromedriver")

driver.implicitly_wait(3)

driver.get("https://nid.naver.com/nidlogin.login")

driver.find_element_by_name('id').send_keys('lewis941001')
driver.find_element_by_name('pw').send_keys('hoonji12#')
driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()


#이런식으로 로그인을 자동화 할 수 있다
#여기에서 내용을 가져오고 다듬는 것은 beautiful soap

import bs4

driver.get("https://order.pay.naver.com/home")

html = driver.page_source
soup = bs4.BeautifulSoup(html, 'html.parser')

notices = soup.find_all("a", {"class":"goods"})

for n in notices:
    print(n.test.strip())

#UI web broswer 가 떠야만 됨  제약이 있음
#cloud 환경 >> windows UI 가상머신 필요 
#webbroswer setting 필요
#그 안의 내용은 제약이 없이 가져올 수 있고
#로그인 까지 쉽게 처리를 할 수 있다
#성능이 떨어짐,, 사용하는 환경상의 제약이 있다
