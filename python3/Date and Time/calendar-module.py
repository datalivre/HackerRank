# Calendar Module
# https://www.hackerrank.com/challenges/calendar-module/problem

from calendar import day_name, weekday


def day_week(m, d, y):
    num_week = weekday(y, m, d)
    return day_name[num_week].upper()


if __name__ == "__main__":
    month, day, year = map(int, input().split())
    print(day_week(month, day, year))
