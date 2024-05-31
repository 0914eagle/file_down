
def max_problems(n, problems):
    topic_count = {}
    for topic in problems:
        if topic in topic_count:
            topic_count[topic] += 1
        else:
            topic_count[topic] = 1
    
    max_problems = 0
    for topic in topic_count:
        count = topic_count[topic]
        curr_problems = count
        total_problems = curr_problems
        while topic * 2 in topic_count and topic_count[topic * 2] > 0:
            curr_problems *= 2
            topic_count[topic * 2] -= 1
            total_problems += curr_problems
        
        max_problems = max(max_problems, total_problems)
    
    return max_problems

# Read input
n = int(input())
problems = list(map(int, input().split()))

# Call the function and print the result
print(max_problems(n, problems))
