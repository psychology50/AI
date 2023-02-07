import numpy as np
import pandas as pd

# # ===== Series =====
# # - 1차원 배열
# # - 리스트, 튜플, ndarray, dict 등으로부터 생성가능

# # == tuple로 Series 만들기 ==
# h = (1, 3, 4, 5, 6)
# s = pd.Series(h)

# print(type(h)) # tuple
# print(type(s)) # pandas.core.series.Series
# print(s)

# h = ('영남대학교', '2023-01-10', 1004, 3.14)
# s1 = pd.Series(h)
# print(s1) # dtype = object
# print(type(s1[0]))

# # == dict로 Series 만들기 ==
# d = {'name': '홍길동', 'id':21911407, 'grade': 4.5}
# s = pd.Series(d)
# print(type(s))
# print(s)
# print(s['name'])
# print(s[0]) # 기본적으로 인덱스도 가지고 있다.
# print(s[0:2]) # 0~1 인덱스까지
# print(s['name':'id']) # 'name'에서 'id'까지 ('id'를 포함한다는 것에 주의)

# h = ('영남대학교', '2023-01-10', 1004, 4.5)
# s = pd.Series(h, index=['학교', '입학일', '학번', '성적'], name='학생정보')
# print(s)
# print(s[ [True, False, True, False] ]) # Boolean Indexing
# print(s[['학교', '성적']]) # Fancy Indexing


# ===== DataFrame =====
# - def. 2차원 배열: 같은 크기의 리스트를 가진 dict로부터 생성하는 경우가 많다.

# data = {
#     'name'  : ['홍길동', '임꺽정', '박하늘'],
#     'birth' : ['2010-01-04', '1970-12-16', '2023-01-08'],
#     'point' : [90, 80, 75],
#     'rate'  : [1.2, 6.3, 2.3]
# }

# df = pd.DataFrame(data)
# print(type(df)) # pandas.core.frame.DataFrame
# print(df.dtypes) # column 마다 data type을 알려줌
# print(df.info())
# print(df.shape)
# print(df.head(1))
# print(df.tail(1))
# print(df.index) # RangeIndex(start=, stop=, step=)

# print(df.columns)
# df.columns = ['이름', '생일', '점수', '비율'] # column 내용이 바뀜

# print(df.describe()) # 기초 통계자료 출력 (수치형 데이터에 대해서만)
# print(df.T) # 데이터 전치행렬

# == 데이터 정렬 (인덱스 기준, column 값을 기준으로 정렬)

# print(df.sort_index())     # row 오름차순
# print(df.sort_index(       # row 내림차순
#     ascending=False
# ))

# df.sort_index(axis=1)      # col 오름차순
# df.sort_index(             # col 내림차순
#     axis=1,
#     ascending=False
# )

# print(df.sort_values('birth'))
# print(df.sort_values(        # 생일 기준으로 잡고, 값이 같으면 point 기준으로 정렬
#     ['birth', 'point'], ascending=False
# ))


# ===== data 가져오기 =====

# print(df[0]) // err. indexing 안 된다.
# print(df[0:2]) # 슬라이싱은 된다.
# print(df['name']) # 일단 column을 선택해야 한다! -> 하나의 Series로 돌아온다

# s = df['name']
# print(s[0])


# # ===== 새로운 column 추가 =====

# df['주소'] = '미상'
# print(df) # broadcast

# df['주소2'] = ['대구', '부산', '서울']
# print(df)

# df.index = ['one', 'two', 'three'] # index 커스텀
# print(df)
# print(df['one':'two'])

# print(df.set_index('name'))
# print(df.set_index('name', inplace=True)) # output이 없다. 원본이 바뀐다.
# print(df)
# print(df.loc['홍길동']) # 행을 선택


# ===== =====

import os
os.chdir("../AI/COG_ICT/data")


casts = pd.read_csv('cast.csv')

# print(casts['n'].fillna(method='ffill'))

# print(casts[casts['title'].str.contains('mma')])
# print(casts['year'].value_counts().head(10)) # Series에 똑같은 값이 몇 번 나오는가?


import matplotlib.pyplot as plt


# p = casts['year'].value_counts()
# print(p) # Series


# p.plot()
# p.sort_index(inplace=True)
# print(p)

## ==========================

# print(casts.groupby(['year']).n.max())
# print(casts.groupby(['year']).n.min())


# == Aaron Abrams가 출연한 영화 출력 ==
# print(casts)
# d = casts[casts['name'] == "Aaron Abrams"]
# print(d.head())
# print(d.info())

# == d에서 각 연도별 출연한 영화의 수를 구하고, 막대그래프로 그리시오.

# p = d['year'].value_counts() # 방법1
# p = d.groupby(['year']).size() # 방법2

# p.plot()

# == casts에서 각 decade마다 (각 10년마다) 몇 편의 영화가 나왔는지 구해보시오.

# decade = casts['year'] // 10 * 10 # 1의 자리를 날림
# # print(casts.groupby(decade).size())
# casts.groupby(decade).size().plot(kind='bar')
# plt.show()

# == 

# decade = casts['year'] // 10 * 10
# # # print(casts.groupby([decade, 'type']).size())
# # casts.groupby(['type', decade, ]).size().plot(kind='bar')
# # plt.show()

# un_c_dec3 = casts.groupby(['type', decade, ]).size().unstack() # dataFrame
# un_c_dec3.plot(kind='bar')
# # plt.show()
# un_c_dec3.T.plot(kind='bar')
# plt.show()


# == 여러 데이터 다루기

release = pd.read_csv('release_dates.csv')

# c_amelia = casts[casts['title'] == 'Amelia']
# r_amelia = release[release['title'] == 'Amelia']

# # c_amelia.append(r_amelia) # 좋지 않은 방법
# print(c_amelia.merge(r_amelia)) # 일치하는 column을 조사하여 데이터를 Join 시켜준다.


# == Aaron Abrams와 함께 출연한 배우들의 리스트를 구해보시오

c_aaron = casts[casts['name'] == "Aaron Abrams"]
co_star = casts.merge(c_aaron, on = ['title', 'year']) # merge 기준 정하기. 선택된 교집합 영역 제외 나머지 부분을 구분해서 보여준다.
co_star = co_star[co_star['name_x'] != co_star['name_y']] # "Aaron Abrams" 본인 제거
co_star = co_star[['title', 'year', 'name_x']] # Fancy_Indexing
co_star = co_star[co_star['name_x'].duplicated()] # 중복되는 배우명 제거
# 혹은, co_star['name_x'].drop_duplicates()

print(co_star)