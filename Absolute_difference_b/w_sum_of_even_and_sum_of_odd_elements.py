n=int(input())
lst=list(map(int,input().split()))
to=0
te=0
for num in lst:
    if num%2==0:
        te+=num
    if num%2!=0:
        to+=num
print(abs(te-to))