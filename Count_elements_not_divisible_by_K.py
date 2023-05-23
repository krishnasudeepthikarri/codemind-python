n,k=map(int,input().split())
lst=list(map(int,input().split()))
s=0
for num in lst:
    if num%k!=0:
       s+=1
print(s)