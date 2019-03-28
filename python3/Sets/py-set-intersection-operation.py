# Set .intersection() Operation
# https://www.hackerrank.com/challenges/py-set-intersection-operation

def newspaper_intersection(eng, fre):
    return len(eng.intersection(fre))


if __name__ == "__main__":

    english, french = [set(input().split()) for _ in range(4)][1::2]
    print(newspaper_intersection(english, french))
