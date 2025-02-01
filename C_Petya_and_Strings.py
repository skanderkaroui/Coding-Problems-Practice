word1 = input().lower()
word2 = input().lower()
ans = 0

for i in range(len(word1)):
    if ord(word1[i]) > ord(word2[i]):
        ans = 1
        break

    elif ord(word1[i]) < ord(word2[i]):
        ans = -1
        break

print(ans)
