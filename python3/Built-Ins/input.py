#!/usr/bin/env python2.7
# Input()
# https://www.hackerrank.com/challenges/input/problem


def compare(x, k):
    return input() == k


if __name__ == "__main__":
    x, k = map(int, raw_input().split())
    print(compare(x, k))
