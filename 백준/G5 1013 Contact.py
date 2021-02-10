import re
pattern = re.compile('^(100+1+|01)+$')
for _ in range(int(input())):
    string = input()
    if re.match(pattern, string):
        print('YES')
    else:
        print('NO')