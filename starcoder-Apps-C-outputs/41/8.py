
#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
if __name__ == "__main__":
    n = int(raw_input())
    time = map(int, raw_input().split())
    time = [0] + time + [0]
    length = len(time)
    dp = [0 for i in range(length)]
    for i in range(length):
        for j in range(i + 1, length):
            if i + j < length:
                dp[i + j] = max(dp[i + j], dp[i] + dp[j] + time[i + j])
    print dp[-1]
