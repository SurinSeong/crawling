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

# 1. 멀티캠퍼스 키워드로 출처 밝히는 코드 작성
# 2. 멀티캠퍼스 키워드로 contents 가져오는 코드 작성

# 검색 키워드 받기
keyword = input("What is the keyword you want to find?\n")

# path에 경로 저장하기
path = f"https://search.naver.com/search.naver?ssc=tab.news.all&where=news&sm=tab_jum&query={keyword}"

# 해당 경로의 웹페이지 열기
driver.get(path)

# 신문사 가져오기
# info.press
press_list = driver.find_elements(By.CLASS_NAME, "info.press")

# 내용 가져오기
# news_dsc
# api_txt_lines.dsc_txt_wrap
content_list = driver.find_elements(By.CLASS_NAME, "api_txt_lines.dsc_txt_wrap")

# for 반복문 이용해서 출처 출력
for press in press_list:
    press = press.text
    print(press + "\n")

# for 반복문 이용해서 내용 출력
for content in content_list:
    content = content.text
    print(content + "\n")

# 함께 출력
i = 0
for press, content in zip(press_list, content_list):
    i += 1
    press = press.text
    content = content.text
    print(f"{i}번째 뉴스 - {press}\n{content}\n")

# 웹 페이지 닫기
driver.quit()