
# Pyhton program to print a very beautiful number

# Function to check the number is in the given range or not
def check_number(n, p, x):
    if(len(n) != p):
        return False
    else:
        if(n[1:] == str(int(n[0]) * x)):
            return True
        else:
            return False

# Function to find the minimum number
def find_minimum(p, x):
    min_num = 1
    # Looping till the length of the minimum number
    for i in range(1, p + 1):
        # Calculating the number
        min_num = min_num * 10 + 1
    # Return the minimum number
    return min_num

# Driver Code
if __name__ == "__main__":
    # Taking the user input
    p, x = map(int, input().split())
    # Find the minimum number
    min_num = find_minimum(p, x)
    # Looping till min_num becomes out of range
    while(len(str(min_num)) <= p):
        # Check the number is in the given range or not
        if(check_number(str(min_num), p, x)):
            print(min_num)
            break
        # Increment the minimum number
        min_num = min_num + 1
    else:
        print("Impossible")
