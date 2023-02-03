# # 1
# i = 1 
# grade = 0
# while i <= 10:
#     grade += int(input(f"학생 {i}의 성적 : "))
#     i += 1
# print(grade // 10)


# # 2
# i = 1
# sum = 0

# while True:
#     grade = int(input(f"학생 {i}의 성적 : "))
#     if grade == -1:
#         break
#     sum += grade
#     i += 1
# print(sum // (i-1))


# # 3
# n = int(input())

# result = 0
# while n > 0:
#     result = result * 10 + n % 10
#     n //= 10
# print(result)


# # 4
# import random

# money = 50
# cnt = 0

# for _ in range(100):
#     while 0 < money < 250:
#         luck = random.randint(0, 1)

#         money += 1 if luck else -1

#         if money == 250:
#             cnt += 1

# print(cnt / 100)


# # 5
# n = int(input())

# for i in range(1, n+1, 2):
#     print(" " * ((n-i)//2), "*" * i, sep="")
 

# # 6
# import turtle

# t = turtle.Turtle()
# t.shape("turtle")
# t.speed(0)

# # for i in range(1, 100):
# #     t.fd(5 * i)
# #     t.left(90)

# for i in range(1, 100):
#     for j in range(4):
#         t.fd(5 * i)
#         t.left(90)


# 6.

n = int(input())
max_length = len(str(n*n))

for i in range(n):
    for j in range(n):
        print("{:>{}}".format((i+1)*n + j, max_length), end=" ")
    print()

print()

for i in range(n):
    for j in range(n):
        print("{:>{}}".format((i+1)*n + i + j*5, max_length), end=" ")
    print()