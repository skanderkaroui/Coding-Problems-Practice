def dominated(n, array):
    max_dict = {}
    for i in range(n):
        if array[i] in max_dict:
            max_dict[array[i]] += 1
        else:
            max_dict[array[i]] = 1
    
    if len(max_dict) == 1:
        return -1

    max_occurrences = max(max_dict.values())
    count = 0
    for val in max_dict.values():
        if val == max_occurrences:
            count += 1

    if count >= 2:
        return 1
    return max_occurrences


t = int(input())

for _ in range(t):
    n = int(input())
    array = list(map(int, input().split()))
    
    print(dominated(n, array))
