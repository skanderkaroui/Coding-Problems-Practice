def broken(array):
    char_dict = {}
    return_list = []
    for i in range(len(array)):
        if array[i] in char_dict:
            char_dict[array[i]] += 1
        else:
            char_dict[array[i]] = 1
    
    for i in range(len(array)):
        if (char_dict[array[i]] % 2 == 1) and (char_dict[array[i]] > 1):
            return_list.append(array[i])

    return ' '.join(return_list)


t = int(input())
for _ in range(t):
    array = input().strip()
    print(broken(array))
