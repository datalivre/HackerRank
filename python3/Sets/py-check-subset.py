# Check Subset
# https://www.hackerrank.com/challenges/py-check-subset

def check_subset(a, b):
    return a.issubset(b)


if __name__ == "__main__":
    for _ in range(int(input())):
        set_a, set_b = [set(input().split()) for _ in range(4)][1::2]
        print(check_subset(set_a, set_b))
