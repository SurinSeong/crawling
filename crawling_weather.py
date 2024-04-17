# 크롤링 전처리 방식 - 딕셔너리에서 데이터 추출하는 방법 사용

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

# 원하는 웹페이지 이동
# 날씨 정보 페이지
path = "https://www.google.com/search?q=weather"
driver.get(path)

# CSS 선택자 사용, 원하는 클래스를 가진 웹 요소에 접근

# 개발자 도구 열어서 커서로 원하는 데이터 선택 후, 해당 코드 복사 (selector)
# 찾고 싶은 것의 ID : #wob_tm
element = driver.find_element(By.ID, "wob_tm").text
# print(element)

# 날씨 정보의 위치 찾기
# #oFNiHe > omnient-visibility-control > div > div > div.eKPi4.BUSxSd > span:nth-child(2) > span.BBwThe
location = driver.find_element(By.CSS_SELECTOR, "span.BBwThe").text
print("="*10)
print(f"{location}'s temperature is {element}'C.")

# 브라우저 닫기
driver.quit()