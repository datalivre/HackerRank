# Set .difference() Operation


def newspaper(b, d):

    english = set([int(i) for i in b.split()])
    french = set([int(i) for i in d.split()])
    return len(english.difference(french))


if __name__ == "__main__":
    a = input()
    b = input()
    c = input()
    d = input()
    print(newspaper(b, d))

