n=int(input())
l=[]
n1,n2=0,1
for i in range(2,n+1):
    n3=n1+n2
    n1=n2
    n2=n3
    l.append(n3)
if n in l:
    print("True")
else:
    print("False")