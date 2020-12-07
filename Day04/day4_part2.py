from pprint import pprint
import sys


def read_input(input_file):
    '''Read the input for the puzzle'''
    try:
        with open(input_file, 'r') as inp:
            input_str = inp.read()
            input_list = input_str.split('\n\n')
            return input_list
    except FileNotFoundError:
        print(f'Failed to read input file {input_file} because it was not found.')
        sys.exit(1)
    except PermissionError:
        print(f'Found input file {input_file}, but permissions do not allow reading it.')
        sys.exit(1)


def newline_to_space(passport):
    '''Replace each newline in a passport string with a single space'''
    return passport.replace('\n', ' ')


def passport_str_to_dict(passport):
    '''Turn a passport string into a dictionary of key-value pairs.
       Note: run the passport through `newline_to_space` first'''
    key_vals = passport.split()
    passport_dict = {}
    for kv in key_vals:
        spl = kv.split(':')
        k = spl[0].strip()
        v = spl[1].strip()
        passport_dict[k] = v

    return passport_dict


def has_all_mandatory_keys(passport):
    '''Using a passport dict, see if all mandatory keys are present'''
    mando = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])
    keys = passport.keys()

    if mando.intersection(keys) == mando:
        return True
    else:
        return False


def valid_byr(byr):
    '''Validate the birth year: must be 4 digits and between 1920 and 2002 inclusive'''
    try:
        byr = int(byr)
        if len(str(byr)) == 4:
            if byr >= 1920 and byr <= 2002:
                return True
            else:
                return False
        else:
            return False
    except ValueError:
        return False


def valid_iyr(iyr):
    '''Validate the issue year: must be 4 digits and between 2010 and 2020 inclusive'''
    try:
        byr = int(iyr)
        if len(str(iyr)) == 4:
            if iyr >= 2010 and iyr <= 2020:
                return True
            else:
                return False
        else:
            return False
    except ValueError:
        return False


def valid_eyr(eyr):
    '''Validate the expiration year: must be 4 digits and between 2020 and 2030 inclusive'''
    try:
        eyr = int(eyr)
        if len(str(eyr)) == 4:
            if eyr >= 2020 and eyr <= 2030:
                return True
            else:
                return False
        else:
            return False
    except ValueError:
        return False


def validate_passports(passport_list):
    '''Given a list of all the unmodified passport strings (newlines intact), do the following:
       - replace all newlines with spaces
       - convert the passport string to a dict
       - check if all mandatory keys and values are present in each passport
       - ensure that the values for each mandatory key are legal values
       '''
    valid = 0
    for passport in passport_list:
        passport = newline_to_space(passport)
        passport_dict = passport_str_to_dict(passport)
        if is_valid := has_all_mandatory_keys(passport_dict):
            valid += 1

    return valid


def main():
    try:
        test = sys.argv[1]
        if test == 'test':
            input_file = 'test_input.txt'
        else:
            raise IndexError
    except IndexError:
        input_file = 'input.txt'

    passports = read_input(input_file)
    num_passports = len(passports)
    num_valid = validate_passports(passports)
    print(f'ANSWER: there are {num_valid} valid passports out {num_passports} passports total')


if __name__ == '__main__':
    main()
