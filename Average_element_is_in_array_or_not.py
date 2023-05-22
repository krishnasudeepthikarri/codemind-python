n=int(input())
lst=list(map(int,input().split()))
a=sum(lst)//n
if a in lst:
    print("True")
else:
    print("False")