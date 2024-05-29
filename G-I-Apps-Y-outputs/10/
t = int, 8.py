
t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    s = input().strip()
    p = list(map(int, input().split()))
    
    # Initialize a dictionary to store the count of each button press
    button_press_count = {chr(ord('a') + i): 0 for i in range(26)}
    
    # Calculate the cumulative count of correct button presses at each position
    correct_button_presses = [0] * (n + 1)
    for i in range(m):
        correct_button_presses[p[i]] += 1
    for i in range(1, n + 1):
        correct_button_presses[i] += correct_button_presses[i - 1]
    
    # Calculate the total count of each button press
    for i in range(n):
        button_press_count[s[i]] += 1 + correct_button_presses[i + 1]
    
    # Print the output for each test case
    print(" ".join(str(button_press_count[chr(ord('a') + i)]) for i in range(26)))
```
