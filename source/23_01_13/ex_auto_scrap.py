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

def genPayload(stnId, startDay, endDay):
    payload = {
        'fileType': 'csv',
        'pgmNo': 70,
        'menuNo': 432,
        'serviceSe': 'F00101',
        'stdrMg': '99999',
        'startDt': startDay,
        'endDt': endDay,
        'taElement': 'MIN',
        'taElement': 'AVG',
        'taElement': 'MAX',
        'stnGroupSns': '',
        'selectType': 1,
        'mddlClssCd': 'SFC01',
        'dataFormCd': 'F00501',
        'dataTypeCd': 'standard',
        'startDay': startDay,
        'startYear': 2013,
        'endDay': endDay,
        'endYear': 2023,
        'startMonth': '01',
        'endMonth': '12',
        'sesnCd': 0,
        'txtStnNm': '대구',
        'stnId': stnId,
        'areaId': '',
        'gFontSize': ''
    }
    return payload

def downloadTempCSV(stnId, startDay, endDay):
    # headers = {
    # 'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    # 'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7'
    # }
    payload = genPayload(stnId, startDay, endDay)
    url = "https://data.kma.go.kr/stcs/grnd/downloadGrndTaList.do"
    filename = str(stnId) + str(startDay) + str(endDay) + '.csv'
    response = requests.post(url, data=payload)
    
    response.raise_for_status()

    with open(filename, 'wb') as f:
        f.write(response.content)
    print(f"{filename} download success")
    return filename

filename = downloadTempCSV(143, 19800101, 19891231)
tmp = pd.read_csv("1431980010119891231.csv", 
                  skiprows=7, 
                  encoding='ms949', 
                  index_col='날짜', 
                  parse_dates=['날짜'])
print(tmp.to_period('M').groupby('날짜').max().iloc[:,3])

