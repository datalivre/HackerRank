# Time Delta
# https://www.hackerrank.com/challenges/python-time-delta/problem

from datetime import datetime


def abs_difference(t1, t2):
    t1 = datetime.strptime(t1, '%a %d %b %Y %H:%M:%S %z')
    t2 = datetime.strptime(t2, '%a %d %b %Y %H:%M:%S %z')
    return int(abs((t1-t2).total_seconds()))


if __name__ == "__main__":
    for _ in range(int(input())):
        t1, t2 = [input() for _ in range(2)]
        print(abs_difference(t1, t2))
