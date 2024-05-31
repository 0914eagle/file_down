
def max_problems_in_contests(n, topics):
    topic_count = {}
    for topic in topics:
        if topic in topic_count:
            topic_count[topic] += 1
        else:
            topic_count[topic] = 1
    
    max_problems = 0
    for count in topic_count.values():
        current_problems = count
        total_problems = count
        while current_problems in topic_count and topic_count[current_problems] >= 2:
            current_problems *= 2
            total_problems += current_problems
        max_problems = max(max_problems, total_problems)
    
    return max_problems

# Read input
n = int(input())
topics = list(map(int, input().split()))

# Call the function and print the result
print(max_problems_in_contests(n, topics))
