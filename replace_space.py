string = "bonjour monsieur winek yekhi   tawa haka"

def replace_space(str):
    str_list = list(str)
    for int, char in enumerate(str_list):
        if str_list[int] == " ":
            str_list[int] = "%20"
    return "".replace(str_list)



print(replace_space(string))