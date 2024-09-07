def string_compression(s):
    n = len(s)
    if n == 0:
        return s
    counter = 1
    res = []
    for i in range(n -1):
        if s[i] == s[i+1]:
            counter += 1
        else:
            res.append(s[i])
            res.append(str(counter))
            counter = 1
    res.append(s[i])
    res.append(str(counter))
    return ''.join(res) if len(res) < n else s
