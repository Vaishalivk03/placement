 num=int(input ("enter the no."))
 temp=num
 sum=0
 while(num==0):
   f=1
   i=1
   r=num%10
   while(i<=r):
  
    f=f*i
    i=i+1
    sum=sum+f
    num=num//10 
   if(temp==num):
    print("the no. is strong")
   else:
    print("the no.is not strong")
