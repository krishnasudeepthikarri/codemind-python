n=int(input()) #9
a=n*n  #a=81
s=0
while a!=0: 
    rem=a%10 #1
    a//=10
    s+=rem  #
if s==n:
    print("Neon Number")
else:
    print("Not Neon Number")