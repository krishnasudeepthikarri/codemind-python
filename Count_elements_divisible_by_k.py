n,k=map(int,input().split())
lst=list(map(int,input().split()))
c=0
for num in lst:
    if num%k==0:
        c+=1
print(c)