
def sort_predictions(n, s, predictions):
    def compare_prediction(pred):
        total_count = 0
        for i in range(len(pred)):
            if pred[i:] + pred[:i] in rival_moves:
                total_count += 1
        return total_count

    rival_moves = set()
    for i in range(n):
        rival_moves.add("R" * i)
        rival_moves.add("P" * i)
        rival_moves.add("S" * i)

    sorted_predictions = sorted(predictions, key=lambda x: (-compare_prediction(x), predictions.index(x)))
    return sorted_predictions

# Input
n, s = map(int, input().split())
predictions = [input().strip() for _ in range(s)]

# Output
sorted_predictions = sort_predictions(n, s, predictions)
for pred in sorted_predictions:
    print(pred)
