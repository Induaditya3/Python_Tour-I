N=int(input("N="))
sum=0
if N>0:
  for i in range(N,2*N+1):
    sum+=i
  print(sum)
else:
  for i in range(N,2*N-1,-1):
    sum+=i
  print(sum)