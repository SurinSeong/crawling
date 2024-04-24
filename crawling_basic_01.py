html = '''
            <!DOCTYPE html>
            <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <title>multicampus market</title>
                </head>
                <body>
                    <h1>Mulcam market</h1>
                    <div class="sale">
                        <p id="fruits1" class="fruits">
                            <span class="name">바나나</span>
                            <span class="price">3000원</span>
                            <span class="inventory">500개</span>
                            <span class="store">선릉센터</span>
                            <a href="http://google.co.kr">홈페이지</a>
                        </p>
                    </div>
                    <div class="prepare">
                        <p id="fruits2" class="fruits">
                            <span class="name">파인애플</span>
                        </p>
                    </div>
                </body>
            </html>
        '''
# bs4 : beautifulsoup --> 정적(static) 웹문서를 파싱(parsing) 툴
# beautifulsoup 가져오기
from bs4 import BeautifulSoup

# html을 파싱할 것
soup = BeautifulSoup(html, 'html.parser')
# print(soup)

# span 태그만 선택해서 출력
print(soup.select('span')) # 리스트로 묶여 있는 것을 알 수 있음. --> 인덱싱, 슬라이싱 가능
print(soup.select('span')[0])
print(soup.select('span')[-1])

# 기호 사용해도 됨.
print(soup.select('#fruits1')) # 해당 id의 내용이 리스트로 추출됨.
print(soup.select('.price'))
print(soup.select('span.name'))

# 선택하고자하는 태그를 구체적으로 적어줘야 내가 원하는 정보를 정확하게 얻을 수 있다.
tags = soup.select('span.name')
print(tags[0], tags[1])

name_tags = soup.select('.name')
print(name_tags[0], name_tags[1])

# 텍스트만 추출
# 공백 제거를 위해 항상 strip()을 써주는 것이 좋다.
print(name_tags[0].text.strip(), name_tags[1].text.strip())

# 반복문 사용
names = []

for tag in name_tags:
    name = tag.text
    names.append(name)
    print(name.strip())
    
print(names)