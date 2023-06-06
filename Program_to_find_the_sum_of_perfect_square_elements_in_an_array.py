import math
n=int(input())
lst=list(map(int,input().split()))
l=[]
s=0
for num in lst:
    a=math.sqrt(num)
    #print(num)
    if a.is_integer():
        l.append(num)
        s+=num
print(s)