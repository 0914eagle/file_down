
# python3
# -*- coding: utf-8 -*-
# @Author  : lina

def main():
    a = input().strip()
    b = input().strip()

    if len(a) != len(b):
        print('NO')
        return

    cnt = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            cnt += 1
            if cnt > 1:
                print('NO')
                return
    print('YES')


if __name__ == '__main__':
    main()
