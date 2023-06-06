for i in range(int(input())):
    x,y=map(int,input().split())
    lst1=list(map(int,input().split()))
    lst2=list(map(int,input().split()))
    a=lst1+lst2
    b=sorted(a)
    print(*b)