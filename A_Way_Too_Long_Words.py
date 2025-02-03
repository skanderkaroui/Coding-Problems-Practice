n = int(input())

for _ in range(n):
    word = input()

    if len(word) <= 10:
        print(word)
    
    else:
        first_letter = word[0]
        last_letter = word[-1]
        long_abrev = len(word[2:])
        print(first_letter+str(long_abrev)+last_letter)