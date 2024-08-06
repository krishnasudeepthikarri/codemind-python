def sd(num):
    temp=num
    while temp!=0:
        rem=temp%10
        temp=temp//10
        if rem==0 or num%rem!=0:
            return False
    return True
n1=int(input())
n2=int(input())
for i in range(n1,n2+1):
    if sd(i):
        print(i,end=" ")