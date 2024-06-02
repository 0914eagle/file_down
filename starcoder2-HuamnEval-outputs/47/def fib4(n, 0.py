
 def fib4(n: int):
    if n < 2:
        return 0
    if n == 2:
        return 2
    fib = [0, 0, 2]
    for i in range(3, n+1):
        fib.append(fib[i-1] + fib[i-2] + fib[i-3] + fib[i-4])
    return fib[n]
 