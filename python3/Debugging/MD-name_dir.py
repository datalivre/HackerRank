import os


s = 'python3/Debugging'
s_split = s.split('/')[-1]
s_split = ' '.join(s_split.split('-'))
print('*',s_split)
for root, dirs, files in os.walk("."):  
    for filename in files:
        with open(filename) as fobj:
            leitor = fobj.readlines()
        print(f"    - [x] [{leitor[0][2:-1]}]({s}/{filename})")
               

