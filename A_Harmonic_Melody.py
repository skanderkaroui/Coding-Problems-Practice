t = int(input())

def is_perfect():
    for i in range(n - 1):
            diff = abs(notes[i + 1] - notes[i])

            if (diff == 7) or (diff == 5):
                continue
            else:
                return "NO"
    return "YES"
        
for _ in range(t):
    n = int(input())
    notes = list(map(int, input().split()))

    print(is_perfect())
