def petya(string):
    word = ""
    word_final = []
    vowels = ["A", "O", "Y", "E", "U", "I"]

    for i in range(len(string)):
        if string[i].upper() not in vowels:
            word = word + string[i]

    for char in list(word):
        word_final.append(".")
        word_final.append(char)

    return "".join(word_final).lower()

# Example usage:
input_string = input().strip()

print(petya(input_string))