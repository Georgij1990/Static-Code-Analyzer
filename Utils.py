def check_len(line):
    return len(line) > 79


def check_semicolon(line):
    if line != "":
        str_to_check = line.split('#')[0]
        return str_to_check.strip()[-1] == ';'
