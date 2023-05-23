n=int(input())
lst=list(map(int,input().split()))
sf=0
ss=0
for i in range(n):
    if i<n//2:
        sf+=lst[i]
    else:
        ss+=lst[i]
print(abs(ss-sf))