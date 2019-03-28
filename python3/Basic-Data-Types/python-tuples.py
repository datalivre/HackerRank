# Tuples
# https://www.hackerrank.com/challenges/python-tuples/problem


def tuple_to_hash(t):
    return hash(t)


if __name__ == '__main__':
    input()
    tuple_list = tuple(map(int, input().split()))
    print(tuple_to_hash(tuple_list))
