def string_compression(word):
    n = len(word)
    res = []
    
    if n < 2:
        return word
    
    res.append(word[0])
    count = 1


    for i in range(n-1):
        if word[i] == word[i+1]:
            count += 1
        else:
            res.append(str(count))
            res.append(word[i+1])
            count = 1
    res.append(str(count))

    return ''.join(res) if len(res) < len(word) else word

if __name__=="__main__":
    print(string_compression('abcdfaa'))
