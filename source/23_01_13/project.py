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

# ======================== #
# ===== Mini-Project ===== #
# ======================== #

# 지점, 시작날짜, 끝날짜 입력받으면 자동으로 기상청에서 해당 데이터를 다운받고
# 각 월별 최고, 최저 기온을 출력하는 프로그램 생성

def printInfo():
    return '''
        서울경기: 서울(108), 인천(112), 수원(119), 강화(201), 양평(202), 이천(203)
		강원영동: 속초(90), 강릉(105), 태백(216)
		강원영서: 철원(95), 대관령(100), 춘천(101), 원주(114), 인제(211), 홍천(212)
		충북: 충주(127), 청주(131), 추풍령(135), 제천(221), 보은(226)
		충남: 서산(129), 대전(133), 천안(232), 보령(235), 부여(236), 금산(238)
                        </td>
                    </tr>
                    <tr>
                        <th scope="row">남부(36)</th>
                        <td class="col_tit">
							경북: 울진(130), 안동(136), 포항(138), 대구(143), 봉화(271), 영주(272), 문경(273), 영덕(277), 의성(278), 구미(279), 영천(281)<br/>								경남: 울산(152), 창원(155), 부산(159), 통영(162), 진주(192), 거창(284), 합천(285), 밀양(288), 산청(289), 거제(294), 남해(295)
							전북: 군산(140), 전주(146), 부안(243), 임실(244), 정읍(245), 남원(247), 장수(248)<br/>
							전남: 광주(156), 목포(165), 여수(168), 완도(170), 장흥(260), 해남(261), 고흥(262)<br/>
                        </td>
                    </tr>
                    <tr>
                        <th scope="row">제주도(4)</th>
                        <td class="col_tit">
                        	제주(184), 고산(185), 성산(188), 서귀포(189)	 
    '''

class Crowling:
    def __init__(self, stnId, startDay, endDay):
        self.stnId = stnId
        self.startDay = startDay
        self.endDay = endDay
        self.filename = ""

    def __genPayload(self):
        payload = {
            'fileType': 'csv',
            'pgmNo': 70,
            'menuNo': 432,
            'serviceSe': 'F00101',
            'stdrMg': '99999',
            'startDt': self.startDay,
            'endDt': self.endDay,
            'taElement': 'MIN',
            'taElement': 'AVG',
            'taElement': 'MAX',
            'stnGroupSns': '',
            'selectType': 1,
            'mddlClssCd': 'SFC01',
            'dataFormCd': 'F00501',
            'dataTypeCd': 'standard',
            'startDay': self.startDay,
            'startYear': 2013,
            'endDay': self.endDay,
            'endYear': 2023,
            'startMonth': '01',
            'endMonth': '12',
            'sesnCd': 0,
            'txtStnNm': '대구',
            'stnId': self.stnId,
            'areaId': '',
            'gFontSize': ''
        }
        return payload

    def __downloadTempCSV(self, filename, response):
        with open(filename, 'wb') as f:
            f.write(response.content)
        self.filename = filename
        return f"{filename} download success"

    def getCSV(self):
        if self.filename == "":
            raise print("파일이 존재하지 않습니다.")
        
        return pd.read_csv(self.filename,
                           skiprows=7,
                           encoding='ms949',
                           index_col='날짜',
                           parse_dates=['날짜'])

    def request(self):
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
        payload = self.__genPayload()
        url = "https://data.kma.go.kr/stcs/grnd/downloadGrndTaList.do"
        filename = str(self.stnId) + str(self.startDay) + str(self.endDay) + '.csv'
        response = requests.post(url, data=payload)
        response.raise_for_status()
        state = self.__downloadTempCSV(filename, response)
        return filename, state

class Calc():
    def __init__(self, data):
        self.data = data

    def getMaxTempEachMonth(self):
        return self.data.to_period('M').groupby('날짜').max()['최고기온(℃)']

    def getMinTempEachMonth(self):
        return self.data.to_period('M').groupby('날짜').min()['최저기온(℃)']

    def mergeMaxMinTemp(self, max, min):
        return 

if __name__ == '__main__':
    entity = Crowling(143, 19880101, 20221231)
    entity.request()
    data = entity.getCSV()
    manager = Calc(data)

    result = pd.merge(
                manager.getMaxTempEachMonth(),
                manager.getMinTempEachMonth(),
                on='날짜'
            )
    print(result)


