# Capitalize!
# https://www.hackerrank.com/challenges/capitalize/problem

def solve(string):
    
    for s in string.split():
        string = string.replace(s, s.capitalize())
    return string    

if __name__ == '__main__':
    s = input()
    print(solve(s))
    
    

    
