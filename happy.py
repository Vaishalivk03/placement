#happy no.
num=int(input("enter the no."))
while(num!=1 and num!=4):
  sum=0
  while(num):
    r=num%10
    sum=sum+r**2
    num=num//10
  num=sum
if(num==1):
  print("happy")
else:
  print("not happy")
