
def max_problems_in_contests(n, topics):
    topic_count = {}
    for topic in topics:
        if topic in topic_count:
            topic_count[topic] += 1
        else:
            topic_count[topic] = 1
    
    max_problems = 0
    for topic, count in topic_count.items():
        problems_in_contest = count
        while topic * 2 in topic_count and topic_count[topic * 2] > 0:
            problems_in_contest += topic_count[topic * 2]
            topic_count[topic * 2] = 0
            topic *= 2
        max_problems = max(max_problems, problems_in_contest)
    
    return max_problems

# Input parsing
n = int(input())
topics = list(map(int, input().split()))

# Call the function and print the result
print(max_problems_in_contests(n, topics))
