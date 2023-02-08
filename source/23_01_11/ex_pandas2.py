import pandas as pd
import os
from timeit import default_timer as timer
import matplotlib.pyplot as plt
import numpy as np

os.chdir("../AI/COG_ICT/data")
plt.rcParams['font.family'] = 'New Gulim'

casts = pd.read_csv('cast.csv')

## ================= ##
## ===== Index ===== ##
## ================= ##


# print(casts.head())

# start = timer()
# print(casts[casts['title'] == 'Macbetch'])
# end = timer()
# print(f"timer = {end - start}") # 0.0065724

# title_casts = casts.set_index('title')
# start = timer()
# print(title_casts.loc['Macbeth']) # 0.022213
# end = timer()
# print(f"timer = {end - start}")

# sort_casts = casts.set_index('title').sort_index()
# start = timer()
# print(sort_casts.loc['Macbeth'])
# end = timer()
# print(f"timer = {end - start}") # 122µs

# multi_casts = casts.set_index(['title', 'year'])
# print(multi_casts.loc['Macbeth'])
# print(multi_casts.xs(1915, level='year'))
# print(multi_casts.xs('Macbeth', level='title')) # multi-index를 접근할 때는 xs를 선호

# multi_casts = casts.set_index(['title', 'year'])
# print(multi_casts.reset_index(['title', 'year'])) # multi-index를 다시 column 값으로 돌려준다.

# # 전체 컬럼 카테고리 바꾸기
# multi_casts.columns = ['이름', '종류', '배역', '평가']
# print(multi_casts.head(1))
# # 특정 컬럼만 바꾸기
# print(multi_casts.rename(columns={'종류':'성별'}))


## ==================== ##
## ===== File I/O ===== ##
## ==================== ##

# df = pd.read_csv('ex1.csv')
# print(df.info())

# df2 = pd.read_table('ex1.csv')
# print(df2.info()) # ','로 값을 구분하지 못해서 하나의 덩어리로 취급

# df2 = pd.read_table('ex1.csv', sep=',')
# print(df2) # read_csv()와 똑같이 작동

# df3 = pd.read_csv('ex2.csv', header=0)
# print(df3)

# df4 = pd.read_csv('ex2.csv', names=['a', 'b', 'c', 'd', 'msg'])
# print(df3)

# df5 = pd.read_csv('ex3.csv', comment='#')
# print(df5)

# df6 = pd.read_csv('ex3.csv', skiprows=[0, 3])
# print(df6)

# df7 = pd.read_csv('ex4.csv', index_col=0)
# print(df7)

# df5.to_csv('ex6.csv', index=False)
# df5.to_excel('ex7.xlsx')
# df9 = pd.read_excel('ex7.xlsx', index_col=False)
# print(df9)


## ============================= ##
## ===== 기상청 데이터 처리 ===== ##
## ============================= ##

# dg_temp = pd.read_csv('daegu_temp_20230111.csv', skiprows=8, encoding='utf-8', names=['날짜', '지점', '평균기온', '최저기온', '최고기온'])
# dg_temp['날짜'] = dg_temp['날짜'].str.strip() # \t 제거
# # # print(dg_temp[dg_temp['평균기온(℃)'].isnull()])
# # # print(dg_temp[9399:9410]) # 비어있는 값 존재
# dg_temp.fillna(method='bfill', inplace=True) # 비어있는 값 채움
# # # print(dg_temp[9399:9410]) # 비어있는 값 제거
# # # print(dg_temp.info())
# del dg_temp['지점']
# # # print(dg_temp.haed(1))
# # # print(dg_temp.head(1))

# # ===== 1. 최고기온을 구하고, 날짜 구하기 ===== #
# print(dg_temp['최고기온'].max())
# print(dg_temp.iloc[2384, 0]) # (방법1) 5.73µs
# print(dg_temp.iat[2384, 0])  # (방법2) 3.68µs 이게 연산 속도가 빠르다

# dg_temp2 = dg_temp.set_index('날짜') # 인덱스 번호 -> 날짜로 변경 
# # print(dg_temp2.head())
# print(dg_temp2['최고기온'].idxmax()) # (방법3)

# # ===== 2. 최고기온 Top 10을 구해보시오
# print(dg_temp2.sort_values('최고기온', ascending=False)['최고기온'].head(10))

# # ===== 3. 최저기온 Top 10을 구해보시오
# print(dg_temp2.sort_values('최저기온')['최저기온'].head(10))


## ================= ##
## ===== Merge ===== ##
## ================= ##

# df1 = pd.DataFrame( {
#     'key' : ['b', 'b', 'a', 'c', 'a', 'a', 'b'],
#     'data1':range(7)
# })
# df2 = pd.DataFrame({
#     'key' : ['a', 'b', 'd', 'b'],
#     'data2':range(4)
# })

# print(pd.merge(df1, df2))
# print(df1.merge(df2))       # 둘 다 같은 방법

