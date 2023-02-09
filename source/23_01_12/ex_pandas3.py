import numpy as np
import pandas as pd
import os
from timeit import default_timer as timer
import matplotlib.pyplot as plt
from sklearn import preprocessing
import seaborn as sns

os.chdir("../AI/COG_ICT/data")
plt.rcParams['font.family'] = 'New Gulim'
plt.rcParams['font.size'] = 14
plt.rcParams['axes.unicode_minus'] = False

# ============================================ #
# =============== 데이터 구해오기 ============= #
# ===== 1. 서울시 자치구 년도별 CCTV 현황  ===== #
# ===== 2. 서울시 주민등록인구 (구별) 현황 ===== #
# ============================================ #

CCTV = pd.read_csv('cctv_in_seoul20230112.csv', 
                    skiprows=1, 
                    thousands=',',
                    encoding="ms949")
POP = pd.read_csv('pop_in_seoul20230112.csv',
                   skiprows=1,
                   usecols=["동별(2)", "계", "한국인", "등록외국인", "65세이상고령자"],
                   encoding="utf-8-sig")

# # (1) 결측치, Column dType 판단
# print(CCTV.info()) 
# print(POP.info())

# # (2) CCTV에서 0번행 삭제
CCTV.drop(0, inplace=True)
# print(CCTV)

# (3) POP Column 바꾸기
POP.columns = ["구별", "인구수", "한국인", "외국인", "고령자"]
POP.drop(0, inplace=True)

# # (4) CCTV 데이터에서 총계로 내림차순 정렬
# print(CCTV.sort_values("총계", ascending=False))

# (5) CCTV 최근 증가율
CCTV["최근증가율"] = (CCTV["2021년"] + CCTV["2020년"] + CCTV["2019년"]) / CCTV["총계"] * 100
# print(CCTV)

# # (6) 최근 증가율 내림차순 정렬
# print(CCTV.sort_values("최근증가율", ascending=False))

# (7) POP에서 외국인 비율, 고령자 비율 추가
POP["외국인비율"] = POP["외국인"] / POP["인구수"] * 100
POP["고령자비율"] = POP["고령자"] / POP["인구수"] * 100
# print(POP)

# (8) CCTV에서 컬럼 인덱스 중에 구분->구별, 총계->CCTV총계
# print(CCTV.head(1))
CCTV.rename(columns= {"구분":"구별", "총계":"CCTV총계" }, inplace=True)
# print(CCTV.head(1))

# # (9) CCTV, POP을 구별을 기준으로 병합해서 DATA_RESULT에 저장
# DATA_RESULT = pd.merge(CCTV, POP, on="구별")
# # print(DATA_RESULT) # CCTV와 POP의 ENTRIES 25와는 다르게 ENTRIES가 24밖에 안 된다. -> 양쪽에 모두 존재하는 값에 대해서만 MERGE했기 때문
# # print(CCTV[CCTV['구별'] != POP['구별']]) # CCTV는 "중 구", POP은 "중구"라고 저장되어 있기 때문에
# # CCTV.iloc[1,0] = "중구"
# print(DATA_RESULT)

# (10) CCTV, POP 병합 (단, CCTV총계, 최근 증가율만 가져와서 병합)
DATA_RESULT =pd.merge(CCTV[["구별", "CCTV총계", "최근증가율"]], POP, on="구별")
# print(DATA_RESULT)

# (11) data_result에 index를 구별로 설정하시오
DATA_RESULT.set_index("구별", inplace=True)
# print(DATA_RESULT)

# ======================== #
# ===== 상관관계 분석 ===== #
# ======================== #

# 상관관계 계수 (-1 ~ 1)
#  -     ~ 0.1: 관계 없음, 무시
#  - 0.1 ~ 0.3: 약한 상관관계
#  - 0.3 ~ 0.7: 뚜렷한 상관관계
#  - 0.7 ~ 1.0: 높은 상관관계

# # (1) 고령자 비율, CCTV 총계 상관관계
# print(np.corrcoef(DATA_RESULT["고령자비율"], DATA_RESULT["CCTV총계"])) # 고령자 비율이 높을 수록 CCTV 수가 줆. (가정에 문제가 있다고 판단할 수도 있음)

# (2) 인구대비 CCTV 수
DATA_RESULT["인구대비CCTV비율"] = DATA_RESULT["CCTV총계"] / DATA_RESULT["인구수"] * 100
# print(DATA_RESULT)

# # (3) 고령자 비율, 인구대비 CCTV 비율 상관관계
# print(np.corrcoef(DATA_RESULT["고령자비율"], DATA_RESULT["인구대비CCTV비율"])) # 약한 상관관계

# # (4) 외국인 비율, 인구대비 CCTV 비율 상관관계
# print(np.corrcoef(DATA_RESULT["외국인비율"], DATA_RESULT["인구대비CCTV비율"])) # 뚜렷한 상관관계

