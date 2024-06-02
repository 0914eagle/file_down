
def total_shower_time(N, T, t_list):
    total_time = 0
    prev_push_time = 0
    for i in range(N):
        if t_list[i] - prev_push_time >= T:
            total_time += T
        else:
            total_time += t_list[i] - prev_push_time
        prev_push_time = t_list[i]
    
    total_time += T  # Add the last T seconds
    return total_time

# Input processing
input_data = input().split()
N = int(input_data[0])
T = int(input_data[1])
t_list = list(map(int, input().split()))

# Call the function and print the result
print(total_shower_time(N, T, t_list))
