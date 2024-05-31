
def max_problems_in_contests(n, topics):
    max_problems = 0
    topic_count = {}
    
    for topic in topics:
        if topic in topic_count:
            topic_count[topic] += 1
        else:
            topic_count[topic] = 1
    
    for topic in topic_count:
        count = topic_count[topic]
        k = 1
        total_problems = count
        while count * 2 in topic_count and topic_count[count * 2] > 0:
            k *= 2
            total_problems += count * 2
            count *= 2
            topic_count[count] -= 1
        
        max_problems = max(max_problems, total_problems)
    
    return max_problems

# Input
n = int(input())
topics = list(map(int, input().split()))

# Output
print(max_problems_in_contests(n, topics))
