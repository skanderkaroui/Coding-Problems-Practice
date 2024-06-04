import sys

def defeat(s, n, monsters):
    monsters.sort()

    for x, y in monsters:
        if s > x:
            s += y
        else:
            return "NO"
    return "YES"

lines = sys.stdin.readlines()

s, n = map(int, lines[0].split())

monsters = []
for line in lines[1:]:
    xi, yi = map(int, line.split())
    monsters.append((xi, yi))

print(defeat(s, n, monsters))
