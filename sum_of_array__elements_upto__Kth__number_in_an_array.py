n=int(input())
lst=list(map(int,input().split()))
k=int(input())
print(sum(lst[:k:]))