n, t = list(map(int,input().split()))

min = 10 ** (n - 1)
max = 10 ** n - 1

def divisible():
    for i in range(min, max + 1):
        if i % t == 0:
            return i
    else:
        return -1

# def divisible():
#     while min < max:
#         mid = (max - min) // 2

#         if mid % t == 0:
#             return mid
        
        
    

print(divisible())