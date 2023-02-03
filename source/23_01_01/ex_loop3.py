cnt = 0
for i in range(1, 10): 
    for j in range(1, 10): 
        for k in range(1, 10):
            if i ** 3 + j ** 3 + k ** 3 == i*100 + j*10 + k:
                cnt += 1

cnt2 = 0
for x in range(100, 1000):
    a = x // 100
    b = x // 10 % 10
    c = x // 10
    if a**3 + b**3 + c**3 == x:
        print(x, end=" ")

print(cnt)

