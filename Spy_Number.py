n=int(input())
s=0
p=1
while n!=0:
    rem=n%10
    n=n//10
    s+=rem
    p=p*rem
if s==p:
    print("Spy Number")
else:
    print("Not Spy Number")