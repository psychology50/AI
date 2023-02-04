# # ===== 1 =====

# A = list(range(10, 15))
# for x in enumerate(A):
#     print(x)


# # ===== 2 =====

# words = tuple(input().split())
# print(len(words))
# print(words[2])
# print(sorted(words))


# # ===== 3 =====
# import random

# 매출 = tuple(random.randint(100, 150) for _ in range(30))
# print(매출)

# for t in range(1, len(매출)):
#     if (매출[t-1] > 매출[t]):
#         print(f"{t+1}일")
#     now = 매출[t]

# # //

# cnt = sum([1 if 매출[x] < 매출[x-1] else 0 for x in range(1, len(매출))])
# print(cnt)


# # ===== 4 =====

# import random

# T = tuple(random.sample(range(10), 8))

# l = len(T)
# for i in range(l):
#     print(T[:l-i])


# # ===== 5 =====

# str1 = input()
# str2 = input()
# print(set(str1) & set(str2))


# # ===== 6 ======

# import random

# S = set(random.sample(range(1, 21), 10))
# T = set(random.sample(range(1, 21), 10))

# print(S, "\n", T, sep="")
# print(S&T)
# print(S|T)
# print(S-T)


# # ===== 7 =====

# L = sorted(list(set(map(int, input().split()))))
# print(L)


# ===== 8 =====

import random

A = tuple(random.randint(1, 10) for _ in range(15))
print(A)
S = set(x for x in A if A.count(x) >= 1)
print(S)
