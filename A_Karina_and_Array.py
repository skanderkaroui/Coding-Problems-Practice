def multiply(n, array):
    if len(array) < 2:
        return 0
    
    array.sort()

    if array[-1] < 0:
        return array[0] * array[1]
    
    return max(array[-1] * array[-2], array[0] * array[1])

t = int(input())

for _ in range(t):
    n = int(input())
    array = list(map(int, input().split()))
    print(multiply(n, array))
