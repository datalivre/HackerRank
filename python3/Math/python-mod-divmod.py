# Mod Divmod
# https://www.hackerrank.com/challenges/python-mod-divmod/problem


def div_mod(a, b):
    print(a//b)
    print(a % b)
    return divmod(a, b)


if __name__ == "__main__":

    a, b = [int(input()) for _ in range(2)]
    print(div_mod(a, b))
