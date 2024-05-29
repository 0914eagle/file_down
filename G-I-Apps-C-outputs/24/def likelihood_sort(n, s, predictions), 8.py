
def likelihood_sort(n, s, predictions):
    def calc_likelihood(prediction, n):
        count = 0
        for i in range(n - len(prediction) + 1):
            if prediction == rival[i:i+len(prediction)]:
                count += 1
        return count

    rival = ''.join(['R', 'P', 'S'][randint(0, 2)] for _ in range(n))
    predictions.sort(key=lambda x: (-calc_likelihood(x, n), predictions.index(x)))
    return predictions

n, s = map(int, input().split())
predictions = [input().strip() for _ in range(s)]
sorted_predictions = likelihood_sort(n, s, predictions)

for prediction in sorted_predictions:
    print(prediction)
```
