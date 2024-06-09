#prime no. in range
start=int(input("enter the no.\n"))
end=int(input("enter the ending no."))
count=0
for num in range (start,end+1):

  for i in range(2,num):
    if(num%i==0):
      isprime=False
      break
  if (isprime):
    print(num)
    count=count+1
print("no. of prime no.s is=",count)
