def seldivnum(num):
    tem=num
    while tem:
        d=tem%10
        tem=tem//10
        if d==0 or num%d!=0:
            return False
    return True
n=int(input())
m=int(input())
for i in range(n,m+1):
    if seldivnum(i):
        print(i,end=" ")