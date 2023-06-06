n=int(input())
lst=list(map(int,input().split()))
a=n//2
b=lst[:a]
c=lst[a:]
d=c[::-1]
print(*d,*b)