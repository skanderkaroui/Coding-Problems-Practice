password = input()
n = int(input())
words_barked = []

def bark():
    for _ in range(n):
        bark = input()
        words_barked.append(bark)

        if n == 1:
            return password in bark + bark

        for word1 in words_barked:
            for word2 in words_barked:
                if password in word1 + word2:
                    return True
        return False

if bark():
    print("YES")
else:
    print("NO")
