t = int(input())

def adj():
    n = int(input())
    
    if n == 1:
        return [[1]]
    
    elif n == 2:
        return [[-1]]
    
for _ in range(t):
    adj = adj()

    for row in adj:
        print(*row)