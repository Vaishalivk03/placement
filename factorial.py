#factorial
num=int(input())
f=1
if num<0:
  print("factorial doesnot exist")
elif num==0:
  print("the factorial is 1")
else:
  for i in range (1,num+1):
    f=f*i
  print("factorial of",num,"is",f)
