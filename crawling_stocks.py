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

# 찾고 싶은 주식 개수 입력
num = int(input("원하는 주식 개수 ==> "))

# 주식명 모음
names = []

# 원하는 개수만큼 주식명 입력
while num > 0:
    name = input("원하는 주식명 : ")
    if name not in names:
        names.append(name)
        num -= 1
    else:
        print('이미 입력했습니다.')

print(names)
print()

# 찾고 싶은 주식 여러 개 리스트 저장
# keyword_list = ['애플', '삼성전자', '현대모비스']
    
# 크롬 열기
# 리스트 요소마다 열고 닫아야 함.
for kw in names:
    # 주식 URL
    path = f'https://www.google.com/search?q={kw}+주식'
    driver.get(path)

    # 기업 이름 찾기
    # <div class="DoxwDb">    <div class="PZPZlf ssJ7i B5dxMb" aria-level="2" data-attrid="title" role="heading">애플</div>  </div>
    name = driver.find_element(By.CSS_SELECTOR, '.DoxwDb').text

    # 현재가 찾기
    # <span jsname="vWLAgc" class="IsqQVc NprOob wT3VGc">165.84</span>
    price = driver.find_element(By.CSS_SELECTOR, '.IsqQVc').text

    # 최고, 최저가 찾기
    # <div class="PZPZlf" data-attrid="최고">167.26</div>
    high_price = driver.find_element(By.CSS_SELECTOR, 'div[data-attrid="최고"]').text
    low_price = driver.find_element(By.CSS_SELECTOR, 'div[data-attrid="최저"]').text

    # 출력
    print(f'=== {kw} INFO ===')
    print(f'주식명 : {name}')
    print(f'현재가 : {price}')
    print(f'상한가 : {high_price}')
    print(f'하한가 : {low_price}\n')
    
driver.quit()