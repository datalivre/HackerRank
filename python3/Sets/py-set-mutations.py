# Set Mutations
# https://www.hackerrank.com/challenges/py-set-mutations

def set_mutations(m, A, n):

    for i in range(n):
        cmd, args = input().split(" ")
        B = set(map(int, input().split(" ")))
        eval('A.'+cmd+'(B)')

    return sum(A)


if __name__ == "__main__":
    m = int(input())
    A = set(map(int, input().split(" ")))
    n = int(input())
    
    print(set_mutations(m, A, n))

