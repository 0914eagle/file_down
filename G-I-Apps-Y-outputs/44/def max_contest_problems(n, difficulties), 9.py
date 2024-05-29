
def max_contest_problems(n, difficulties):
    # Initialize a variable to keep track of the maximum number of problems in the contest
    max_problems = 1
    
    # Iterate through the difficulties
    for i in range(n):
        # Initialize a variable to keep track of the current number of problems
        curr_problems = 1
        
        # Check for each difficulty if it can be included in a valid contest
        for j in range(i+1, n):
            if 2*difficulties[i] >= difficulties[j]:
                curr_problems += 1
            else:
                break
        
        # Update the maximum number of problems in the contest
        max_problems = max(max_problems, curr_problems)
    
    return max_problems

# Input reading and function calling
n = int(input())
difficulties = list(map(int, input().split()))
print(max_contest_problems(n, difficulties))
```
