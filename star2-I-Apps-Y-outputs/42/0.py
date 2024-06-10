
def symm_diff(m, n):
    m_set = set(m)
    n_set = set(n)
    return sorted(m_set.union(n_set) - m_set.intersection(n_set))

if __name__ == '__main__':
    m = int(input())
    m_list = list(map(int, input().split()))
    n = int(input())
    n_list = list(map(int, input().split()))
    for elem in symm_diff(m_list, n_list):
        print(elem)

