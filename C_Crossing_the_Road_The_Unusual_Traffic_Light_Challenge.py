def road_crossing(n, c, s):
    # Find the index of the current color (c) in the sequence
    curr_index = s.index(c)
    min_wait = float('inf')
    found_green = False
    for i in range(n):
        # Find the next occurrence of green (g) after the current index
        next_index = (curr_index + i) % n
        if s[next_index] == 'g':
            # Calculate the number of seconds needed to wait until green
            wait_time = (next_index - curr_index) % n
            min_wait = min(min_wait, wait_time)
            found_green = True
            break
    # If green doesn't appear after the current index, wait until the end of the cycle
    if not found_green:
        min_wait = n - curr_index
    return min_wait

# Read the number of test cases
t = int(input())

# Process each test case
for _ in range(t):
    # Read inputs for the current test case
    n, c = input().split()
    n = int(n)
    s = input()

    # Print the result for the current test case
    print(road_crossing(n, c, s))