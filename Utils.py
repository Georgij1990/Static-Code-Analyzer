import os.path
import string
import argparse
import re

empty_lines = []
def_regex = '^def'
class_regex = "^class"

def return_argument():
    parser = argparse.ArgumentParser()
    parser.add_argument('path')
    arg = parser.parse_args()
    return arg.path


def add_error(error_codes, path_name, line_counter, error_code, error_message):
    error = f'{path_name}: Line {line_counter}: {error_code} {error_message}'
    error_codes.append(error)


def check_len(line):
    return len(line) > 79


def check_indentation(line):
    counter = 0
    for i in line:
        if i.isspace():
            counter += 1
        else:
            break
    return counter % 4 != 0


def check_semicolon(line):
    if line != "" and not line.strip().startswith('#'):
        str_to_check = line.split('#')[0]
        return str_to_check.strip()[-1] == ';'


def check_spaces_before_comment(line):
    strip_line = line.strip()
    if not strip_line.startswith('#') and '#' in strip_line:
        str_before_comment = strip_line.split('#')[0]
        return str_before_comment[-2:] != '  '


def find_to_do(line):
    strip_line = line.strip()
    if strip_line == '':
        return False
    if strip_line.startswith('#'):
        return 'todo' in strip_line.lower()
    if '#' in strip_line:
        return 'todo' in strip_line.split('#')[1].lower()


def check_empty_line(line, line_counter):
    length = len(empty_lines)
    if line != '' and length != 3:
        empty_lines.clear()
        return False
    if length == 0:
        empty_lines.append(line_counter)
        return False
    if length < 3:
        empty_lines.append(line_counter)
        return False
    if length == 3:
        empty_lines.clear()
        return True


def check_construction_name(line):
    strip_line = line.strip()
    if re.match(def_regex, strip_line):
        def_template = r'^def\s{1}(?!\s)'
        if re.match(def_template, strip_line) is None:
            return True
    elif re.match(class_regex, strip_line):
        class_template = r'^class\s{1}(?!\s)'
        if re.match(class_template, strip_line) is None:
            return True
    return False


def check_class_name(line):
    strip_line = line.strip()
    if re.match(class_regex, strip_line):
        camel_case_template = r'^class\s{1,}[A-Z]{1}[a-z]{1,}[A-Z]*[a-z]*'
        if re.match(camel_case_template, strip_line) is None:
            return True
    return False


def check_function_name(line):
    strip_line = line.strip()
    if re.match(def_regex, strip_line):
        capital_letters = r'def\s{1}[a-z0-9_]*[A-Z]{1,}[a-z0-9_]*'
        if re.match(capital_letters, strip_line) is not None:
            return True
    return False


def check_string(line, path_name, errors, line_counter, error_codes):
    if check_len(line):
        add_error(errors, path_name, line_counter, 'S001', error_codes['S001'])
    if check_indentation(line):
        add_error(errors, path_name, line_counter, 'S002', error_codes['S002'])
    if check_semicolon(line):
        add_error(errors, path_name, line_counter, 'S003', error_codes['S003'])
    if check_spaces_before_comment(line):
        add_error(errors, path_name, line_counter, 'S004', error_codes['S004'])
    if find_to_do(line):
        add_error(errors, path_name, line_counter, 'S005', error_codes['S005'])
    if check_empty_line(line, line_counter):
        add_error(errors, path_name, line_counter, 'S006', error_codes['S006'])
    if check_construction_name(line):
        add_error(errors, path_name, line_counter, 'S007', error_codes['S007'])
    if check_class_name(line):
        add_error(errors, path_name, line_counter, 'S008', error_codes['S008'])
    if check_function_name(line):
        add_error(errors, path_name, line_counter, 'S009', error_codes['S009'])


def check_file(path, line_counter, errors, error_codes):
    with open(path) as file:
        lines = [line.rstrip('\n') for line in file]
        for i in lines:
            line_counter += 1
            check_string(i, path, errors, line_counter, error_codes)