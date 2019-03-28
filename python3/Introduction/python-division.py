# Python: Division
# https://www.hackerrank.com/challenges/python-division/problem



def division(a, b):
    
    return f'{a//b}\n{a/b}'


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
    print(division(a, b))