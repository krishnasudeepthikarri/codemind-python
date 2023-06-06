n=int(input())
lst=list(map(int,input().split()))
l1=lst[::2]
l2=lst[1::2]
a=sum(l2)-sum(l1)
if a==0:
    print("YES")
else:
    print("NO")