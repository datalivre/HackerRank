# No Idea!
# https://www.hackerrank.com/challenges/no-idea

def no_idea(n, a, b):
    happy = 0
    for i in n:
        if i in a:
            happy += 1
        elif i in b:
            happy -= 1
    return happy


if __name__ == "__main__":

    input()
    n = input().split()
    a, b = [set(input().split()) for _ in range(2)]

    print(no_idea(n, a, b))

