num=int(input("enter the no."))
 temp=num
 l=len(str(num))
 sum=0
 c=1

 while(num):
  
   r=num%10
   c=r**l
   sum=sum+c
   num=num//10
 if(temp==sum):
     print("the no. is armstrong")
 else:
     print("not armstrong no.")
