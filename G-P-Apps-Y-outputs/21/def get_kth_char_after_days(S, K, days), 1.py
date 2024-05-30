
def get_kth_char_after_days(S, K, days):
    for _ in range(days):
        new_S = ''
        for char in S:
            if char == '2':
                new_S += '22'
            elif char == '3':
                new_S += '333'
            elif char == '4':
                new_S += '4444'
            elif char == '5':
                new_S += '55555'
            elif char == '6':
                new_S += '666666'
            elif char == '7':
                new_S += '7777777'
            elif char == '8':
                new_S += '88888888'
            elif char == '9':
                new_S += '999999999'
            else:
                new_S += char
        S = new_S

    return S[K - 1]

S = input().strip()
K = int(input().strip())
result = get_kth_char_after_days(S, K, 5 * 10**15)
print(result)
```
