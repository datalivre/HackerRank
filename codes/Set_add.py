# Set .add()

def count_name():
    country = set()
    for _ in range(int(input())):
        country.add(input().strip())
    
    return len(country)

if __name__ == "__main__":
    print(count_name())
    
