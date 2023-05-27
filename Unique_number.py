n=int(input())
l=[]
i=0
while n!=0:
    rem=n%10
    n//=10
    i+=1
    l.append(rem)
    a=set(l)
if len(a)==i:
    print("Unique Number")
else:
    print("Not Unique Number")