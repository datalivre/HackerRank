# Athlete Sort
# https://www.hackerrank.com/challenges/python-sort-sort/problem

from operator import itemgetter


def sorted_k(arr, k):
    # with itemgetter, examples become simpler and faster.
    for a in sorted(arr, key=itemgetter(k)):  # py2.6>
        print(*a)


if __name__ == '__main__':
    n, m = map(int, input().split())
    array = [[int(i) for i in input().split()] for _ in range(n)]
    k = int(input())
    sorted_k(array, k)

