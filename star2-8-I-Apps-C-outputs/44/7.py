
import sys

def main():
    height, width = map(int, input().split())
    lines = []
    for i in range(height):
        line = input()
        if len(line) != width:
            print("Invalid input!")
            sys.exit(1)
        lines.append(line)
    
    def process_image(x, y):
        for i in range(y, height):
            for j in range(x, width):
                if lines[i][j] == '+':
                    if i == y or i == height - 1 or j == x or j == width - 1:
                        continue
                    else:
                        return (i - y) * (j - x)
        return 0
    
    min_image_size = width * height
    for i in range(height):
        for j in range(width):
            if lines[i][j] == '+':
                image_size = process_image(j, i)
                if image_size > 0 and image_size < min_image_size:
                    min_image_size = image_size
    
    for i in range(height):
        for j in range(width):
            if lines[i][j] == '+':
                image_size = process_image(j, i)
                if image_size == min_image_size:
                    for m in range(i, height):
                        for n in range(j, width):
                            if lines[m][n] == '+':
                                if m == i or m == height - 1 or n == j or n == width - 1:
                                    continue
                                else:
                                    lines[m] = lines[m][:n] + ' ' + lines[m][n + 1:]
                    for m in range(i, height):
                        if lines[m][j] == '+':
                            lines[m] = lines[m][:j] + ' ' + lines[m][j + 1:]
                    for m in range(i, height):
                        if lines[m][width - 1] == '+':
                            lines[m] = lines[m][:width - 1] + ' '
    
    for line in lines:
        print(line)
    
if __name__ == '__main__':
    main()


