import pandas as pd
import numpy as np
import time

# 셀레니움 임포트
from selenium import webdriver

# chrome 브라우저 이용할 것
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

# 브라우저 옵션 설정
chrome_options = Options()

# detach 옵션을 이용해 자동화
# 브라우저를 자동화한 후, browser window 창 유지
chrome_options.add_experimental_option("detach", True)

# excludeSwitches : 불필요한 로깅 메세지 브라우저에서 제외
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()

# url
url = 'https://music.bugs.co.kr/chart/track/realtime/total/'
driver.get(url)

# HTML 다운로드 및 bs4로 읽기
from bs4 import BeautifulSoup
html = driver.page_source   # 정보확인
soup = BeautifulSoup(html, 'html.parser')

##----------------------------------------------------------------------------------------------------------------------
# 실시간 곡 차트 끌어오기
# 들어갈 때부터 실시간 곡 차트 페이지로 
# #CHARTrealtime
# #CHARTrealtime > table
# realtime_info = 'div#CHARTrealtime > table.list.trackList.byChart'

songs = soup.select('div#CHARTrealtime > table.list.trackList.byChart > tbody > tr')
print(len(songs))
# print(songs)
print('Bugs 실시간 차트 보기')

songs_list = []

for song in songs:
    rank = song.select('td > div.ranking > strong')[0].text
    title = song.select('th > p.title > a')[0].text
    artist = song.select('td.left > p.artist > a')[0].text
    album = song.select('td.left > a.album')[0].text
    
    # 빈 리스트에 저장하기
    songs_list.append({'rank' : rank,
                       'song' : title,
                       'artist' : artist,
                       'album' : album})
    
    # 실시간 곡 정보 보여주기
    print(f'곡제목 : {title}\n가수명 : {artist}\n앨범명 : {album}')
    print('='*10, rank, '번째 저장 완료', '='*10)

import pandas as pd
bugs = pd.DataFrame(songs_list)
print(bugs)
bugs.to_excel('./bugs_realtime_chart.xlsx', index=False)

driver.quit()




