
def max_problems_in_contests(n, topics):
    topic_counts = {}
    for topic in topics:
        if topic not in topic_counts:
            topic_counts[topic] = 1
        else:
            topic_counts[topic] += 1
    
    max_problems = 0
    for count in sorted(topic_counts.values(), reverse=True):
        cur_problems = count
        while cur_problems in topic_counts and topic_counts[cur_problems] > 0:
            topic_counts[cur_problems] -= 1
            cur_problems *= 2
            max_problems = max(max_problems, cur_problems // 2)
    
    return max_problems

# Read input
n = int(input())
topics = list(map(int, input().split()))

# Call the function and print the result
print(max_problems_in_contests(n, topics))
