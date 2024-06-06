
'''
由于 Bruce 总是从第一位开始找，所以若第 1 位为 '('，在 Bruce 之前的 Barry 一定不会去改变第 1 位，所以我们只要看最后 1 位是 '(' 还是 ')'。
1. 若最后 1 位为 ')'，Barry 可以改最后 1 位，这样就可以让 Bruce 无法完成平衡。
2. 若最后 1 位为 '('，Barry 若想让 Bruce 无法完成平衡，只能在第一位改成 ')'，这样，后面 Bruce 只要把 ')' 转成 '(' 即可。
   注意：若前面已经有 '('，Barry 必须把前面的 ')' 改成 '('，这样才可以让 Bruce 把前面的 ')' 转成 '('，同时，后面的 '(' 也要改成 ')'。
'''
n, k = map(int, input().split())
s = input()
a = [int(input()) for i in range(n)]

if s[-1] == ')':
    print(a[-1])
else:
    ans = 0
    for i in range(n):
        if s[i] == '(':
            ans += a[i]
        else:
            if i + 1 < n and s[i + 1] == ')':
                ans += a[i]
            else:
                ans += a[i]
    if k % 2 == 0:
        print(ans)
    else:
        print(-ans)

