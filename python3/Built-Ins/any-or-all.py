# Any or All
# https://www.hackerrank.com/challenges/any-or-all/problem


n, lista = input(), input().split()
print(all(int(i) >= 0 for i in lista) and any(i == i[::-1] for i in lista))
