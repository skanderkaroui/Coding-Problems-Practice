def teams(n, array):
    array.sort()
    num_prob = 0
    
    for i in range(0, n, 2):
        num_prob += array[i+1] - array[i]
    
    return num_prob

n = int(input())
array = list(map(int, input().split()))
print(teams(n, array))
