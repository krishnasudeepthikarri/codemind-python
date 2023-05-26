n=int(input())
s=0
p=1
while n!=0:
    rem=n%10
    n//=10
    s+=rem
    p=p*rem
print(p-s)