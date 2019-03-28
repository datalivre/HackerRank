# Set .difference() Operation
# https://www.hackerrank.com/challenges/py-set-difference-operation

def newspaper(b, d):

    english = set([int(i) for i in b.split()])
    french = set([int(i) for i in d.split()])
    return len(english.difference(french))


if __name__ == "__main__":

    a, b, c, d = [input() for _ in range(4)]
    print(newspaper(b, d))

