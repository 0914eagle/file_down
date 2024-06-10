
def tape_art(n, c):
    tape_colors = {}
    for i, color in enumerate(c):
        if color not in tape_colors:
            tape_colors[color] = [i + 1, i + 1]
        else:
            tape_colors[color][1] = i + 1
    if len(tape_colors) != n:
        return "IMPOSSIBLE"
    tape_instructions = []
    for color, tape_instruction in tape_colors.items():
        tape_instructions.append([tape_instruction[0], tape_instruction[1], color])
    tape_instructions.sort(key=lambda x: x[2])
    return len(tape_instructions)
    return tape_instructions


def main():
    n = int(input())
    c = list(map(int, input().split()))
    print(tape_art(n, c))


if __name__ == "__main__":
    main()

