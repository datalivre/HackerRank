# Print Function
# https://www.hackerrank.com/challenges/python-print/problem


def print_n(n):

    for i in range(1, n+1):
        print(i, end='')


if __name__ == '__main__':
    n = int(input())
    print_n(n)
