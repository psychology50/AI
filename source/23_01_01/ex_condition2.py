x, y = map(int, input().split())

r = 5
curr = (x**2 + y**2) ** (1//2)

if (curr < r):
    print("원의 내부")
elif curr == r:
    print("원의 경계")
else:
     print("원의 외부")