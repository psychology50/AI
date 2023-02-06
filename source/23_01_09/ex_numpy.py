import numpy as np

# ===== Numpy 배열 (ndarray) =====

# a = np.array([1,2,3,4,5])
# print(type(a)) # <class 'numpy.ndarray'>
# print(a) # [1, 2, 3, 4, 5]

# L = [1, 2, 3.14, 'aaa'] 
# b = np.array(L)
# print(L) # [ 1 ,  2 ,  3.14 , 'aaa']
# print(b) # ['1', '2', '3.14', 'aaa'] 모두 문자로 취급

# # print(dir(b)) # nparray가 가지는 모든 메서드 출력

# print(np.zeros(3)) # [0. 0. 0.]
# print(np.zeros((3,5)))
# print(np.zeros((4, 255, 255, 255))) # 4차원 배열
# print(np.ones((1, 4, 3)))
# print(np.eye(5)) # 단위행렬
# print(np.eye(5, k=-1)) # 1이 채워지는 대각선 줄을 조정할 수 있다.

# print(np.full((3, 5), 1004))
# print(np.full((2, 3), False))
# print(np.empty((10, 20))) # 배열 초기화를 하지 않고 메모리만 할당 -> 데이터 양은 많은데 아직 값을 모르는 경우

# print(np.ones_like(np.empty((10, 20)))) # 인자로 들어온 배열과 똑같은 크기에 1을 채운다
# print(np.zeros_like(np.empty((10, 20))))

# L = np.zeros_like(np.empty((10, 20)))
# print(L.shape) # 행렬크기
# print(L.ndim) # 차원

# list(range(0, 10, 0.5)) # err -> 실수값 때문에 안 된다.
# print(np.arange(0, 10, 0.5)) # 실수값도 가능하다!!


# ===== 등간격으로 데이터 나누기 =====

# a = np.linspace(0, 100)
# print(a) # 0~100 까지 defalt값 50개로 나눈다.
# print(np.linspace(0, 100, 5))
# print(np.logspace(1, 100)) # log값으로 다룬다.

# a = np.ones((2,3), dtype=np.int8) # int 8bit type
# print(np.ones(5).dtype) # dtype = float64

# b = a.astype(np.float64)
# print(a.dtype) # a 자체의 타입이 바뀌지 않는다.
# print(b.dtype) # 새로운 배열로 받아주어야 한다.

# print(a.size)
# print(a.itemsize) # type이 8bit였으므로 하나당 1byte
# print(b.itemsize)


# # ===== Copy. swallow copy & deep copy =====

# list_a = [1,2,3,4,5,6,7,8]
# list_b = list_a
# print(list_a is list_b) # True
# print(list_a == list_b) # True
# print(id(list_a), id(list_b))

# list_c = list_a[1:4]
# print(list_a is list_c) # False
# print(list_a == list_c) # False
# print(id(list_a), id(list_c))

# list_d = list_a[:] # slicing을 이용한 깊은 복사
# print(list_a is list_d) # False
# print(list_a == list_d) # True
# print(id(list_a), id(list_d))

# list_e = list_a.copy() # python method를 이용한 복사(1차원까지만)
# print(list_a is list_e) # False
# print(list_a == list_e) # True
# print(id(list_a), id(list_e))

# list_a = [[10, 20, 30], [1, 2, 3]]
# list_f = list_a.copy()
# print(list_a is list_f) # False
# print(list_a == list_f) # True
# print(id(list_a), id(list_f))
# list_f[0][1] = 50
# print(list_a) # 2차원 포인터가 같은 1차원 리스트의 주소를 가르키고 있기 때문.
# print(list_f) # copy는 내부의 값을 복사해오긴 하는데, 리스트의 id를 복사해서 가져오므로 결과적으로 같은 주소를 가리킨다.

# # 가장 안전한 방법 (깊은 복사)
# import copy

# list_g = copy.deepcopy(list_a)
# print(list_a is list_g) # False
# print(list_a == list_g) # True
# print(id(list_a), id(list_g))
# list_g[0][1] = 20
# print(list_a)
# print(list_g)

# # == Numpy에서 깊은 복사

# a = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

# b = a[ 1:4 ]
# print(b) # view : 대용량 데이터 중에서 일정 부분만 떼어내 작업을 하여 원본을 수정한다. (즉, 원본 데이터와 연결되어 있다.)
# print(b.base) # view의 원본 데이터 확인

# c = a[1:4].copy() # 서로 연관이 없다.
# c[0] = 5
# print(a, c) 

# d = a.view() # id는 다르지만 슬라이싱과 같다.
# print(id(a))
# print(id(d))
# print(d.base) 


# # ===== ndarray에서 값을 가져오는 방법 =====
# a = np.array(range(1, 10))
# print(a.shape)
# b = a.reshape((3,3))

# # Indexing & Slicing
# print(b[0])
# print(b[0][0])
# print(b[0][1:2])

# print(b[0, 0]) # comma로 바로 접근 (numpy만)
# print(b[0, 1:2]) # 슬라이싱도 가능

# # Boolean Indexing
# a = np.array(range(5))
# b = a[ [True, False, False, True, False] ] # 선택할 값만 True로
# print(b)

# a = np.array([10, 3, 7, 5, 9, 1])
# print(a > 5) # 5보다 큰 원소에 대한 Boolean 연산 (vertorizer 연산 / elementwise)
# print(a[a>5])
# print(a[(a > 5) & (a < 10)]) # 논리연산으로 index 가능

# # nbarray 연산

# print(a + 3) # 각각의 원소에 모두 연산 작업
# print(a * 3)


# # ===== Quiz =====

