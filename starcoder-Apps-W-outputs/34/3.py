
def input_data():
    return [
        {'n': 5, 'data': [
            ['01', '0'],
            ['2', '1'],
            ['2extra', '0'],
            ['3', '1'],
            ['99', '0']
        ]},
        {'n': 2, 'data': [
            ['1', '0'],
            ['2', '1']
        ]},
        {'n': 5, 'data': [
            ['1', '0'],
            ['11', '1'],
            ['111', '0'],
            ['1111', '1'],
            ['11111', '0']
        ]}
    ]


def do_move(line, move_list):
    file_name = line[0]
    move_to = line[1]
    if file_name != move_to:
        move_list.append(line)


def get_move_to(line, move_to_list):
    for move_to in move_to_list:
        if move_to[0] == line[0]:
            return move_to[1]
    return line[0]


def get_move_list(data):
    move_list = []
    move_to_list = []
    for i in range(len(data)):
        line = data[i]
        type_ = line[1]
        file_name = line[0]
        if type_ == '0':
            move_to = get_move_to(line, move_to_list)
            line = (file_name, move_to)
            do_move(line, move_list)
            move_to_list.append(line)
        elif type_ == '1':
            move_to = get_move_to(line, move_to_list)
            line = (file_name, move_to)
            do_move(line, move_list)

    return move_list


def get_ans(n, data):
    move_list = get_move_list(data)
    return len(move_list)


if __name__ == '__main__':
    for data in input_data():
        n = data['n']
        data = data['data']
        ans = get_ans(n, data)
        print ans
