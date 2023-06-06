l,r,k=map(int,input().split())
l1=[]
c=0
for i in range(l,r+1):
    l1.append(i)
for num in l1:
    if num%k==0:
        c+=1
print(c)