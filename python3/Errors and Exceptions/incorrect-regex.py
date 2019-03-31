# Incorrect Regex
# https://www.hackerrank.com/challenges/incorrect-regex/problem

import re


def re_compile(s):

    try:
        if re.compile(s):
            return True
    except:
        return False


if __name__ == "__main__":
    for _ in range(int(input())):
        string = input()
        print(re_compile(string))
