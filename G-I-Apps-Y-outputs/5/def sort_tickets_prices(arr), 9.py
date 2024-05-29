
def sort_tickets_prices(arr):
    arr.sort()
    return arr

if __name__ == "__main__":
    input_arr = list(map(int, input().split()))
    n = input_arr[0]
    arr = input_arr[1:]
    
    sorted_arr = sort_tickets_prices(arr)
    print(*sorted_arr)
