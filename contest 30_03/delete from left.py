

def move(string1, string2):
    list1 = list(string1)
    list2 = list(string2)
    count = 0

    def remove(list1):
        return list1[1:]
    
    while (list1 is not None) and (list2 is not None) and (list1 != list2):
        if len(list1) > len(list2):
            list1 = remove(list1)
            if list1 == list2:
                count +=1
            
        if len(list2) > len(list1):
            list2 = remove(list2)
            if list1 == list2:
                count +=1
    return count

string1 = "test"
string2 = 'west'
print(move(string1, string2))