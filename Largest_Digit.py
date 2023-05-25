n=int(input())
l=[]
while n!=0:
    rem=n%10
    n//=10
    l.append(rem)
print(max(l))