n=int(input())
lst=list(map(int,input().split()))
l=[]
for num in lst:
    if num%2==0:
        l.append(num)
        
if len(l)==len(lst):
    print("True")
else:
    print("False")