
def maximum_problems(n, problems):
    topics = {}
    for topic in problems:
        if topic in topics:
            topics[topic] += 1
        else:
            topics[topic] = 1

    max_problems = 0
    for topic, count in topics.items():
        k = 1
        total_problems = count
        while 2*k <= count:
            k *= 2
            total_problems += k

        max_problems = max(max_problems, total_problems)

    return max_problems

# Read input
n = int(input())
problems = list(map(int, input().split()))

# Call the function and output the result
result = maximum_problems(n, problems)
print(result)
