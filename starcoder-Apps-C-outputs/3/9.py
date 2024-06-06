

import sys

def main():
    # 整数 N を取得する
    N = int(input())

    # 整数配列 a を取得する
    a = list(map(int, sys.stdin.readline().split()))

    # 整数配列 a を昇順にソートする
    a.sort()

    # 変数 sum に合計値を保持する
    sum = 0
    for i in range(N-1):
        sum += a[i+1] - a[i]

    # 結果を出力する
    print(sum)

if __name__ == '__main__':
    main()
