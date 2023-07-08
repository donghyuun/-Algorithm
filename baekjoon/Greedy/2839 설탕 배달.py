def solution():
  n = int(input())
  f = n//5
  
  for f in range(f,-1,-1):
    if 5*f + (n-5*f)//3 * 3 == n and (n-5*f)%3 == 0:
      print(f+(n-5*f)//3)
      return 
  print(-1)
solution()
