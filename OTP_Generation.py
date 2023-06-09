n=input()
for i in range(len(n)):
    if(int(n[i])%2!=0):
        num=int(n[i])
        print(num*num,end='')