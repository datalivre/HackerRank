import string

def creator(n, url):
#    name = ''.join(p for p in n if p not in string.punctuation)
#    name = '_'.join(name.split())

    ifname = "if __name__ == '__main__':"
    commets = f"# {n}\n# {url}\n\n\n\n{ifname}"
    name = url.split('/')[-2]
    print(commets, file=open(f'{name}.py', 'w'))
    return n


if __name__=='__main__':

    name = input("Inset name ")
    url = input("Insert URL ")
    
    creator(name, url)

