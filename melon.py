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
driver.maximize_window()

# url
url = 'https://www.melon.com/chart/index.htm'
driver.get(url)

# HTML 다운로드 및 bs4로 읽기
from bs4 import BeautifulSoup
html = driver.page_source   # 정보확인
soup = BeautifulSoup(html, 'html.parser')
# print(soup)

# 100개의 노래 tag 찾기
# 1. NGD
# print(soup.select('tbody > tr'))
# songs = soup.select('tr')[1:]
# print(len(songs))
# print(songs[0])
# song = songs[0]
# print(song.select('a'))
# title = song.select('a')
# print(len(title))
# print(title[0]) # None
# print(title[1]) # 곡정보
# print(title[2].text) # 곡제목

# 2. 조금 더 스마트 하게
# print(song.select('span > a'))
# title = song.select('span > a')
# print(title)
# print(title[0])
# print(title[0].text)

# 3. 곡 제목 찾는 방법 - 그나마 정말 스마트 하게
# div : class = 'ellipsis rank01'
# title = song.select('div.ellipsis.rank01 > span > a')
# print(title)
# print(len(title))
# print(title[0])
# print(title[0].text)

# 3-1. 가수 정보 찾기
# singer = song.select('div.ellipsis.rank02 > a')
# print(singer[0].text)

# 앨범 정보 찾기
# <div class="ellipsis rank03">
# <a href="javascript:melon.link.goAlbumDetail('11487023');" title="Armageddon - The 1st Album - 페이지 이동">Armageddon - The 1st Album</a>
# </div>
# album = song.select('div.ellipsis.rank03 > a')
# print(album[0].text)

# 좋아요
# like = song.select('span.cnt')
# print(like[0].text.split()[1])

# -------------------------------------------------------------------------------------------
# 멜론 100위 노래 순위 정보 가져오기
# 저장할 리스트
songs_list = []

songs = soup.select('tr')[1:]

for i, song in enumerate(songs):
    # 곡
    title = song.select('div.ellipsis.rank01 > span > a')
    # 가수
    singer = song.select('div.ellipsis.rank02 > a')
    # 앨범명
    album = song.select('div.ellipsis.rank03 > a')
    # 좋아요
    like = song.select('span.cnt')
    
    songs_list.append({'rank' : i+1,
                       'song' : title[0].text,
                       'singer' : singer[0].text,
                       'album' : album[0].text,
                       'likes' : like[0].text.split()[1]})
    
    print('='*10, i+1, '번째 저장 완료', '='*10)

import pandas as pd
melon = pd.DataFrame(songs_list)
print(melon)
melon.to_excel('./melon_top100.xlsx', index=False)

driver.quit()