string ="abccddelkjr"

def rem_dup(string):
    set_string = set(string)
    rm_string = "".join(set_string)
    return rm_string

print(rem_dup(string))
