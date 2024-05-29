def permutation(list):
    b_list = 




    return len(list) == len(set(list))









t = int(input())
for _ in range(t):
    n = int(input())
    array = list(map(int, input().split()))
    
    print(dominated(n, array))