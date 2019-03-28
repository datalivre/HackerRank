# Finding the percentage
# https://www.hackerrank.com/challenges/finding-the-percentage/problem

from statistics import mean


def precision_percentage(query, x):
    return f'{mean(student_marks.get(query)):.{x}f}'


if __name__ == '__main__':

    student_marks = {}
    for _ in range(int(input())):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores

    print(precision_percentage(input(), 2))
