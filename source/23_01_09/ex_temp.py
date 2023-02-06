# 기상청 데이터 분석 예제

import numpy as np
import os

os.chdir("../AI/COG_ICT/data")

daeguTemp = np.loadtxt('daegu_temp_20230110.csv', delimiter=',', encoding="utf-8-sig", dtype=np.float64)

# # == 최고기온

# print(np.max(daeguTemp, axis=0)[4]) 

# np.max(daeguTemp[:, 4])

# # == 최저기온

# print(np.min(daeguTemp, axis=0)[4])

# np.min(daeguTemp[:, 4])

# # == When?

# print(np.argmax(daeguTemp[:, 4])) # row
# print(daeguTemp[1303, 0].astype(np.int64)) # 날짜

# print(np.argmin(daeguTemp[:, 3]))
# print(daeguTemp[1122, 0].astype(np.int64))

# # == 최저기온, 최고기온 Top10

# # max_day = 

# max_days = {}
# min_days = {}
# for i in range(10):
#     row = np.argmax(daeguTemp[:, 4])
#     max_days[daeguTemp[row, 0].astype(np.int64)] = daeguTemp[row, 4]
#     daeguTemp = np.delete(daeguTemp, row, axis=0)

#     row = np.argmin(daeguTemp[:, 4])
#     min_days[daeguTemp[row, 0].astype(np.int64)] = daeguTemp[row, 4]
#     daeguTemp = np.delete(daeguTemp, row, axis=0)

# print(max_days)
# print(min_days)

# # == 각 연도별 최고, 최저기온을 구해보시오.

# def max_temp_on_year(data, year):
#     return np.max(data[data[:, 0] // 10000 == year, 4])

# D = {}
# for year in range(int(daeguTemp[0,0]//10000), int(daeguTemp[-1, 0]//10000 + 1)):
#     D[year] = max_temp_on_year(daeguTemp, year)

# print(D)

