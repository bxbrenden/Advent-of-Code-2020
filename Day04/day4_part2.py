from pprint import pprint
import re
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
        iyr = int(iyr)
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


def valid_hgt(hgt):
    '''Validate the height: must be a number followed by "in" or "cm"
       - If "cm", must be between 150 and 193 inclusive
       - If "in", must be between 59 and 76 inclusive'''

    def find_delimiter(hgt):
        '''Find where the integers stop and the characters start.
           Return the index of the first char.'''

        for index, char in enumerate(hgt):
            try:
                num = int(char)
            except ValueError:
                return index

        return None

    if index := find_delimiter(hgt):
        num = int(hgt[:index])
        units = hgt[index:]
        #print(f'Number: {num}, Units: {units}')

        if units == "cm" or units == "in":
            if units == "cm":
                if num >= 150 and num <=193:
                    return True
                else:
                    return False
            elif units == "in":
                if num >= 59 and num <= 76:
                    return True
                else:
                    return False
        else:
            return False
    else:
        return False


def valid_hcl(hcl):
    '''Validate hair color: must begin with "#" followed by 6 chars [0-9a-f]'''
    hcl_regex = r'^#[0-9a-f]{6}'
    hcl_pattern = re.compile(hcl_regex)
    if hcl_pattern.match(hcl):
        return True
    else:
        return False


def valid_ecl(ecl):
    '''Validate the eye color: must be in set of ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']'''
    eye_colors = set(['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'])
    if ecl in eye_colors:
        return True
    else:
        return False


def valid_pid(pid):
    '''Validate the passport ID: must be 9 digits long, all numerals [0-9], and may have leading zeroes'''

    if len(pid) == 9:
        for char in pid:
            try:
                int(char)
            except:
                return False
    else:
        return False

    return True


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
        pass_dict = passport_str_to_dict(passport)
        if has_mandos := has_all_mandatory_keys(pass_dict):
            byr = pass_dict['byr']
            iyr = pass_dict['iyr']
            eyr = pass_dict['eyr']
            hgt = pass_dict['hgt']
            hcl = pass_dict['hcl']
            ecl = pass_dict['ecl']
            pid = pass_dict['pid']

            if valid_byr(byr):
                if valid_iyr(iyr):
                    if valid_eyr(eyr):
                        if valid_hgt(hgt):
                            if valid_hcl(hcl):
                                if valid_ecl(ecl):
                                    if valid_pid(pid):
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
