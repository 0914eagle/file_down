
def takahashi_aoki(A, B, C, D):
    if A < C:
        return "Yes"
    if C < A:
        return "No"
    if B < D:
        return "Yes"
    if D < B:
        return "No"
    return "Yes"

