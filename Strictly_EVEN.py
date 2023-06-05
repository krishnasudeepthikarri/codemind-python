n=int(input())
lst=list(map(int,input().split()))
l=[]
a=lst[::2]
for num in a:
    if num%2==0:
        l.append(num)
if len(l)==len(a):
    print("True")
else:
    print("False")