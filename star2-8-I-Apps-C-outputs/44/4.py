
import re

def remove_ads(web_page):
    page_height, page_width = map(int, input().split())

    web_page = [list(input()) for _ in range(page_height)]
    image_borders = [(i, j) for i in range(page_height) for j in range(page_width) if web_page[i][j] == '+']
    image_borders.sort(key=lambda x: x[0] * page_width + x[1])
    image_characters = set()

    while image_borders:
        stack = [image_borders.pop(0)]
        while stack:
            i, j = stack.pop()
            if (i, j) in image_borders:
                image_borders.remove((i, j))
            for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= x < page_height and 0 <= y < page_width and (x, y) not in image_borders and web_page[x][y] != '+':
                    stack.append((x, y))
                    image_characters.add(web_page[x][y])

    for i in range(page_height):
        for j in range(page_width):
            if web_page[i][j] in image_characters:
                web_page[i][j] = ' '

    return ''.join([''.join(row) for row in web_page])

web_page = remove_ads(web_page)
print(web_page)

