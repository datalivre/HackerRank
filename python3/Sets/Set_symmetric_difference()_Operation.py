# Set .symmetric_difference() Operation
# https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation

def newspaper(e, f):

    english = set([int(i) for i in e.split()])
    french = set([int(i) for i in f.split()])
    return len(english.symmetric_difference(french))


if __name__ == "__main__":

    e_list, f_list = [input() for i in range(4)][1::2]
    print(newspaper(e_list, f_list))

