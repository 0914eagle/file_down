
def solve(s):
    s = s.strip()
    n = int(s.split("=")[1].strip())
    def is_valid(arr):
        s = 0
        for i in range(len(arr)):
            if i%2 == 0:
                s += arr[i]
            else:
                s -= arr[i]
        return s == n
    
    def generate(arr):
        if len(arr) == 2*len(arr)-1:
            if is_valid(arr):
                return True
            return False
        if len(arr) < 2*len(arr)-1:
            for i in range(1, n+1):
                arr.append(i)
                if generate(arr):
                    return True
                arr.pop()
        return False
    
    arr = []
    if generate(arr):
        res = [str(arr[0])]
        for i in range(1, len(arr)):
            if i % 2 == 1:
                res.append("+")
            else:
                res.append("-")
            res.append(str(arr[i]))
        res.append("=")
        res.append(str(n))
        return "Possible\n" + "".join(res)
    return "Impossible"

s = input()
print(solve(s))

