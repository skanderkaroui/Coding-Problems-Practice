password = input()
n = int(input())
words_barked = []

def bark():
    for _ in range(n):
        bark = input()
        words_barked.append(bark)

    if password in words_barked:
        return True

    for word1 in words_barked:
        for word2 in words_barked:
            if password in word1 + word2:
                return True
    return False

print("YES" if bark() else "NO")
