n=int(input())
lst=list(map(int,input().split()))
e=0
o=0
for num in lst:
    if num%2==0:
        e+=1
    if num%2!=0:
        o+=1
print(e,o)