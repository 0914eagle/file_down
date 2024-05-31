
def max_problems_in_contests(n, problems):
    topic_counts = {}
    for topic in problems:
        if topic in topic_counts:
            topic_counts[topic] += 1
        else:
            topic_counts[topic] = 1
    
    max_problems = 0
    for topic in topic_counts:
        num_problems = topic_counts[topic]
        cnt = 1
        while num_problems >= cnt:
            max_problems = max(max_problems, cnt)
            cnt *= 2
    
    return max_problems

# Input reading
n = int(input())
problems = list(map(int, input().split()))

# Output
print(max_problems_in_contests(n, problems))
