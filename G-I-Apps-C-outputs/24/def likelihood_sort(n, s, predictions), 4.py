
def likelihood_sort(n, s, predictions):
    def calculate_likelihood(prediction):
        total_options = 3 ** len(prediction)
        return 1 - (2 ** len(prediction) / total_options)

    predictions.sort(key=lambda x: calculate_likelihood(x), reverse=True)
    return predictions

# Input processing
n, s = map(int, input().split())
predictions = []
for _ in range(s):
    predictions.append(input().strip())

# Sort predictions based on likelihood
sorted_predictions = likelihood_sort(n, s, predictions)

# Output sorted predictions
for prediction in sorted_predictions:
    print(prediction)
