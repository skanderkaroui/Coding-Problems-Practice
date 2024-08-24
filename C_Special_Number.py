def lucky_number(n):
    if n % 4 == 0 or n % 7 == 0 or n % 47 == 0 or n % 74 == 0 or n % 477 == 0 or n % 774 == 0 or n % 747 == 0 or n % 447 == 0 or n % 774 == 0 or n % 474 == 0 or n % 747 == 0 or n % 774 == 0:
        print("YES")
    else:
        print("NO")

n = int(input())
lucky_number(n)