# Integers Come In All Sizes
# https://www.hackerrank.com/challenges/python-integers-come-in-all-sizes/problem


def super_size(a, b, c, d):
    
    return f'{(a ** b) + (c ** d)}'


if __name__ == "__main__":
    a, b, c, d = [int(input()) for _ in range(4)]
    print(super_size(a, b, c, d))
