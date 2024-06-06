
def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append(input())
    a.sort()
    m = max([len(x) for x in a])
    ans = []
    for i in range(m):
        l = len(set([x[i] for x in a if len(x) > i]))
        if l == 1:
            continue
        for j in range(97, 97 + 26):
            s = chr(j)
            if s not in [x[i] for x in a if len(x) > i]:
                ans.append(s)
                for k in range(n):
                    if len(a[k]) <= i:
                        continue
                    if a[k][i] == s:
                        continue
                    a[k] = a[k][:i] + s + a[k][i+1:]
                break
        else:
            print("Impossible")
            return
    print("".join(ans) + "abcdefghijklmnopqrstuvwxyz")
main()
