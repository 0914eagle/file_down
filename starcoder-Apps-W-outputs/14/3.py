
from random import randint
def get_random_string(max_length=10):
    string_length = randint(1, max_length)
    letters = [chr(randint(65, 90)) for _ in range(string_length)]
    return ''.join(letters)

def generate_input_data(n, m):
    n_answers = [get_random_string(max_length=m) for _ in range(n)]
    correct_answers = [get_random_string(max_length=m) for _ in range(m)]
    answer_points = [randint(1, 1000) for _ in range(m)]
    return n_answers, correct_answers, answer_points

n = 1000
m = 1000
n_answers, correct_answers, answer_points = generate_input_data(n, m)

print(n, m)
for ans in n_answers:
    print(ans)
for ans in correct_answers:
    print(ans)
print(' '.join(map(str, answer_points)))
