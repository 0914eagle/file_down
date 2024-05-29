
def round_avg_up(a, b):
    average = (a + b) / 2
    return int(average + 0.5)

if __name__ == "__main__":
    a, b = map(int, input().split())
    result = round_avg_up(a, b)
    print(result)
```
