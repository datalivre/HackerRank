# String Split and Join
# https://www.hackerrank.com/challenges/python-string-split-and-join/problem

def split_and_join(line):
    line = '-'.join(line.split())
    return line


if __name__=='__main__':
    line = input()
    print(split_and_join(line))
