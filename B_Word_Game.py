def score(n, array1,array2,array3):
    score = [0,0,0]
    for i in range(len(array1)):
        if array1[i] == array2[i] != array3[i]:
            array1[i] +=1
            array2[i] +=1
        if array1[i] == array3[i] != array2[i]:
            array1[i] +=1
            array3[i] +=1
        if array2[i] == array3[i] != array1[i]:
            array1[i] +=1
            array3[i] +=1
            











t = int(input())
for _ in range(t):
    n = int(input())
    array1 = input().split()
    array2 = input().split()
    array3 = input().split()
    array = list(map(int, input().split()))
    
    print(score(n, array1,array2,array3))