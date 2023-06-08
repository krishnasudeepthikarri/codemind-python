m=int(input())
n=int(input())
for i in range(m,n+1):
    temp=i
    rev=0
    while temp!=0:
        rem=temp%10
        temp//=10
        rev=rev*10+rem
    if i==rev:
        print(i,end=' ')