# 셀레니움 임포트
from selenium import webdriver

# chrome 브라우저 이용할 것
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# 브라우저 옵션 설정
chrome_options = Options()

# detach 옵션을 이용해 자동화
# 브라우저를 자동화한 후, browser window 창 유지
chrome_options.add_experimental_option("detach", True)

# excludeSwitches : 불필요한 로깅 메세지 브라우저에서 제외
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

driver = webdriver.Chrome(options=chrome_options)

## ============Parsing============ ##
# 파싱을 위해 웹페이지 가져오기
# naver >> '푸바오' 검색 >> 뉴스
# 마지막 16진수 = 푸바오 이기 때문에 한글로 푸바오 바꿔서 입력하고 검색해도 됨.

# keyword로 검색하고 싶은 단어 받아서 사용
keyword = input("Input the keyword : ")

# keyword 받은거 path의 16진수 자리에 넣어주기
path = f"https://search.naver.com/search.naver?ssc=tab.news.all&where=news&sm=tab_jum&query={keyword}"

# path 불러오기
driver.get(path)

# 뉴스 타이틀 가져오기 >> #sp_nws1 > div.news_wrap.api_ani_send > div > div.news_contents > a.news_tit
# 뉴스 타이틀의 class가 모두 news_tit라는 것을 알 수 있음.
title_list = driver.find_elements(By.CLASS_NAME, 'news_tit')

# class에서 title만 뽑고 싶기 때문에 for문 사용
for title in title_list:
    title = title.text
    print(title)

# 웹페이지 닫기
driver.quit()