# # 짝수만 2배
# a = np.array(range(10))
# a[ a%2 == 0 ] = a[ a%2==0 ] * 2
# b = a
# print(b)

# a[a<6] = a[a<6] * 3
# print(a)

# a[a<10] = 0 # 10보다 작은 값을 모두 0
# print(a)


## ===== Fancy Indexing =====

# b = np.arange(100).reshape((20, -1)) # 열의 개수 알아서 지정해줘!
# print(b)
# print(b[1, 1]) # 특정 row, col의 값 선택
# print(b[ [2, 5, 8] ]) # 특정 row 값 모두 선택 (Fancy Indexing)
# print(b[ : , [1, 3] ]) # 모든 row의 특정 col 모두 선택
# print(b[ [2,4,8], [0,1,3] ])
# print(b[2:5, 1:4])


# # ===== Vectorized Operation (Elementwise Operation) =====

# a = np.array( [1,2,3,4,5] )
# b = np.array( [6,7,8,9,10] )
# print(a + b) # 행렬합
# print(a * b) # 행렬곱
# print(a / b) # 행렬 나눗셈
# print(a > b)

# # c = np.array( [2,3,4,5] )
# # print(a+c) # 차원 크기가 다르기 때문에. broadcast를 할 수 없다!

# a = np.arange(6).reshape((2, 3))
# b = np.arange(6, 12).reshape((2, 3))

# # print(a @ b) # Matrix dot operation(@) : 행렬곱 -> (n, m) * (a, b)에서 m == a여야 한다.
# print(a @ b.reshape((3, 2)))
# print(b.T) # 전치행렬(.T) : 행 <-> 열


# # ===== Broadcasting =====
# c = np.array([10, 20, 30])
# print(a)
# print(c)
# print(a+c) # 모양이 다른데 연산이 된다. broadcast 되기 때문에. (부족한 차원을 자동으로 다른 값으로 채운다.)
# # 근데 이건 오히려 위험한 거 아닌가??


# # ===== Axis(축) =====

# a = np.arange(6).reshape((2, 3))
# print(a)

# val1 =np.sum(
#     a,
#     axis=0 # 행방향, 행이 증가하는 방향으로
# )
# val2 = np.sum(
#     a,
#     axis=1 # 열방향, 열이 증가하는 방향으로
# )
# print(val1)
# print(val2)

# print(np.max(a, axis=0))


# # ===== Universal Function : ufunc =====
# # def. 벡터화 연산을 지원하는 함수
# # 사용자 정의 함수로 ufunc를 만들 수도 있다.

# a = np.arange(6).reshape((2, 3))
# b = np.arange(6, 12).reshape((2, 3))

# print(type(np.max)) # 함수
# print(type(np.sum)) # 함수
# print(type(np.add)) # numpy.ufunc
# print(np.add(a, b))

# print(np.argmax(a)) # 행렬을 무조건 모두 1차원으로 표현한다
# print(np.all(a)) # 행렬의 모든 값이 참인가? -> 0 때문에 False
# print(np.all(a, axis=0))
# print(np.any(a)) # 행렬에 하나라도 참이 있다면

# print(a.nonzero()) # 0행 1열, 0행 2열, 1행 0열, 1행 1열, 1행 2열에 0이 아닌 값이 존재한다. (행과 열을 구분해서 보여줌)
# print(np.where(a>2, a*2, a*4)) # 참이면 a*2, 거짓이면 a*4 연산을 해준다.
# print(np.where(a>2, 0, a))
# print(np.where(a)) # 인자를 하나만 주면 nonzero()와 비슷한 결과를 돌려준다.


## ===== 난수 생성 =====
## - rand()    : 균등분포 (0~1) 
## - randn()   : 표준 정규분포, 표준편차 1, 평균 0 (대체로 -1~1)
## - randint() : 정수 (low ~ high-1)

# 안녕_클레오_파트라_세상에서_제일_가는_포테이토_칩 = np.random.rand(2,3)
# print(안녕_클레오_파트라_세상에서_제일_가는_포테이토_칩)

# 밥_밥_김밥_밥_밥_김밥_밥_밥_김밥_밥_밥_김밥 = np.random.randn(2,3)
# print(밥_밥_김밥_밥_밥_김밥_밥_밥_김밥_밥_밥_김밥)

# 김칫국_김칫국_김칫국_김칫국 = np.random.randint(10)
# print(김칫국_김칫국_김칫국_김칫국)

# 계란말이_계란말이_계란말이_요우 = np.random.randint(1, 6)
# print(계란말이_계란말이_계란말이_요우)

# 사이_사이_사이다_사이_사이_사이다 = np.random.randint(1, 7, 20)
# print(사이_사이_사이다_사이_사이_사이다)

# print(np.random.randint(11, size=11))

# a = np.random.rand(24)
# print(a.size)
# print(a.resize((2,2), refcheck=False)) # 다른데서 참조하든 말든 resize 시켜버린다. 리턴값 없음 -> 원본이 바뀜
# print(a.size)
# print(a.resize((4,4), refcheck=False))
# print(a.size) # 크게 키우면 0을 채워버린다. reshape은 모양만 바꾸지만, resize는 데이터 개수 자체를 바꿀 수 있다.


# # ===== 파일 입출력 =====

# import os
# os.chdir("../AI/COG_ICT/data")

# a = np.random.randint(1, 46, 100).reshape((10, -1))
# # np.savetxt('rand1to45.csv', a, delimiter=',', fmt="%d") # 저장
# b = np.loadtxt('rand1to45.csv', delimiter=',', dtype=np.int64)
# print(b)
# print(b.dtype)