# print(pd.merge(df1, df2, left_on='data1', right_on='data2')) # 공통되는 기준이 없으면 버린다
# print(pd.merge(df1, df2, left_on='data1', right_on='data2', how='left'))  # left 기준으로 무조건 생성하고 없는 값은 Null로 채운다
# print(pd.merge(df1, df2, left_on='data1', right_on='data2', how='right')) # right 기준
# print(pd.merge(df1, df2, left_on='data1', right_on='data2', how='outer')) # 양쪽 모두 기준

# df1 = pd.DataFrame( {
#     'key1' : ['b', 'b', 'a', 'c', 'a', 'a', 'b'],
#     'data1':range(7)
# })
# df2 = pd.DataFrame({
#     'key2' : ['a', 'b', 'd', 'b'],
#     'data2':range(4)
# })

# print(pd.merge(df1, df2)) # 에러, 공통된 column이 없기 때문에
# print(pd.merge(df1, df2, left_on='key1', right_on='key2', how="outer"))


## ===================================== ##
## ===== Concatenation(데이터 결합) ===== ##
## ===================================== ##

# s1 = pd.Series([0,1], index=['a', 'b'])
# s2 = pd.Series([2,1,3], index=['c', 'd', 'e'])
# s3 = pd.Series([4,7], index=['a', 'e'])

# # print(s1, s2, s3, sep='\n')

# print(pd.concat([s1, s2]))
# print(pd.concat([s1, s2], axis=1)) # 열로 추가
# print(pd.concat([s1, s3], axis=1))

# df1 = pd.DataFrame( {
#     'key1' : ['b', 'b', 'a', 'c', 'a', 'a', 'b'],
#     'data1':range(7)
# })
# df2 = pd.DataFrame({
#     'key2' : ['a', 'b', 'd', 'b'],
#     'data2':range(4)
# })

# print(pd.concat([df1, df2]))         # merge  : 조합을 구성하여 바인딩해준다.
# print(pd.concat([df1, df2], axis=1)) # concat : 행 or 열로 붙일지만 결정


## ================================ ##
## ===== Time Series (시계열) ===== ##
## ================================ ##

# rng = pd.date_range('2023-01-11 09:30', periods=10)
# rng = pd.date_range('2023-01-11 09:30', periods=10, freq='B') # Business Day (구글에 표 검색)
# rng = pd.date_range('2023-01-11 09:30', periods=10, freq='50T') # 50분 간격
# rng = pd.date_range('2023-01-11 09:30', periods=10, freq='50T', tz='Asia/Seoul') # 서울 시간 기준

# print(rng.tz_convert('Australia/Sydney')) # 시드니 시간 기준

# ===== 문자열 -> 시간 ===== #

# date_data = ['07/07/2023', '08/18/1889', '12/01/1818'] # 미국식 표현법 기준 (mm/dd/yyyy)
# print(pd.to_datetime(date_data))

# print(pd.to_datetime(date_data, dayfirst=True)) # 유럽식 표현법 기준 (dd/mm/yyyy)

# dates = pd.date_range('2023-01-02', '2023-01-09')
# # print(dates)
# atemp = pd.Series([12.3, 13, 14.5, 12, 15, 8, 18, 6], index=dates)
# # print(atemp)
# stemp = pd.Series([11.3, 15, 12.5, 9, 11, 10, 15, 8], index=dates)
# df = pd.DataFrame({'대구': atemp, '경산': stemp})
# # print(df)
# df['기온차'] = df['대구'] - df['경산'] # column 추가
# # print(df)

# print(df.loc['2023-01-05'])
# print(df.loc['01/05/2023']) # 날짜 표기법으로 되어 있으면 이렇게도 선택할 수 있다.
# print(df.loc['Jan. 05. 2023'])
# print(df.loc['2023-01'])    # Month까지만 선택하면 해당 월의 모든 데이터를 얻을 수 있다.
# print(df.loc['2023'])
# print(df['2023']) # index처럼 사용하기 때문에 column으로도 select할 수 있다.
# print(df['2023/01'])

## ========================================== ##
## ===== 기상청 데이터 (날짜 인덱스 사용) ===== ##
## ========================================== ##

dg_temp2 = pd.read_csv('daegu_temp_20230111.csv', 
                        skiprows=8, 
                        encoding='UTF-8-sig',
                        names=['날짜', '지점', '평균기온', '최저기온', '최고기온'],
                        index_col='날짜',
                        parse_dates=['날짜'])

# print(dg_temp2.loc['2022']['최고기온'].max())
# print(dg_temp2.loc['2022']['최고기온'].idxmax())

# ===== 연도별 최고기온, 최저기온 ===== #

# dg_temp_ann = dg_temp2.to_period('A') # 연단위로 바꿈
# # print(dg_temp_ann.groupby('날짜')['최고기온'].max())
# # print(dg_temp_ann.groupby('날짜')['최저기온'].min())

