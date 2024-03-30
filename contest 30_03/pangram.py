def pangram(string):
    s = set()
    for char in string:
        if char.isalpha():
            s.add(char.lower())
    if len(s) == 26:
        return "YES"
    else:
        return "NO"

# Example usage:
n = int(input())
input_string = input().strip()
print(pangram(input_string))
