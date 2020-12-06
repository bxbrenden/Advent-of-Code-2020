from collections import Counter
import sys
import re

def read_input(input_file):
    '''Read the input file and parse into usable chunks'''
    try:
        with open(input_file, 'r') as inp:
            input_str = inp.read()
            input_lines = [line for line in input_str.split('\n') if line != '']
            return input_lines
    except PermissionError:
        print(f'Input file {input_file} found, but permissions do not allow opening.')
        sys.exit(1)
    except FileNotFoundError:
        print(f'Input file {input_file} not found. Please make sure it exists.')
        sys.exit(1)


def validate_password(pass_and_policy):
    '''Given a password and policy, return True if the password conforms to the policy, otherwise False
       Example pass_and_policy value:
           6-8 s: svsssszslpsp'''
    pass_policy_list = pass_and_policy.split(': ')
    policy = pass_policy_list[0]
    passwd = pass_policy_list[1]
    char_range_list = policy.split(' ')
    char_range = char_range_list[0]
    char = char_range_list[1]
    min_max = [int(num) for num in char_range.split('-')]
    min_chars = min_max[0]
    max_chars = min_max[1]
    #print(f'pass_and_policy: {pass_and_policy}')
    #print(f'policy: {policy}')
    #print(f'passwd: {passwd}')
    #print(f'char: {char}')
    #print(f'min_chars: {min_chars}')
    #print(f'max_chars: {max_chars}')
    #print('\n')

    char_count = Counter(passwd)
    count = char_count[char]
    if count <= max_chars and count >= min_chars:
        print(f'{pass_and_policy} is a valid password.')
        print(f'    Policy requires <= {max_chars} instances of {char}.')
        print(f'    Policy requires >= {min_chars} instances of {char}.')
        print(f'    Password has {count} instances of {char}')
        return True
    else:
        print(f'{pass_and_policy} is NOT a valid password!')
        print(f'    Policy requires <= {max_chars} instances of {char}.')
        print(f'    Policy requires >= {min_chars} instances of {char}.')
        print(f'    Password has {count} instances of {char}')
        return False


def main():
    input_file = 'input.txt'
    passwords = read_input(input_file)
    validities = []
    for passwd in passwords:
        is_valid = validate_password(passwd)
        validities.append(is_valid)

    num_valid = len([v for v in validities if v == True])
    print(f'ANSWER: valid number of passwords is {num_valid}')


if __name__ == '__main__':
    main()
