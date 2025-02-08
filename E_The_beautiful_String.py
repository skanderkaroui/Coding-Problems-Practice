t = int(input())

for _ in range(t):
    s = input()
    q = int(input())
    s_list = list(s)

    for _ in range(q):
        i, v = list(map(int,input().split()))

        s_list[i-1] = str(v)

        s = ''.join(s_list)

        if "1100" in s:
            print("YES")
        else:
            print("NO")

