
from collections import defaultdict

def sort_predictions(n, s, predictions):
    scores = defaultdict(int)
    
    for i in range(s):
        prediction = predictions[i]
        for j in range(len(prediction)):
            for k in range(n - len(prediction) + 1):
                substring = prediction[j:j+len(prediction)]
                for l in range(k, k + len(prediction)):
                    if substring == predictions[i]:
                        scores[predictions[i]] += 1
    
    sorted_predictions = sorted(predictions, key=lambda x: (-scores[x], predictions.index(x)))
    
    return sorted_predictions

# Input parsing
n, s = map(int, input().split())
predictions = [input().strip() for _ in range(s)]

# Sort the predictions
sorted_predictions = sort_predictions(n, s, predictions)

# Output the sorted predictions
for p in sorted_predictions:
    print(p)
