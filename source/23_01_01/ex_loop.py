n = int(input())

sum = 0
for i in range(1, n+1):
    sum += 1/i
print(sum)

sum2 = 0
for i in range(1, n+1):
    sum2 += 1/(i ** i)
print(sum2)

sum3 = 0
for i in range(1, n+1):
    sum3 += i/(n-i+1)
print(sum3)