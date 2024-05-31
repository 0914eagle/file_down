
def solve_library_inventory(N, M, initial_state, final_state):
    def count_diff_positions(curr, target):
        count = 0
        for i in range(len(curr)):
            if curr[i] != target[i]:
                count += 1
        return count
    
    def find_book_position(shelves, book_num):
        for i in range(N):
            for j in range(M):
                if shelves[i][j] == book_num:
                    return (i, j)
        return None
    
    def move_book(shelves, from_pos, to_pos):
        x1, y1 = from_pos
        x2, y2 = to_pos
        shelves[x2][y2] = shelves[x1][y1]
        shelves[x1][y1] = 0
    
    total_lifting = 0
    for book_num in range(1, N*M + 1):
        start_pos = find_book_position(initial_state, book_num)
        end_pos = find_book_position(final_state, book_num)
        if start_pos != end_pos:
            diff_start = count_diff_positions(initial_state[start_pos[0]], final_state[start_pos[0]])
            diff_end = count_diff_positions(initial_state[end_pos[0]], final_state[end_pos[0]])
            total_lifting += diff_start + diff_end
            move_book(initial_state, start_pos, end_pos)
    return total_lifting

# Read input
N, M = map(int, input().split())
initial_state = [list(map(int, input().split())) for _ in range(N)]
final_state = [list(map(int, input().split())) for _ in range(N)]

# Output result
result = solve_library_inventory(N, M, initial_state, final_state)
print(result)
