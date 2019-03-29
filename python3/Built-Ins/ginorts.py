# ginortS
# https://www.hackerrank.com/challenges/ginorts/problem

# ginortS
# https://www.hackerrank.com/challenges/ginorts/problem


def ginorts(s):
    lista = """abcdefghijklmnopqrstuvwxyz
    ABCDEFGHIJKLMNOPQRSTUVWXYZ
    1357902468"""
    print(*sorted(s, key=lista.index), sep="")


if __name__ == "__main__":
    string = input()
    ginorts(string)
