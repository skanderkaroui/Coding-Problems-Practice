t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    count = 0
    start = True

    for i in range(n):

        if s[i] == "W" and start == False:
            continue
        
        if s[i] == "W" and start == True:
            count += 1
        
        if s[i] == "B" and start == False:
            start = True
            count += 1
        
        else:
            count += 1
    
    print(count)
