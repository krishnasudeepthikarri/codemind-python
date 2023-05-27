n=int(input()) #121
rev=0
temp=n
while n!=0:
    rem=n%10
    n//=10
    rev=rev*10+rem #121
if temp==rev:  #121==121
    print("True")
else:
    print("False")