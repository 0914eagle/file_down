
def light_toggling(input_str):
    n = len(input_str)
    if n == 0:
        return 0
    if n == 1:
        if input_str == '0':
            return 0
        else:
            return 1
    def toggle_next_light(time, curr_index):
        if curr_index < n:
            if input_str[curr_index] == '1':
                time += 1
                time = toggle_next_light(time, curr_index + 1)
            else:
                time = toggle_next_light(time, curr_index + 1)
        return time
    time = 0
    time = toggle_next_light(time, 0)
    return time
input_str = input()
print(light_toggling(input_str))

