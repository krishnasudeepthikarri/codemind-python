n=int(input()) #10
n1=0
n2=1
print(n1,n2,end=' ') #0,1
for i in range(2,n): 
    n3=n1+n2  #n3=0+1=1
    n1=n2     #n1=1
    n2=n3     #n2=1
    print(n3,end=' ')