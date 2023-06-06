n=int(input())
l=[]
l1=[]
l2=[]
while n!=0:
    rem=n%10
    n//=10
    l.append(rem)
for num in l:
    if num%2==0:
        l1.append(num)
    else:
        l2.append(num)
if len(l1)==len(l):
    print("Even")
elif len(l2)==len(l):
    print("Odd")
else:
    print("Mixed")