# # (5) 다양한 분석
# print(np.corrcoef(DATA_RESULT["인구수"], DATA_RESULT["CCTV총계"]))
# print(np.corrcoef(DATA_RESULT["인구수"], DATA_RESULT["인구대비CCTV비율"])) # 음의 상관관계, 밀집도가 다르기 때문에 발생

# # (6) CCTV총계를 내림차순으로 정렬해서 막대그래프로 그려보시오.
# bar_graph = DATA_RESULT["CCTV총계"].sort_values(ascending=False).plot(kind='bar')
# plt.show()

# # (7) 인구대비 CCTV 비율 내림차순 막대그래프
# bar_graph = DATA_RESULT["인구대비CCTV비율"].sort_values().plot(kind='barh') # 오름차순으로 해야 수평 막대그래프에서는 제일 위로 올라간다
# plt.show()

# # (8) Scatter 그래프를 사용해서, 인구수(x축), CCTV총계(y축)으로 그려보시오
# plt.figure(figsize=(6,6), dpi=120)
# plt.scatter(DATA_RESULT['인구수'], DATA_RESULT['CCTV총계'], s=50)
# plt.xlabel("인구수")
# plt.ylabel("CCTV총계")
# plt.grid()
# plt.show()

# # (9) 경향선(추세선)을 추가해보자.
# fp1 = np.polyfit(DATA_RESULT["인구수"], DATA_RESULT["CCTV총계"], 1) # 1차 방정식
# # print(fp1) # [4.08446860e-03 1.76042642e+03] -> 기울기, y절편
# f1 = np.poly1d(fp1) # 기울기와 y절편 값을 주면 함수를 만들어준다.

# fx = [100000, 700000] # 정의역 설정

# plt.figure(figsize=(6,6), dpi=120)
# plt.scatter(DATA_RESULT['인구수'], DATA_RESULT['CCTV총계'], s=50)

# plt.plot(fx, f1(fx), 'r--')

# plt.xlabel("인구수")
# plt.ylabel("CCTV총계")
# plt.grid()
# plt.show()

# # (10) 원의 크기와 색에 상관관계 부여
# fp1 = np.polyfit(DATA_RESULT["인구수"], DATA_RESULT["CCTV총계"], 1)
# f1 = np.poly1d(fp1)
# fx = [100000, 700000]

# plt.figure(figsize=(6,6), dpi=120)
# plt.scatter(DATA_RESULT['인구수'], DATA_RESULT['CCTV총계'], 
#             s = (DATA_RESULT["인구대비CCTV비율"]*10) ** 2,
#             c = DATA_RESULT["외국인비율"])
# plt.colorbar()
# plt.plot(fx, f1(fx), 'r--')
# plt.xlabel("인구수")
# plt.ylabel("CCTV총계")
# plt.grid()
# plt.show()

# # (11) 원의 정보 기입하기 : plt.text() + 좌표 보정
# fp1 = np.polyfit(DATA_RESULT["인구수"], DATA_RESULT["CCTV총계"], 1)
# f1 = np.poly1d(fp1)
# fx = [100000, 700000]

# plt.figure(figsize=(6,6), dpi=120)
# plt.scatter(DATA_RESULT['인구수'], DATA_RESULT['CCTV총계'], 
#             s = (DATA_RESULT["인구대비CCTV비율"]*10) ** 2,
#             c = DATA_RESULT["외국인비율"])

# for gName in DATA_RESULT.index:
#     x = DATA_RESULT.at[gName, "인구수"] * 1.02
#     y = DATA_RESULT.at[gName, "CCTV총계"] * 0.98
#     plt.text(x,y,gName)

# plt.colorbar()
# plt.plot(fx, f1(fx), 'r--')
# plt.xlabel("인구수")
# plt.ylabel("CCTV총계")
# plt.grid()
# plt.show()

# # (12) 오차가 크지 않으면 이름 제거
fp1 = np.polyfit(DATA_RESULT["인구수"], DATA_RESULT["CCTV총계"], 1)
f1 = np.poly1d(fp1)
fx = [100000, 700000]

DATA_RESULT["오차"] = np.abs(DATA_RESULT["CCTV총계"] - f1(DATA_RESULT["인구수"]))

# plt.figure(figsize=(6,6), dpi=120)
# plt.scatter(DATA_RESULT['인구수'], DATA_RESULT['CCTV총계'], 
#             s = (DATA_RESULT["인구대비CCTV비율"]*10) ** 2,
#             c = DATA_RESULT["외국인비율"])

# for gName in DATA_RESULT.index:
#     if 0 <= DATA_RESULT.at[gName, "오차"] < 1000:
#         continue
#     x = DATA_RESULT.at[gName, "인구수"] * 1.02
#     y = DATA_RESULT.at[gName, "CCTV총계"] * 0.98
#     plt.text(x,y,gName)

# plt.colorbar()
# plt.plot(fx, f1(fx), 'r--')
# plt.xlabel("인구수")
# plt.ylabel("CCTV총계")
# plt.grid()
# plt.show()

# ================================== #
# ===== 범죄현황과 상관관계 분석 ===== #
# ================================== #

