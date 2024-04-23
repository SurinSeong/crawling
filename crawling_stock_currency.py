# 셀레니움 임포트
from selenium import webdriver

# chrome 브라우저 이용할 것
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# 브라우저 옵션 설정
chrome_options = Options()
# headless : 브라우저 창을 실제로 운영체제의 ‘창’으로 띄우지 않고
# 화면을 그려주는 작업(렌더링)을 가상으로 진행해주는 방법.
# 실제 브라우저와 동일하게 동작하지만 창은 뜨지 않는 방식으로 동작
# headless : GUI(Graphic User InterFace)없이 실행 >> 실제 브라우저창이 눈에 보이지 않게 실행
chrome_options.add_argument('--headless')

# detach 옵션을 이용해 자동화
# 브라우저를 자동화한 후, browser window 창 유지
# headless와 같이 쓸 수 없을 듯
# chrome_options.add_experimental_option("detach", True)

# excludeSwitches : 불필요한 로깅 메세지 브라우저에서 제외
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

# 셀레니움에서 크롬 웹 드라이버를 자동으로 다운로드 및 설치
service = Service(executable_path=ChromeDriverManager().install())

# 웹드라이버 설정
driver = webdriver.Chrome(service=service, options=chrome_options)

# 대기시간 : 10초
wait = WebDriverWait(driver, 10)

########################################################################################################

# 찾고 싶은 주식 개수 입력
num = int(input("원하는 주식 개수 ==> "))

# 주식명 모음
stock_list = []

# 원하는 개수만큼 주식명 입력
while num > 0:
    name = input("원하는 주식명 : ")
    if name not in stock_list:
        stock_list.append(name)
        num -= 1
    else:
        print('이미 입력했습니다.')
        
for stock in stock_list:
    # 주식 URL
    path = f'https://www.google.com/search?q={stock}+주식'
    driver.get(path)
    
    # wait는 find_element 대신 사용하는 것이 있음.
    # EC.presence_of_element_located
    name = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.DoxwDb'))).text
    price = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.IsqQVc'))).text
    high_price = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[data-attrid="최고"]'))).text
    low_price = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[data-attrid="최고"]'))).text
    # 이때 화폐 단위를 맞춰줘야 함. --> 화폐단위도 가져온다.
    # <span jsname="T3Us2d" class="knFDje"> USD</span>
    currency = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.knFDje'))).text
    
    # 화폐 단위도 가격에 함께 나타나도록 보여주는 방법
    if currency == 'KRW':
        unit = '₩'
    elif currency == 'USD':
        unit = '$'
    elif currency == 'JPY':
        unit = '￥'
        
    # 출력
    print(f'==== {name} INFO ====')
    print(f'주식명 : {name}')
    print(f'화폐단위 : {currency}')
    print(f'현재가 : {unit + " " + price}')
    print(f'상한가 : {unit + " " + high_price}')
    print(f'하한가 : {unit + " " + low_price}\n')
    
driver.quit()