n=int(input())
a=n*n
s=0
while a!=0:
    rem=a%10
    a//=10
    s+=rem
if s==n:
    print("Neon Number")
else:
    print("Not Neon Number")