
def likelihood_sort(n, s, predictions):
    def frequency_prediction(pred):
        count = 0
        for i in range(len(pred)):
            count += n - len(pred) + 1
        return count

    predictions.sort(key=lambda x: (-frequency_prediction(x), predictions.index(x)))

    return predictions

# Input processing
n, s = map(int, input().split())
predictions = [input().strip() for _ in range(s)]

# Sort predictions
sorted_predictions = likelihood_sort(n, s, predictions)

# Output sorted predictions
for pred in sorted_predictions:
    print(pred)
