n=int(input())
lst=list(map(int,input().split()))
s=0
for num in lst:
    while num!=0:
        rem=num%10
        num=num//10
        s=s+rem
print(s)
        