# high_tmp = dg_temp_ann.groupby('날짜')['최고기온'].max()
# low_tmp  = dg_temp_ann.groupby('날짜')['최저기온'].min()

# p = pd.merge(high_tmp, low_tmp, on='날짜')
# # p.plot(kind='bar')
# # plt.show()
    
# decade_temp = dg_temp_ann.groupby((dg_temp_ann.index.year // 10 * 10)).max()
# print(decade_temp)

## =============================== ##
## ===== 시각화 (Matplotlib) ===== ##
## =============================== ##

# plt.plot( [1,3,5,7,9,10], [1,3,4,2,5,8] )
# plt.xlabel( 'time' )
# plt.ylabel( 'grade' )
# plt.title('My First Graph')
# plt.show()

# == 한글 폰트로 지정하는 방법? == #

# import matplotlib.font_manager as fm

# font_list = fm.findSystemFonts()

# print(font_list)
# for f in font_list:
#     if 'GULIM' in f:
#         print(f)

# print(fm.FontProperties(fname='C:\\Windows\\Fonts\\NGULIM.TTF').get_name()) # New Gulim

# for f in font_list: 
#     print(fm.FontProperties(fname=f).get_name()) # 폰트 이름 모두 찾아보기

# ============================== #

# plt.rcParams['font.family'] = 'New Gulim'
# plt.rcParams['font.size'] = 14
# plt.plot( [1,3,5,7,9,10], [1,3,4,2,5,8], 'rD-.' )
# plt.xlabel( '시간' )
# plt.ylabel( '등급' )
# plt.title('첫 번째 그래프')
# plt.show()


x = np.arange(0, 10)
y = np.arange(0, 100, 10)

# # 범위를 다소 크게
# plt.plot(x, y)
# plt.grid()
# plt.xticks( x ) # 값이 있는 위치마다 모두 좌표 찍기
# plt.yticks( y )
# plt.show()

# # 범위를 세밀하게
# plt.plot(x,y, color='red', linestyle='--', linewidth=4)
# plt.grid()
# plt.xticks( np.arange(0,10,0.5) ) # 값이 있는 위치마다 모두 좌표 찍기
# plt.yticks( [20, 50, 90] )
# plt.show()

# # 그래프 겹쳐서 그리기
# plt.rcParams['font.family'] = 'New Gulim'
# plt.figure( figsize=(6,4) )
# plt.plot(x, y, label='경산')
# plt.plot(x, x**2, label='대구')
# plt.plot(x, x*y*4, label='부산')
# plt.legend() # 범례
# plt.grid()
# plt.show()

# # 파일 저장
# plt.rcParams['font.family'] = 'New Gulim'
# plt.figure( figsize=(6,4) )
# plt.plot(x, y*2, 'g-.h', label='경산')
# plt.plot(x, x**2, 'k:D', label='대구')
# plt.plot(x, x*y, 'r-->', label='부산')
# plt.legend() # 범례
# plt.grid()
# plt.savefig('myfirst.png', dpi=150) # dpi : 해상도
# plt.show()

# # 막대 그래프
# labels = ['a', 'b', 'c']
# values = [10, 50, 20]
# plt.bar(labels, values)
# plt.show()

# # 막대 그래프 width 조정
# labels = ['a', 'b', 'c']
# values = [10, 50, 20]
# plt.bar(labels, values, width=0.3)
# plt.show()

# # 막대 그래프 패턴 조정
# labels = ['a', 'b', 'c']
# values = [10, 50, 20]
# bars = plt.bar(labels, values, width=0.3)
# bars[0].set_hatch('x')
# bars[1].set_hatch('-')
# bars[2].set_hatch('\\')
# plt.show()

## ======================================== ##
## ===== 산포도 그래프 (Scatter Graph) ===== ##
## ======================================== ##

# plt.scatter(10, 20, s=300, c='green') # 좌표 기입
# plt.show() 

# x = np.arange(0, 20, 2)
# plt.scatter(x, x**2, s=x*10, c=x*30)
# plt.text(10, 100, "중요한 값")
# plt.show()

# # color 정보
# x = np.arange(0, 20, 2)
# plt.scatter(x, x**2, s=x*10, c=x*30)
# plt.text(10, 100, "중요한 값")
# plt.colorbar()
# plt.show()

## =================== ##
## ===== SubPlot ===== ##
## =================== ##

plt.figure(figsize=(6,4), dpi=100)

plt.subplot(1,3,1) # 구분 그래프를 1행 3열, 그 중에서 첫 번째 값을 지정
plt.plot([1,5,7], [10, 50, 20])
plt.title('(a) 온도')

plt.subplot(132) # comma 없이도 구분
plt.scatter(x, x**2, s=x*10, c=x*30)
plt.title('(b) 인구수')

plt.subplot(133)
plt.bar(['x', 'y', 'z'], [100, 30, 60])
plt.title('(c) 소득')

plt.suptitle('경산 인구 및 소득')

plt.show()