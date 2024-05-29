
def likelihood_sort(n, s, predictions):
    def likelihood(prediction):
        count = 0
        for i in range(n - len(prediction) + 1):
            if prediction == predictions[i:i + len(prediction)]:
                count += 1
        return count
    
    sorted_predictions = sorted(predictions, key=lambda x: likelihood(x), reverse=True)
    return sorted_predictions

# Reading input
n, s = map(int, input().split())
predictions = [input().strip() for _ in range(s)]

# Sorting predictions
sorted_predictions = likelihood_sort(n, s, predictions)

# Output sorted predictions
for pred in sorted_predictions:
    print(pred)
