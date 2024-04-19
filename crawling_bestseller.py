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

# 사이트 URL 가져오기
path = "https://product.kyobobook.co.kr/bestseller/online?period=001&page=1&per=50"
driver.get(path)

# 일간 베스트 도서 목록 찾기
# 한 번에 여러 개의 도서 정보를 가져올 수 있음.
book_elements = driver.find_elements(By.CLASS_NAME, 'prod_item')

# 도서 정보로부터 내가 원하는 세부 정보를 가져올 수 있음.
# enumerate를 이용해 인덱스를 가져올 수 있음.
for index, book in enumerate(book_elements):
    title = book.find_element(By.CLASS_NAME, "prod_info").text
    # author가 출판사, 출판일과 같이 나와서 저자만 빼서 출력함.
    author = book.find_element(By.CLASS_NAME, "prod_author").text.split("·")[0]
    price = book.find_element(By.CLASS_NAME, "price").text
    rank = index + 1
    print(f'RANK {rank} : {title} - {author} ({price})')

driver.quit()
    
