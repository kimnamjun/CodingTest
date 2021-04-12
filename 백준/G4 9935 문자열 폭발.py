string = input()
e_string = input()

stack = list()
for s in string:
    stack.append(s)

    if len(stack) < len(e_string):
        continue

    explode = True
    for i, e in enumerate(e_string[::-1]):
        if e != stack[-(i+1)]:
            explode = False
            break
    if explode:
        for _ in range(len(e_string)):
            stack.pop()

print(''.join(stack) if stack else 'FRULA')