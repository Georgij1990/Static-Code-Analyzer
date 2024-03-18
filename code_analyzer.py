# write your code here C:\Studying\python_scripts\script.txt
import Utils

path = input()

errors = []

line_counter = 0

error_codes = {'S001': 'Too long', 'S003': 'Unnecessary semicolon'}
error_code = None

with open(path) as file:
    lines = [line.rstrip() for line in file]
    for i in lines:
        line_counter += 1
        if Utils.check_len(i):
            error_code = 'S001'
            error = f'Line {line_counter}: {error_code} {error_codes[error_code]}'
            errors.append(error)
        if Utils.check_semicolon(i):
            error_code = 'S003'
            error = f'Line {line_counter}: {error_code} {error_codes[error_code]}'
            errors.append(error)

[print(i) for i in errors]
