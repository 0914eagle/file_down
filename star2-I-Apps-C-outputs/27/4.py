
def closest_paper(papers, x, y):
    n = len(papers)
    for i in range(n):
        if papers[i] == x:
            x_index = i
        if papers[i] == y:
            y_index = i
    clockwise_distance = (y_index - x_index + n) % n
    counterclockwise_distance = (x_index - y_index + n) % n
    if clockwise_distance < counterclockwise_distance:
        return "clockwise"
    elif clockwise_distance > counterclockwise_distance:
        return "counterclockwise"
    else:
        return "either"

def guessing_circle(papers):
    unique_papers = set(papers)
    possible_x = []
    for x in unique_papers:
        is_possible = True
        for y in unique_papers:
            if x != y:
                answer = closest_paper(papers, x, y)
                if answer == "either":
                    is_possible = False
                    break
        if is_possible:
            possible_x.append(x)
    if len(possible_x) == 0:
        return "none"
    else:
        return " ".join(map(str, sorted(possible_x)))

n = int(input())
papers = list(map(int, input().split()))
print(guessing_circle(papers))

