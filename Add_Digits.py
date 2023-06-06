def add(n):
    s=0
    while n!=0:
        rem=n%10
        n//=10
        s+=rem
    if s<=9:
        return s
    else:
        return add(s)
n=int(input())
print(add(n))