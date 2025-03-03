n = int(input())

list = list(map(int, input().split()))
easy = True

for i in range(n):
    if list[i] == 1:
        easy = False
        break

if easy:
    print("EASY")
else:
    print("HARD")