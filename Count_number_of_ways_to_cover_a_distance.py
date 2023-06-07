n=int(input())
r=0
i=0
a=1
b=1
c=2
if n==0:
    print(i)
elif n<=2:
    print(n)
else:
    for i in range(3,n+1):
        r=a+b+c
        a=b
        b=c
        c=r
print(r)