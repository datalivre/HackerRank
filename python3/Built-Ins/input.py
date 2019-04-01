# Input()
# https://www.hackerrank.com/challenges/input/problem

def compare(x, k):
    return input() == k


if __name__ == "__main__":
    # py2
    x, k = map(int, raw_input().split())
    print(compare(x, k))
