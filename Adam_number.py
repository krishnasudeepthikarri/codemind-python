n=int(input()) #12
a=n*n  #144
rev=0
rev3=0
while n!=0:
    rem=n%10
    n//=10
    rev=rev*10+rem #21
    rev2=rev*rev #441
while rev2!=0:
    rem2=rev2%10
    rev2//=10
    rev3=rev3*10+rem2
if a==rev3:
    print("True")
else:
    print("False")