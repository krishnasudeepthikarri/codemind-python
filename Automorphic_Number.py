n=int(input())
a=n*n
b=len(str(n))
last_digit=a%pow(10,b)
if last_digit==n:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")