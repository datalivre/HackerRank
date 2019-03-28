# Check Subset


def check_subset(a, b):
    return a.issubset(b)


if __name__ == "__main__":
    for _ in range(int(input())):
        input()
        set_a = set(input().split())
        input()
        set_b = set(input().split())

        print(check_subset(set_a, set_b))
