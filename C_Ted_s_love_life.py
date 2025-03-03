t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())

    for _ in range(m):
        s = input()
        hash = {}
        valid = True

        if n != len(s):
            print("NO")
            continue
        
        char_val = {}
        val_char = {}
        valid = True

        for i in range(n):
            char = s[i]
            val = a[i]

            if char in char_val and char_val[char] != val:
                valid = False
                break
            
            if val in val_char and val_char[val] != char:
                valid = False
                break

            char_val[char] = val
            val_char[val] = char

        print("YES" if valid else "NO")
