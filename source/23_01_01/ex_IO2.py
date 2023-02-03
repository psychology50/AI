num = int(input("네 자리 정수를 입력하세요: "))

n4 = num // 1000
n3 = (num % 1000) // 100
n2 = (num % 100) // 10
n1 = num % 10

print(n4 + n3 + n2 + n1)