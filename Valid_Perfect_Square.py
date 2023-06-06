import math
for i in range(int(input())):
    n=int(input())
    a=math.sqrt(n)
    if a.is_integer():
        print("True")
    else:
        print("False")