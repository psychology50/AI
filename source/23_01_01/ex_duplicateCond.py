a, b, c = map(float, input().split())

if a > b:
    if a > c: 
        print(a)
    else:
        print(c)
else:
    if b > c:
        print(b)
    else:
        print(c)