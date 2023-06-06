for i in range(int(input())):
    n=int(input())
    lst=list(map(int,input().split()))
    l=[]
    for i in range(1,n+1):
        l.append(i)
    #print(lst)
    #print(l)
    for num in l:
        if num not in lst:
            print(num)