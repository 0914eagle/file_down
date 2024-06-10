
import sys
input = sys.stdin.readline


def detect_ad(i, j, web_page, H, W):
    stack = [(i, j)]
    while stack:
        row, col = stack.pop()
        for r, c in [(row - 1, col), (row, col + 1), (row + 1, col), (row, col - 1)]:
            if 0 <= r < H and 0 <= c < W and web_page[r][c] == "$+$":
                stack.append((r, c))
                web_page[r][c] = " "


def is_ad(web_page, H, W):
    for i in range(1, H - 1):
        for j in range(1, W - 1):
            if web_page[i][j] == "$+$":
                detect_ad(i, j, web_page, H, W)
                return True
    return False


def main():
    H, W = map(int, input().split())
    web_page = [list(input().strip()) for _ in range(H)]
    while is_ad(web_page, H, W):
        pass
    for line in web_page:
        print("".join(line))


if __name__ == "__main__":
    main()


