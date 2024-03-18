# write your code here
path = input()

errors = []

line_counter = 0

with open(path) as file:
    lines = [line.rstrip() for line in file]
    for i in lines:
        line_counter += 1
        if len(i) > 79:
            error = f'Line {line_counter}: S001 Too long'
            errors.append(error)

[print(i) for i in errors]
