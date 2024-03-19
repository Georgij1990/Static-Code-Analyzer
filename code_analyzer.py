# write your code here C:\Studying\python_scripts\script1.txt
import Utils

path = input()
errors = []
line_counter = 0
error_codes = {'S001': 'Too long', 'S002': 'Indentation is not a multiple of four', 'S003': 'Unnecessary semicolon',
               'S004': 'At least two spaces required before inline comments', 'S005': 'TODO found',
               'S006': 'More than two blank lines used before this line'}
error_code = None

with open(path) as file:
    lines = [line.rstrip('\n') for line in file]
    for i in lines:
        line_counter += 1
        if Utils.check_len(i):
            Utils.add_error(errors, line_counter, 'S001', error_codes['S001'])
        if Utils.check_indentation(i):
            Utils.add_error(errors, line_counter, 'S002', error_codes['S002'])
        if Utils.check_semicolon(i):
            Utils.add_error(errors, line_counter, 'S003', error_codes['S003'])
        if Utils.check_spaces_before_comment(i):
            Utils.add_error(errors, line_counter, 'S004', error_codes['S004'])
        if Utils.find_to_do(i):
            Utils.add_error(errors, line_counter, 'S005', error_codes['S005'])
        if Utils.check_empty_line(i, line_counter):
            Utils.add_error(errors, line_counter, 'S006', error_codes['S006'])

[print(i) for i in errors]
