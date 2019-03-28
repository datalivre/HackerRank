# Set .symmetric_difference() Operation


def newspaper(b, d):

    english = set([int(i) for i in b.split()])
    french = set([int(i) for i in d.split()])

    return len(english.symmetric_difference(french))


if __name__ == "__main__":

    e = input()
    e_list = input()
    f = input()
    f_list = input()
    print(newspaper(e_list, f_list))

