
def cut_chessboard(n):
    if n == 1:
        return 2
    elif n == 2:
        return 4
    elif n == 3:
        return 6
    else:
        return 2*n

