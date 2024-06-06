

# 1152B_polycarpus

# n tasks
n = int(input())

# initialise all to zero
total_time = 0
max_queue_length = 0

# create a list for the number of messages to send
messages = []

# create a queue
queue = []

for i in range(n):
    # t_i is the time (the second) when the i-th task was received
    # c_i is the number of messages to send
    t_i, c_i = [int(x) for x in input().split()]

    # append the number of messages to send to a list
    messages.append(c_i)

    # calculate total_time
    if t_i < total_time:
        total_time = total_time + c_i
    else:
        total_time = t_i + c_i

    # calculate max_queue_length
    # if queue is empty, maximum length is number of messages to send
    if len(queue) == 0:
        max_queue_length = max_queue_length + c_i
    else:
        max_queue_length = max_queue_length + len(queue) + c_i

    # add messages to the tail of the queue
    queue.append(messages[-1])

    # if time is reached, remove from queue
    if total_time - t_i == 1:
        queue.pop(0)

# print total_time and max_queue_length
print(total_time, max_queue_length)