# 서울시 5대 범죄 발생현황 통계

CRIME = pd.read_csv('crime_in_seoul20230112.csv',
                    skiprows=3,
                    encoding="utf-8-sig",
                    usecols=["자치구별(2)", "발생.1", "검거.1", "발생.2", "검거.2","발생.3", "검거.3","발생.4", "검거.4", "발생.5", "검거.5"])
CRIME.columns = ["구별", "살인발생", "살인검거", "강도발생", "강도검거", "강간강제추행발생", "강간강제추행검거", "절도발생", "절도검거", "폭력발생", "폭력검거"]
CRIME.drop(0, inplace=True)
CRIME.set_index("구별", inplace=True)
# print(CRIME)

# (1) 각 범죄마다 검거율을 추가해보자.

# CRIME["살인검거율"] = CRIME["살인검거"] / CRIME["살인발생"] * 100
# CRIME["강도검거율"] = CRIME["강도검거"] / CRIME["강도발생"] * 100
# CRIME["강간강제추행검거율"] = CRIME["강간강제추행검거"] / CRIME["강간강제추행발생"] * 100
# CRIME["절도검거율"] = CRIME["절도검거"] / CRIME["절도발생"] * 100
# CRIME["폭력검거율"] = CRIME["폭력검거"] / CRIME["폭력발생"] * 100

for n in ["살인", "강도", "강간강제추행", "절도", "폭력"]:
    CRIME[n + "검거율"] = CRIME[n + "검거"] / CRIME[n + "발생"] * 100

# print(CRIME)

# (2) 검거율이 100보다 큰 경우 (사건 발생 일자와 검거 일자가 달라서 발생) 값을 100으로 조정
for c in CRIME.columns:
    if '검거율' in c:
        CRIME.loc[CRIME[c] > 100, c] = 100

# print(CRIME)

# (3) 검거 비율만 남기고 나머지는 삭제
# for c in CRIME.columns:
#     if '발생' in c and '검거' in c and '율' not in c:
#         del CRIME[n]
        
for c in CRIME.columns:
    if c.endswith('검거'):
        del CRIME[c]

# print(CRIME)

# (4) "발생"문자만 지워주자
for c in CRIME.columns:
    if c.endswith('발생'):
        CRIME.rename(columns={c:c[:-2]}, inplace=True)

# print(CRIME) 


# =================================== #
# ===== 데이터 정규화 (Nomalize) ===== #
# =================================== #

# (1) min-max nomalize 방법
x = CRIME[ ['살인', '강도', '강간강제추행', '절도', '폭력'] ]
# print(x)

min_max_scaler = preprocessing.MinMaxScaler()
x_scaled = min_max_scaler.fit_transform(x.astype(float)) # data들로 학습을 시켜준다고 보면 된다. (x -> float 형태로 줘야 한다.)
# print(x_scaled) # np.ndarray값으로 리턴해줌

CRIME_norm = pd.DataFrame(x_scaled, index=x.index, columns=x.columns)
# print(CRIME_norm)

# (2) CRIME_norm에 CRIME의 각 검거율을 추가
for c in CRIME.columns:
    if '검거율' in c:
        CRIME_norm[c] = CRIME[c]
# print(CRIME_norm)

# (3) CRIME_norm에 DATA_RESULT 인구수, CCTV 총계 정보 추가하시오.
CRIME_norm[ ['인구수', 'CCTV총계', '최근증가율'] ] = DATA_RESULT[ ['인구수', 'CCTV총계', '최근증가율'] ]
# print(CRIME_norm)

# (4) 범죄 컬럼을 만드시오. 범죄 = 모든 범죄의 발생 수의 합
CRIME_norm['범죄'] = CRIME_norm.loc[:, '살인':'폭력'].sum(axis=1)
# print(CRIME_norm)

# (5) 살인검거율 ~ 폭력검거율 합
CRIME_norm['검거'] = CRIME_norm.loc[:, '살인검거율':'폭력검거율'].sum(axis=1)
# print(CRIME_norm)

# # (6) 이쁘게 그리기
# sns.pairplot(CRIME_norm)
# plt.show()

# # (7) 관심있는 내용만 그리기 + 추세선 추가
# sns.pairplot(CRIME_norm[ ['인구수', 'CCTV총계', '최근증가율', '범죄', '검거'] ], kind='reg')
# plt.show()

# (8) 검거의 최대값으로 각 검거의 값을 나누고 * 100 해서 다시 검거에 저장하시오.
CRIME_norm['검거'] = CRIME_norm['검거'] / CRIME_norm['검거'].max() * 100
# print(CRIME_norm)

# (9) 정렬
CRIME_norm_sorted = CRIME_norm.sort_values('검거', ascending=False)

# (10) hitmap
plt.figure(figsize=(10,25), dpi=100)
sns.heatmap(CRIME_norm_sorted[ ['살인검거율', '강도검거율', '강간강제추행검거율', '절도검거율', '폭력검거율', '검거'] ],
                                annot=True, fmt='.2f', cmap='YlGnBu')
plt.show()

