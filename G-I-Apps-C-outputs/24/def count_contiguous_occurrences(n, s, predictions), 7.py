
def count_contiguous_occurrences(n, s, predictions):
    def get_probability(prediction):
        count = len(prediction)
        return sum(1 / 3 ** count for _ in range(n - count + 1))

    predictions.sort(key=get_probability, reverse=True)

    return predictions

# Input parsing
n, s = map(int, input().split())
predictions = []
for i in range(s):
    prediction = input().strip()
    predictions.append(prediction)

# Output sorted predictions
sorted_predictions = count_contiguous_occurrences(n, s, predictions)
for prediction in sorted_predictions:
    print(prediction)
