# Any or All
# https://www.hackerrank.com/challenges/any-or-all/problem


lista = [input().split() for _ in range(2)][1]
print(all(int(i) >= 0 for i in lista) and any(i == i[::-1] for i in lista))
