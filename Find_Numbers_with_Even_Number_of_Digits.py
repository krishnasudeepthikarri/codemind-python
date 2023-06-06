n=input()
lst=list(map(str,input().split()))
c=0
for num in lst:
    if len(num)%2==0:
        c+=1
print(c)