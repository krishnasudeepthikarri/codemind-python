a=int(input())
b=int(input())
pfs_a=0
for i in range(1,a):
    if a%i==0:
        pfs_a+=i
pfs_b=0
for j in range(1,b):
    if b%j==0:
        pfs_b+=j
if pfs_a==b and pfs_b==a:
    print("Amicable")
else:
    print("Not Amicable")