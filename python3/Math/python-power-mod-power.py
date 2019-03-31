# Power - Mod Power
# https://www.hackerrank.com/challenges/python-power-mod-power/problem


def power(a, b, m):
    print(a ** b)
    print((a ** b) % m)


if __name__ == "__main__":
    a, b, m = [int(input()) for _ in range(3)]
    power(a, b, m)
