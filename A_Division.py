t = int(input())

for _ in range(t):
    div = int(input())
    
    if div >= 1900:
        print("Division 1")
    
    elif div <= 1899 and div >= 1600:
        print("Division 2")
    
    elif div <= 1599 and div >= 1400:
        print("Division 3")
    
    else:
        print("Division 4")