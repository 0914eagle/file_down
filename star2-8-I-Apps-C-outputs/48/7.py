
def tape_art(length, colors):
    tape_art = dict()
    for i in range(length):
        color = colors[i]
        if color not in tape_art:
            tape_art[color] = [i + 1, i + 1]
        else:
            tape_art[color][1] = i + 1

    instructions = list()
    for color, positions in tape_art.items():
        instructions.append(positions + [color])

    return instructions


def main():
    length = int(input())
    colors = list(map(int, input().split()))

    instructions = tape_art(length, colors)
    if len(instructions) == len(set(colors)):
        print(len(instructions))
        for instruction in instructions:
            print(*instruction)
    else:
        print("IMPOSSIBLE")


if __name__ == "__main__":
    main()

