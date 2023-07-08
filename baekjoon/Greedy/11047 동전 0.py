n, price = map(int, input().split())
arr = []
sum = 0
for i in range(0,n):
    arr.insert(0, int(input()))
for m in arr:
    if price // m != 0:
        sum = sum + price // m
        price = price - m*(price//m)
print(sum)
