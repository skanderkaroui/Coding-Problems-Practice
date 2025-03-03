n = int(input())
p = list(map(int, input()))
a, b, c, d, e = map(int, input())
res = [0] * 5
count = 0
m = 0

for i in range(n):
    m += p[i]

    for j in range(p):
        print("")
