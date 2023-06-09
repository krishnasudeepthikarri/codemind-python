for i in range(int(input())):
    s=input()
    for j in range(len(s)):
        if s[j].isdigit():
            print("Yes")
            break
    else:
        print("No")