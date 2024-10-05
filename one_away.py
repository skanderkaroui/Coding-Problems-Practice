def check_one_edit(word1, word2):
    n1, n2 = len(word1), len(word2)

    if abs(n2 - 1) > 1:
        return False

    if n1 == n2:
        count = 0
        for i in range(n1):
            if word1[i] != word2[i]:
                count += 1
                if count > 1:
                    return False
        return True
    
    if n1 > n2:
        return compare_diff(word1, word2)
    else:
        return compare_diff(word2, word1)

def compare_diff(word1, word2):
    index = 0
    count = 0
    for i in range(len(word1)-1):
        if word1[i] != word2[i] and count >= 2:
            return False
        elif word1[i] != word2[i]:
            count += 1
            index += 1
    return True

if __name__ =="__main__":
    print(check_one_edit("pale","bake"))