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
import urllib

os.chdir("../AI/COG_ICT/data")
plt.rcParams['font.family'] = 'New Gulim'
plt.rcParams['font.size'] = 14
plt.rcParams['axes.unicode_minus'] = False

# ========================= #
# ===== Mini-Project2 ===== #
# ========================= #

# 네이버 영화 포스트 정보 받기

def get_poster_info(webUrl):
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    imgUrls = [x['src'].split('?')[0] for x in soup.select('p.result_thumb img')]
    titles = [a.get_text() for a in soup.select("dt a")]
    posterInfo = dict(zip(titles, imgUrls))
    return posterInfo

def getAllTitlesAndImgs(url):
    d, page = {}, 1

    while True:
        tmp = get_poster_info(url + '&page=' + str(page))

        pre = len(d)
        d.update(tmp)
        nxt = len(d)

        if pre == nxt:
            break
        page += 1
    return d

def downloadImg(filename, url):
    img = requests.get(url)
    img.raise_for_status() # Exception Handling

    with open(filename, 'wb') as f:
        f.write(img.content)
    print(f'{filename} download success : {len(img.content)/1000}kB')

def remove_whitespace(s):
    tmp = s.replace('/', '')
    tmp = tmp.replace(':', "")
    tmp = tmp.replace(' ', '')
    return tmp

def downloadMoviePoster(name, url):
    titlesAndUrls = getAllTitlesAndImgs(url)
    os.makedirs(name, exist_ok=True) # 이미 폴더가 존재하면 덮어씌우기
    for title in titlesAndUrls:
        if 'poaster_default.gif' in titlesAndUrls[title]: continue
        filename = './' + name + '/' + remove_whitespace(title) + '.jpg'
        url = titlesAndUrls[title]
        downloadImg(filename, url)

if __name__ == '__main__':
    target = input("찾으시는 영화 정보를 입력해주세요 : ")
    url = f"https://movie.naver.com/movie/search/result.naver?section=movie&query={urllib.parse.quote(target)}"
    downloadMoviePoster(target, url)



