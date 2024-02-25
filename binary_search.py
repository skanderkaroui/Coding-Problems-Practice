list = [0,1,2,3,4,6,9,11,15]
num = 11

def binary_search(list, num):
    len = 0
    r = len(list) - 1

    while len <= r:
        m = (l+r)

        if a > list[m]:
            l = m + 1
        elif a < list[m]:
            r = m - 1
        else:
            return True
    
    return False

print(binary_search(list, num))