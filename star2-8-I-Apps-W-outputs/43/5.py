
import numpy as np
from itertools import product

def main():
    board = np.array([input() for _ in range(8)])
    start_pos = np.argwhere(board == "T")[0]
    goal_pos = np.argwhere(board == "D")[0]
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    instructions = ["R", "L", "F", "X"]
    def is_valid_pos(pos):
        return np.all(np.logical_and(pos >= 0, pos < 8))
    def is_valid_instruction(pos, instruction):
        if instruction == "F":
            return is_valid_pos(pos) and board[tuple(pos)] in {".", "D"}
        elif instruction == "X":
            return is_valid_pos(pos) and board[tuple(pos)] == "I"
        else:
            return True
    def get_next_pos(pos, instruction):
        if instruction == "F":
            return pos + directions[pos[2]]
        elif instruction == "L":
            return pos + [1]
        elif instruction == "R":
            return pos + [-1]
        else:
            return pos
    def is_solved(pos):
        return np.all(pos[:2] == goal_pos)
    def get_all_paths(pos, path):
        if is_solved(pos):
            return [path]
        all_paths = []
        for instruction in instructions:
            next_pos = get_next_pos(pos, instruction)
            if is_valid_instruction(next_pos[:2], instruction):
                all_paths.extend(get_all_paths(next_pos, path + instruction))
        return all_paths
    all_paths = get_all_paths(np.append(start_pos, 0), "")
    min_length = min(len(path) for path in all_paths)
    min_paths = [path for path in all_paths if len(path) == min_length]
    if min_paths:
        print(min_paths[0])
    else:
        print("No solution")


if __name__ == "__main__":
    main()


