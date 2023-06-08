def sd(num):
    temp=num
    while temp!=0:
        rem=temp%10
        temp//=10
        if rem==0 or num%rem!=0:
            return False
    return True
m=int(input())
n=int(input())
for i in range(m,n+1):
    if sd(i):
        print(i,end=" ")