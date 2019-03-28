# Set .discard(), .remove() & .pop()
# https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem


def set_methods(n):

    for _ in range(int(input())):
        eval('n.{}({})'.format(*input().split()+['']))
    return sum(n)

if __name__ == "__main__":
    
    input()
    n = set(map(int, input().split())) 
    print(set_methods(n))
