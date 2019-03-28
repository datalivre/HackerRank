# Set .union() Operation
# https://www.hackerrank.com/challenges/py-set-union

def union(n, b):
    return len(n.union(b))


if __name__ == "__main__":

    n_english, b_frech = [set(input().split()) for i in range(4)][1::2]
    print(union(n_english, b_frech))
