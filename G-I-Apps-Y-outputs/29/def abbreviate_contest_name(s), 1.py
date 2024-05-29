
def abbreviate_contest_name(s):
    name_list = s.split()
    contest_name = name_list[1]
    abbreviation = contest_name[0] + 'C'
    print(abbreviation)

abbreviate_contest_name("AtCoder Beginner Contest")
