num=int(input("enter the no."))

 sum=0
 sq=num*num
 while(sq):
  r=sq%10
  sum=sum+r
  sq=sq//10
 if(num==sum):
   print("neon")
 else:
   print("not a neon")
