# Merge the Tools!
# https://www.hackerrank.com/challenges/merge-the-tools/problem


from collections import OrderedDict


def merge_the_tools(string, k):
    for x in range(0, len(string), k):
        sliced = string[x:x+k]
        print(''.join(OrderedDict.fromkeys(sliced)))


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
