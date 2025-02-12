t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    count = 0
    start = True

    for i in range(n):
        if s[i] == "W":
            if start == False:
                continue
            if start == True:
                if i != n:
                    count += 1
                else:
                    continue         
        else:
            if start == False:
                start = True
                count += 1
            else:
                count += 1
    
    print(count)
