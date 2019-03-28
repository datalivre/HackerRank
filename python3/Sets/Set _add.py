# Set .add()
# https://www.hackerrank.com/challenges/py-set-add

def count_name(country):
    for _ in range(int(input())):
        country.add(input().strip())
    return len(country)


if __name__ == "__main__":
    country = set()
    print(count_name(country))

