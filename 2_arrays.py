string = "abcd"

def reverse(string):
    str_list = list(string)
    str_list.reverse()
    reverse_string = "".join(str_list)
    return reverse_string

print(reverse(string))