
def max_problems_in_contests(n, topics):
    topic_count = {}
    for topic in topics:
        if topic in topic_count:
            topic_count[topic] += 1
        else:
            topic_count[topic] = 1

    max_problems = 0
    for topic in set(topics):
        current_topic = topic
        problems_in_contests = 0
        while current_topic in topic_count and topic_count[current_topic] > 0:
            problems_in_contests += topic_count[current_topic]
            topic_count[current_topic] = 0
            current_topic *= 2
        max_problems = max(max_problems, problems_in_contests)

    return max_problems

# Input parsing
n = int(input())
topics = list(map(int, input().split()))

# Call the function and print the result
print(max_problems_in_contests(n, topics))
