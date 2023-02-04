# ===== 1 =====

# import random

# A = random.sample(range(1, 20), 8)
# print(A)


# # ===== 2 =====

# import random

# A = random.sample(range(1, 50), 10)
# A.remove(max(A))
# A.remove(min(A))
# print(A)
# print(sum(A) // len(A))


# # ===== 3 =====

# numbers = list(range(1, 11))

# print(numbers[::-2])
# numbers[1:] = []
# print(numbers)


# # ===== 4 =====

# grades = [int(input()) for _ in range(5)]

# print(grades)
# print(sorted(grades))
# print(max(grades))
# print(min(grades))
# print(sum(grades), sum(grades)/len(grades))

# cnt = 0
# for g in grades:
#     if (g >= 90):
#         cnt += 1
# print(cnt)


# # ===== 5 =====

# reg = ["우유", "사과", "우유", "사과"]
# while(True):
#     event = input()

#     if (event == '+'):
#         reg.append("사과")
#     elif (event == '-'):
#         if "우유" in reg:
#             reg.remove("우유")
#         else:
#             print("우유가 없습니다.")
#     if (event == 'x' or event == 'X'):
#         break

#     print(reg)


# # ===== 6 =====

# import random

# lotto = []
# while len(lotto) < 6:
#     num = random.randint(1, 45)
#     if num not in lotto:
#         lotto.append(num)


# user = [int(input("로또 번호를 적으세요 : ")) for _ in range(6)]

# cnt = len(set(lotto) & set(user))

# print(sorted(lotto))
# print(f"{7-cnt}등 입니다~")


# # ===== 7 =====

# nbrs = list(x for x in range(100) if x % 2 == 0 and x % 3 == 0)
# print(nbrs)


# # ===== 8 =====

# l1 = [x for x in range(10, 51, 10)]
# l2 = [sum(l1[:x+1]) for x in range(len(l1))]
# print(l2)

# # ===== 9 =====
# a = [(x,y,z) for x in range(1,31) for y in range(x+1, 31) for z in range(y+1, 31) if x**2 + y**2 == z**2]
# print(a)


# # ===== 10 =====

# def recur(L):
#     if L == []:
#         return L
#     elif isinstance(L[0], list):
#         return recur(L[0]) + recur(L[1:])
#     else:
#         return [L[0]] + recur(L[1:])

# A = recur([1, 2 ,[3, 4, [5, 6], [7, [8, 9]], 10], 11])
# print(A)  


# # ===== 11 =====

# import random

# def make_matrix(row, col):
#     L = list(list(random.randint(1, 10) for _ in range(col)) for _ in range(row))
#     return L 

# def print_matrix(L):
#     for row in range(len(L)):
#         for col in range(len(L[0])):
#             print(f"{L[row][col]:3d}", end=" ")
#         print()

# def add_matrix(A, B):
#     row = len(A)
#     col = len(A[0])
#     L = [[A[r][c] + B[r][c] for c in range(col)] for r in range(row)]
#     return L

# L = make_matrix(5, 5)

# print("L = ")
# print_matrix(L)

# print()
# print_matrix(add_matrix(make_matrix(4, 4), make_matrix(4, 4)))






