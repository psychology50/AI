# # ===== 1 =====

# words = input()
# for x in range(len(words)):
#     print(words[x+1:] + words[:x+1])


# # ===== 2 =====

# ISSN = input("8자리 수를 입력하시오 : ")

# sum = 0
# for i in range(len(ISSN)-1):
#     sum += int(ISSN[i]) * (8-i)
# check = 11 - (sum % 11)

# print("유효한 코드입니다.") if (check == int(ISSN[7])) else print("유효하지 않은 코드입니다.")
    

# # ===== 3 =====

# nbrs = "0123456789"
# hyphen = "-"

# phone = input("전화번호를 입력하시오(010-dddd-dddd) : ").split('-')

# if len(phone) != 3 or not phone[1].isdigit() or not phone[2].isdigit():
#     print("유효하지 않은 번호입니다.")


# # ===== 4 =====

# date = input("날짜를 입력하세요: ").split("/")
# print(date[2] + date[0] + date[1])


# # ===== 5 =====
# import random
# from timeit import default_timer as timer

# A = random.sample(range(1, 1000001), 10000)
# A[-1] = -1
# A[-2] = -2

# target = int(input())

# def f1(target): 
#     for x in range(len(A) - 1):
#         for y in range(x+1, len(A)):
#             if A[x] + A[y] == target:
#                 return x, y, A[x], A[y]
#     return -1, -1, -1, -1

# start = timer()
# print(f1(target)) # 너무 오래 걸린다.
# end = timer()
# print(f"time -> {end - start}")

# def f2(target):
#     for x in range(len(A)-1):
#         search_num = target - A[x]
#         if search_num in A[x+1:]:
#             y = A[x+1:].index(search_num) + x + 1
#             return x, y, A[x], A[y]
#     return -1, -1, -1, -1

# start = timer()
# print(f2(target))
# end = timer()
# print(f"time -> {end - start}")

# def f3(target):
#     D = {value : idx for idx, value in enumerate(A)}
#     for x in range(len(A)-1):
#         search_num = target - A[x]
#         if search_num in D:
#             y = D[search_num]
#             return x, y, A[x], A[y]
#     return -1, -1, -1, -1

# start = timer()
# print(f3(target))
# end = timer()
# print(f"time -> {end - start}")


# ===== 6 =====

import sys
sys.setrecursionlimit(10**8)

n = int(input())
graph = [[0 for _ in range(n)] for _ in range(n)]

def make_graph(y, x, value):
    if value > n:
        return
    graph[y][x] = value

    if 0 <= y-1 < n and 0 <= x-1 < n:
        if graph[y-1][x-1] == 0:
            make_graph(y-1, x-1, value+1)
        else:
            make_graph(y+1, x, value+1)
    elif not 0 <= y-1 < n:
        if graph[y-1][n-1] == 0:
            make_graph(y-1, n-1, value+1)
        else:
            make_graph(y+1, x, value+1)
    elif not 0 <= x-1 < n:
        if graph[n-1][x-1] == 0:
            make_graph(n-1, x-1, value+1)
        else:
            make_graph(y+1, x, value+1)
    else:
        if graph[n-1][n-1] == 0:
            make_graph(n-1, n-1, value+1)
        else:
            make_graph(y+1, x, value+1)
    
make_graph(0, n//2, 1)

for r in range(n):
    print(graph[r])