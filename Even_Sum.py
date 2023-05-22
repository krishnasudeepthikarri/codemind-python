n=int(input())
lst=list(map(int,input().split()))
t=0
for num in lst:
    if num%2==0:
        t=t+num
print(t)