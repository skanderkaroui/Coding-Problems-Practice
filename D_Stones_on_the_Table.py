n = int(input())
s = input()

def stone_counter(s, n):
    ans = 0
    for i in range(n - 1):
        if s[i] ==  s[i+1]:
            ans += 1
    return ans
        

print(stone_counter(s, n))

