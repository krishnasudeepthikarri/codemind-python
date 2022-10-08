num=int(input())
sum=0
while num>9:
    sum=0
    while num:
        remainder=num%10
        num=num//10
        sum=sum+remainder
    num=sum
print(sum)
    