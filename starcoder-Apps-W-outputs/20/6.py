
'''
题目大意：
给定一个长度为l的线段，再给出d，表示每两个鸟之间至少相距d，
同时，两端距离至少为6，求最大可能在线段上安排鸟的数量
'''

'''
思路：
贪心算法，按位置从小到大排序，最左边的位置满足6<=x<=d
每一轮计算能放置的最大数量，根据能放置的最大数量进行剪枝
'''

from typing import List

def max_bird(line_length: int,
             distance: int,
             birds: List[int]) -> int:
    num_birds = 0
    birds.sort()
    left_pos = 6
    for bird in birds:
        if bird >= left_pos:
            num_birds += 1
            left_pos = bird + distance
    # 剩余位置能放的最多的鸟的数量
    rest_num_birds = (line_length - left_pos - distance) // distance
    return num_birds + rest_num_birds

if __name__ == '__main__':
    line_length, distance, num_birds = [int(x) for x in input().split()]
    birds = []
    for _ in range(num_birds):
        birds.append(int(input()))
    print(max_bird(line_length, distance, birds))
