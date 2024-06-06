
def observation(N,M):
    # Observation data
    data = []
    for i in range(N):
        line = input()
        data.append([int(x) for x in line.split()])
    
    # Create a matrix
    matrix = [[0 for i in range(M)] for j in range(M)]
    for i in range(M):
        for j in range(M):
            if i != j:
                matrix[i][j] = 1
            else:
                matrix[i][j] = 0
    
    # Fill the matrix
    for i in range(N):
        for j in range(M):
            # find an observation
            if data[i][j+4] > 0:
                data[i][j+4] -= 1
                for k in range(M):
                    if j != k and data[i][k+4] > 0:
                        data[i][k+4] -= 1
                        matrix[j][k] = 0
    
    # Calculate the answer
    answer = []
    for i in range(M):
        sum_i = 0
        for j in range(M):
            sum_i += matrix[i][j]
        answer.append(sum_i)
    # Return
    return answer

# Read the data
N, M = [int(x) for x in input().split()]
answer = observation(N,M)

# Print the answer
if 0 in answer:
    print(-1)
else:
    print(' '.join(map(str, answer)))
