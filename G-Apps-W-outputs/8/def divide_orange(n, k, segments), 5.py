
def divide_orange(n, k, segments):
    result = []
    current_segment = 1

    for i in range(k):
        child_segments = []

        for j in range(n):
            child_segments.append(current_segment)
            current_segment += 1

        result.append(child_segments)

    for segment in segments:
        for child_segment in result:
            if segment in child_segment:
                child_segment.remove(segment)
                child_segment.append(segment)

    for child_segment in result:
        print(" ".join(map(str, child_segment)))

# Input
n, k = map(int, input().split())
segments = list(map(int, input().split()))

# Solve and Output
divide_orange(n, k, segments)
