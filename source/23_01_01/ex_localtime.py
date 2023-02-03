import time

t = time.localtime()
print(t.tm_year)

num = int(input("주민번호 앞 6자리 : ")[:2])
print(f"당신의 나이는 {100 - num + t.tm_year%100}세 입니다.")