# Nested Lists
# https://www.hackerrank.com/challenges/nested-list/problem


def students_score(students):
    score = sorted(set(s[1] for s in students))[1]
    for s in students:
        if s[1] == score:
            print(s[0])


if __name__ == '__main__':
    students = sorted([input(), float(input())] for _ in range(int(input())))
    students_score(students)
