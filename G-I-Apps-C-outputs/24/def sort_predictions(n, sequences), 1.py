
def sort_predictions(n, sequences):
    def get_likelihood(seq):
        count = 0
        for i in range(len(seq), n):
            count += 3**len(seq)
        return count

    predictions = sorted(sequences, key=lambda x: get_likelihood(x), reverse=True)
    return predictions

# Read input
n, s = map(int, input().split())
sequences = [input().strip() for _ in range(s)]

# Sort predictions
sorted_predictions = sort_predictions(n, sequences)

# Output sorted predictions
for pred in sorted_predictions:
    print(pred)
    
# Example usage
# n = 3
# s = 4
# sequences = ['PP', 'RR', 'PS', 'SS']
# sorted_predictions = sort_predictions(n, sequences)
# for pred in sorted_predictions:
#     print(pred)
```
