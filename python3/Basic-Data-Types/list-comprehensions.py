# List Comprehensions
# https://www.hackerrank.com/challenges/list-comprehensions/problem


def comprehensions(x, y, z, n):

    return [[i, j, k] for i in range(x+1) for j in range(y+1)
            for k in range(z+1) if ((i+j+k) != n)]


if __name__ == '__main__':
    x, y, z, n = (int(input()) for i in range(4))
    print(comprehensions(x, y, z, n))
