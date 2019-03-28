# sWAP cASE
# https://www.hackerrank.com/challenges/swap-case/problem


def swap_case(string):
##    new_string = ''
##    for s in string:
##        if s.isupper():
##            new_string += s.lower()
##        else:
##            new_string += s.upper()
##    return new_string
    return string.swapcase()


if __name__ == '__main__':

    s = input()
    result = swap_case(s)
    print(result)
