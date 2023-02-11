import numpy as np
import pandas as pd
import os
from timeit import default_timer as timer
import matplotlib.pyplot as plt
from sklearn import preprocessing
import seaborn as sns
from bs4 import BeautifulSoup
import requests
from datetime import datetime
from PIL import Image
from io import BytesIO
import time

os.chdir("../AI/COG_ICT/data")
plt.rcParams['font.family'] = 'New Gulim'
plt.rcParams['font.size'] = 14
plt.rcParams['axes.unicode_minus'] = False

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
url = "https://www.yu.ac.kr/main/index.do"
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

# print(soup.prettify())
# print(list(soup.children))

# print(soup.find_all('p', class_="mini-title"))

# ========================
# ===== CSS Selector =====
# ========================

# # new_title = soup.select('div.main-news-box p.mini-title')
# # print(new_title[0].text)

news_txt_boxes = soup.select('div.news-txt-box')

titles_with_dates = [(div.p.get_text(), div.span.get_text()) for div in news_txt_boxes]
# print(titles_with_dates)

yu_newsroom = pd.DataFrame(titles_with_dates, columns=['제목', '게시날짜'])

# # 수집 날짜 추가하기
today = datetime.today().strftime("%Y-%m-%d")
yu_newsroom['수집날짜'] = today

# # print(yu_newsroom)

# # yu_newsroom.to_excel('yu_newsroom' + today + 'xlsx')

# ============================== #
# ===== 주기적 프로그램 실행 ===== #
# ============================== #
# crontab: 리눅스나 유닉스 서버에서 주기적으로 프로그램을 실행할 때 사용한다.

# (1) 이미지 주소 확보

imgTags = soup.select('.news-img-box')
imgUrl = []
for imgTag in imgTags:
    style = imgTag['style']
    url = style[ style.find('(')+1 : style.find(')') ]
    imgUrl.append('https://www.yu.ac.kr' + url)
# print(imgUrl)

# # (2) 이미지 화면에 띄워보기
# img1 = requests.get(imgUrl[0])
# # print(img1.status_code) # 200 : 양호
# img = Image.open(BytesIO(img1.content))
# plt.imshow(img)
# plt.axis('off')
# plt.show()

# # (3) 이미지 저장하기
# with open('img1.jpg', 'wb') as f:
#     f.write(img1.content)

# (4) 자동화 시작
def downloadImg(filename, url):
    img = requests.get(url)
    img.raise_for_status() # Exception Handling

    with open(filename, 'wb') as f:
        f.write(img.content)
    print(f'{filename} download success : {len(img.content)/1000}kB')
# downloadImg('img2.jpg', imgUrl[1])

yu_newsroom['이미지파일'] = None
# print(yu_newsroom)

# for idx, url in enumerate(imgUrl):
#     filename = str(int(time.time() * 100)) + '.jpg'
#     downloadImg(filename, url)
#     yu_newsroom.iloc[idx, 3] = filename

# print(yu_newsroom)
