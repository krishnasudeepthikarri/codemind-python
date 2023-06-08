n=int(input())
s=0
temp=n
while n:
    i=1
    p=1
    r=n%10
    while i<=r:
        p=p*i
        i=i+1
    s+=p
    n//=10
if s==temp:
    print("The number",temp,"is a strong number")
else:
    print("The number",temp,"is not a strong number")