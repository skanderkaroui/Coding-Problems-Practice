def minimizeStack(n, a):
    from collections import Counter
    
    length_counts = Counter(a)
    
    tallest_tower = max(length_counts.values())
    
    total_towers = len(length_counts)
    
    return f"{tallest_tower} {total_towers}"




n = int(input())
a = list(map(int, input().split()))
print(minimizeStack(n, a))