# # 1
# def recur(n, depth, res):
#     if n == depth+1:
#         print(res)
#         return
#     recur(n, depth+1, res + 1/depth)

# recur(int(input()), 1, 0)


# # 2
# def bcoef(n, k):
#     if k == 0 or k == n:
#         return 1
    
#     return bcoef(n-1, k-1) + bcoef(n-1, k)

# print(bcoef(10, 5))


# # 3

# from timeit import default_timer as timer

# def power(x, n):
#     if (n == 0):
#         return 1
#     return x * power(x, n-1)


# def power2(x, n):
#     if n == 0:
#         return 1
#     if n % 2 == 1:
#         return x * power2(x, (n-1)//2)**2
#     else:
#         return power2(x, n//2)**2

# start = timer()
# print(power(2, 100))
# end = timer()
# print(f"power -> {end-start}")

# start = timer()
# print(power2(2, 100))
# end = timer()
# print(f"power2 -> {end-start}")

# # 주피터에서 %timeit power(1, 100) 을 입력하면 함수 작동 시간을 알려준다.

def recur(n):
    if n == 0:
        return '0'
    if n == 1:
        return '1'
    return str(recur(n//2)) + str(recur(n%2))

n = int(input())
print(recur(n))


