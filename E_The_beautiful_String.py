import sys
data = sys.stdin.read().split()
t = int(data[0])
idx = 1
res = []
for _ in range(t):
    s = list(data[idx]); idx += 1
    n = len(s)
    q = int(data[idx]); idx += 1
    occ = [False] * (n - 3) if n >= 4 else []
    cnt = 0
    for j in range(n - 3):
        if s[j] == '1' and s[j+1] == '1' and s[j+2] == '0' and s[j+3] == '0':
            occ[j] = True
            cnt += 1
    for _ in range(q):
        pos = int(data[idx]) - 1
        new_val = data[idx + 1]
        idx += 2
        s[pos] = new_val
        st = max(0, pos - 3)
        ed = min(pos, n - 4)
        for j in range(st, ed + 1):
            valid = s[j] == '1' and s[j+1] == '1' and s[j+2] == '0' and s[j+3] == '0'
            if valid and not occ[j]:
                occ[j] = True
                cnt += 1
            elif not valid and occ[j]:
                occ[j] = False
                cnt -= 1
        res.append("YES" if cnt else "NO")
sys.stdout.write("\n".join(res))
