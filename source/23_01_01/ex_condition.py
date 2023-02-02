# 1
# x, y = map(int, input().split())
# print(x-y if x > y else y-x)

# 2
# now = int(input())

# min = now % 100
# print(f"오후 {now // 100 - 12}:{min}") if now // 100 > 12 else print(f"오전 {now // 100}:{min}")

# 3
year = int(input())

if year % 400 == 0:
    print("윤년입니다.")
elif (year % 4) == 0 and year % 100 != 0:
    print("윤년입니다.")
else:
    print("윤년이 아닙니다.")
