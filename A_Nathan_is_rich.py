t = int(input())

def wheels_seen():
        n = int(input())
        n_2 = int(n / 2)
        res = []

        for c in range(n):
            b = n_2 - 2 * c
            if b >= 0:
                return b + c
                
for _ in range(t):
    print(wheels_seen())
