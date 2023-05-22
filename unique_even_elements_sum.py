n=int(input())
lst=list(map(int,input().split()))
s=0
lst2=set(lst)
for num in lst2:
    if num%2==0:
        s=s+num
print(s)