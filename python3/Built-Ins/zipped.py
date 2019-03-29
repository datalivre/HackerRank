# Zipped!
# https://www.hackerrank.com/challenges/zipped/problem


def zip_sum(n, x):

    l_list = []
    l_list = [map(float, input().split()) for _ in range(x)]
    for i in zip(*l_list):
        print(round(sum(i)/len(i),1))


if __name__ == "__main__":
    n, x = [int(i) for i in input().split()]
    zip_sum(n, x)
