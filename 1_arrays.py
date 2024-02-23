c = "aaabdczer"

def is_unique(word):
    char_dict={}
    for char in word:
        val = ord(char)
        if char_dict[val] == True :
            return False
        char_dict[val] = True
    return True

print(is_unique(c))