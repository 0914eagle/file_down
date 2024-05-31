
def max_problems_in_contests(n, topics):
    topic_count = {}
    for topic in topics:
        if topic in topic_count:
            topic_count[topic] += 1
        else:
            topic_count[topic] = 1
    
    max_problems = 0
    for topic in topic_count.keys():
        k = 1
        total_problems = topic_count[topic]
        while topic * (2**k) in topic_count:
            total_problems += topic_count[topic * (2**k)]
            k += 1
        max_problems = max(max_problems, total_problems)
    
    return max_problems

# Input processing
n = int(input())
topics = list(map(int, input().split()))

# Call the function and print the result
print(max_problems_in_contests(n, topics))
