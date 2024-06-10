
def solve(n, p, k, t):
	original_speed = 100
	new_speed = original_speed + p
	original_length = k
	for timestamp in t:
		original_length *= original_speed / new_speed
		new_speed += p
	return original_length


def main():
	n, p, k = list(map(int, input().split()))
	t = list(map(int, input().split()))
	original_length = solve(n, p, k, t)
	print(original_length)


if __name__ == "__main__":
	main()

