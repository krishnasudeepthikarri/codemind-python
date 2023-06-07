for i in range(int(input())):
    n=int(input())
    rev=0
    temp=n
    while temp!=0:
        rem=temp%10
        temp//=10
        rev=rev*10+rem
    if rev==n:
        print("True")
    else:
        print("False")