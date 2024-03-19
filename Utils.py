import string

empty_lines = []


def add_error(error_codes, line_counter, error_code, error_message):
    error = f'Line {line_counter}: {error_code} {error_message}'
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
