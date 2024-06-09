def avg(a,b):
  c=a+b
  d=c/2
  return d
m1=int(input())
m2=int(input())
m3=int(input())
a1=avg(m1,m2)
a2=avg(m2,m3)
a3=avg(m3,m1)
m=max(a1,a2,a3)
print(m)
