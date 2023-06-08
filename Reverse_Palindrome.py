def fun(n):
    rev=0
    temp=n
    while n!=0:
        rem=n%10
        n//=10
        rev=rev*10+rem
    r=temp+rev
    t=r
    res=0
    while r>0:
        rem2=r%10
        r//=10
        res=res*10+rem2
    if res==t:
        return res
    else:
        return fun(t)
        
n=int(input())
print(fun(n))