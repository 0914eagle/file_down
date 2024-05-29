
from collections import defaultdict

def likelihood_sort(n, s, predictions):
    counts = defaultdict(int)

    for i in range(s):
        for j in range(len(predictions[i])):
            for k in range(j+1, len(predictions[i])+1):
                counts[predictions[i][j:k]] += 1

    sorted_predictions = sorted(predictions, key=lambda x: (-counts[x], x))
    return sorted_predictions

# Input parsing
n, s = map(int, input().split())
predictions = [input().strip() for _ in range(s)]

# Call the function and print the output
sorted_predictions = likelihood_sort(n, s, predictions)
for prediction in sorted_predictions:
    print(prediction)
