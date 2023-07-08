num = int(input())
arr = list(map(int, input().split()))

arr.sort()
sum = 0
result = 0
for i in arr:
    sum = sum + i
    result += sum

print(result)

# 다른 풀이
i 가 len(arr) 까지 도달해야 하므로 range도 (1, len(arr)+1) 로 설정해줘야 한다.

num = int(input())
arr = list(map(int, input().split()))

arr.sort()
result = 0
for i in range(1, len(arr)+1):
    result += sum(arr[0:i])
print(result)
