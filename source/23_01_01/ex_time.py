import time

# 1970년 1월 1일 00시 00분 00초 기준 [s]
print(time.time())

t = int(time.time()) + 9 * 3600
now = t % (24 * 3600)

hr = now // 3600
min = (now % 3600) // 60
sec = int((now % 3600) % 60)
print(f"{hr}시 {min}분 {sec}초")