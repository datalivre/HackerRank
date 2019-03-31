# Exceptions
# https://www.hackerrank.com/challenges/exceptions/problem


def integer_division(a, b):
    try:
        return int(a)//int(b)
    except Exception as e:
        return f'Error Code: {e}'


if __name__ == "__main__":
    for _ in range(int(input())):
        a, b = [i for i in input().split()]
        print(integer_division(a, b))
