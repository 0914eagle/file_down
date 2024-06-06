

def get_file_content():
    with open('input.txt') as f:
        return f.read()


def print_file_content(data):
    with open('output.txt', 'w') as f:
        f.write(data)


def get_numbers(line):
    return list(map(int, line.strip().split(' ')))


def get_matrix(lines):
    return [get_numbers(line) for line in lines]


def main():
    data = get_file_content()
    lines = data.strip().split('\n')
    n, h, m, k = get_numbers(lines[0])
    matrix = get_matrix(lines[1:])
    result = ''
    if k >= m // 2:
        result = '0 0'
    else:
        pass
    print_file_content(result)


if __name__ == '__main__':
    main()

