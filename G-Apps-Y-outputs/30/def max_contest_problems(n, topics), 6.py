
def max_contest_problems(n, topics):
    topic_count = {}
    for topic in topics:
        topic_count[topic] = topic_count.get(topic, 0) + 1

    max_problems = 0
    for topic, count in topic_count.items():
        num_problems = min(count, 2)
        total_problems = 0
        while num_problems <= count:
            total_problems += num_problems
            num_problems *= 2
        max_problems = max(max_problems, total_problems)

    return max_problems

# Read input
n = int(input())
topics = list(map(int, input().split()))

# Call the function and print the output
print(max_contest_problems(n, topics))
