# Check Strict Superset
# https://www.hackerrank.com/challenges/py-check-strict-superset

def check_strict_superset(a_set, n):
    is_superset = []
    for _ in range(n):
        n_set = set(map(str, input().split()))
        is_superset.append(a_set.issuperset(n_set))

    return (all(is_superset))


if __name__ == "__main__":
    a_set = set(map(str, input().split()))
    n = int(input()) 
    print(check_strict_superset(a_set, n))
