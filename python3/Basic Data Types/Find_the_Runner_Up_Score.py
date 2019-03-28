# Find the Runner-Up Score!
# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem


def find_runner(arr, x):
    return sorted(arr)[-x]


if __name__ == "__main__":
    input()
    arr = set([int(i) for i in input().split()])
    print(find_runner(arr, 2))
