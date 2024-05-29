def shortest_contiguous_substring(s):
    counts = {'1': 0, '2': 0, '3': 0}
    min_length = float('inf')
    start = 0
    distinct_chars = 0
    
    for end, char in enumerate(s):
        if counts[char] == 0:
            distinct_chars += 1
        counts[char] += 1
        
        while distinct_chars == 3:
            min_length = min(min_length, end - start + 1)
            counts[s[start]] -= 1
            if counts[s[start]] == 0:
                distinct_chars -= 1
            start += 1
    
    return min_length if min_length != float('inf') else 0

t = int(input())

for _ in range(t):
    s = input().strip()
    print(shortest_contiguous_substring(s))
