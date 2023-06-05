n=int(input())
c1=0
c2=0
rev=0
for i in range(1,n+1):
    if n%i==0:
        c1+=1
if c1==2:
    while n!=0:
        rem=n%10
        n//=10
        rev=rev*10+rem
    for j in range(1,rev+1):
        if rev%j==0:
            c2+=1
if c1==c2==2:
    print("circular prime")
elif c1==2 and c2!=2:
    print("prime but not a circular prime")
else:
    print("not prime")