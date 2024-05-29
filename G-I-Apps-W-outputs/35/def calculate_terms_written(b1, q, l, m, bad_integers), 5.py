
def calculate_terms_written(b1, q, l, m, bad_integers):
    current_term = b1
    terms_written = 0
    infinite = False

    while abs(current_term) <= l:
        if current_term in bad_integers:
            bad_integers.remove(current_term)
        else:
            terms_written += 1

        if q == 0 or terms_written >= 10**6:
            infinite = True
            break

        current_term *= q

    if infinite:
        print("inf")
    else:
        print(terms_written)

# Input parsing
b1, q, l, m = map(int, input().split())
bad_integers = set(map(int, input().split()))

calculate_terms_written(b1, q, l, m, bad_integers)
```
