# # 1
# def max_and_sum(*args):
#     return max(args), sum(args)

# value = max_and_sum(1, 4, 5, 54, 5)
# print(value)


# # 2
# def get_peri(radius = 5.0):
#     return 2 * 3.14 * radius

# print(get_peri())
# print(get_peri(float(input())))


# # 3
# def max_data(args):
#     return max(args)

# values = list(map(int, input().split()))
# print(max_data(values))


# # 4
# import random

# OTP = "abcdefghijklmnopqrstuvwxyz0123456789"
# password = ""

# for _ in range(6): password += random.choice(OTP)
# print(password)


# # 5
# n = int(input())

# def reverse(n):
#     result = 0
#     while n > 0:
#         result = result * 10 + n % 10
#         n //= 10
#     return result

# while n <= 2147483647:
#     print(n)
#     rn = reverse(n)
#     if n == rn: break
#     n += rn


# 6
def gcd(a, b):
    while (b > 0): # 유클리드 호제법
        a, b = b, a % b
    print(a)

x, y = map(int, input().split())
gcd(x, y)

# LEGB 규칙
# Local - Enclosing Function Local - Global - Built-in 순서로 변수를 찾는다.
