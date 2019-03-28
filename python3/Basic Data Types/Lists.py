# List
# https://www.hackerrank.com/challenges/python-lists/problem


def list_methods(lista):
    for _ in range(int(input())):
        method, *args = input().split()
        if method != 'print':
            eval(f'lista.{method}{tuple(map(int, args))}')
        else:
            print(lista)


if __name__ == "__main__":
    lista = []
    list_methods(lista)
