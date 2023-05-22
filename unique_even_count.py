n=int(input())
lst=list(map(int,input().split()))
c=0
lst2=set(lst)
for num in lst2:
    if num%2==0:
        c+=1
print(c)