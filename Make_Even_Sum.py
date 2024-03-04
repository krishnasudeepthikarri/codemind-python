n=int(input())
lst=list(map(int,input().split()))
c=0
for num in lst:
    c+=num
if c%2==0:
    print("1")
else:
    print("0")
