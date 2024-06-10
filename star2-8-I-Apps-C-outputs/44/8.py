
def detect_image(page, h, w):
  img = [[0 for j in range(w)] for i in range(h)]
  for i in range(h):
    for j in range(w):
      if page[i][j] == '+':
        img[i][j] = 1
  return img


def find_image(img, h, w):
  images = []
  for i in range(h):
    for j in range(w):
      if img[i][j] == 1:
        images.append(find_image_helper(img, h, w, i, j))
  return images


def find_image_helper(img, h, w, i, j):
  if not (0 <= i < h and 0 <= j < w) or img[i][j] != 1:
    return 0
  img[i][j] = 0
  return 1 + find_image_helper(img, h, w, i+1, j) + find_image_helper(img, h, w, i-1, j) + find_image_helper(img, h, w, i, j+1) + find_image_helper(img, h, w, i, j-1)


def process_web_page(page, h, w):
  img = detect_image(page, h, w)
  images = find_image(img, h, w)
  for i in range(h):
    for j in range(w):
      if img[i][j] == 1:
        print('+', end='')
      else:
        print(' ', end='')
    print()
  for image in images:
    print(image)


if __name__ == "__main__":
  h, w = map(int, input().split())
  page = []
  for i in range(h):
    page.append(list(input()))
  process_web_page(page, h, w)

