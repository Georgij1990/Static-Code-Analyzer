# write your code here C:\Studying\python_scripts\script1.txt
import Utils
import os

path = Utils.return_argument()
errors = []
line_counter = 0
error_codes = {'S001': 'Too long', 'S002': 'Indentation is not a multiple of four', 'S003': 'Unnecessary semicolon',
               'S004': 'At least two spaces required before inline comments', 'S005': 'TODO found',
               'S006': 'More than two blank lines used before this line'}
error_code = None

isDir = os.path.isdir(path)
if not isDir:
    Utils.check_file(path, line_counter, errors, error_codes)
elif isDir:
    for root, dirs, files in os.walk(path):
        for name in files:
            path_name = os.path.join(root, name)
            Utils.check_file(path_name, line_counter, errors, error_codes)

[print(i) for i in errors]
