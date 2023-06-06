n=int(input())
arr=list(map(int,input().split()))
lst=set(arr)
if n>2:
    a=sorted(lst)
    print(a[-3])
else:
    print(max(lst))