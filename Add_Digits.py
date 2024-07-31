num=int(input())
while num>9:
    s=0
    while num!=0: #1
        rem=num%10 #1
        num=num//10 #0
        s+=rem #s=11
    num=s
print(s)