#9
n=int(input())
for i in range (0,n):
  for j in range (0,n):
    if(j<=i):
      print(j+1,end=" ")
    else:
      print(" ",end=" ")
  print()
