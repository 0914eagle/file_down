
def get_row(lst, x):
    result = []
    for row_idx, row in enumerate(lst):
        for col_idx, value in enumerate(row):
            if value == x:
                result.append((row_idx, col_idx))
    result.sort(key=lambda tup: (tup[0], -tup[1]))
    return result
