
from collections import defaultdict

def likelihood_order(n, s, predictions):
    # Count the frequency of each predicted sequence
    prediction_freq = defaultdict(int)
    for prediction in predictions:
        prediction_freq[prediction] += 1

    # Calculate the likelihood of each prediction appearing
    likelihood = {}
    for prediction, freq in prediction_freq.items():
        likelihood[prediction] = freq * (n - len(prediction) + 1)

    # Sort the predictions by likelihood in descending order
    sorted_predictions = sorted(predictions, key=lambda x: likelihood[x], reverse=True)
    
    return sorted_predictions

# Read input
n, s = map(int, input().split())
predictions = [input().strip() for _ in range(s)]

# Get the sorted predictions
sorted_predictions = likelihood_order(n, s, predictions)

# Print the sorted predictions
for prediction in sorted_predictions:
    print(prediction)
