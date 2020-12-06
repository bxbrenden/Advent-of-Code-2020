from day2_part1 import read_input


def validate_policy(pass_and_policy):
    '''Given a password and policy, return True if the password conforms to the policy, otherwise False'''
    pass_policy_list = pass_and_policy.split(': ')
    policy = pass_policy_list[0]
    passwd = pass_policy_list[1]
    char_index_list = policy.split(' ')
    char_range = char_index_list[0]
    char = char_index_list[1]
    indices = [int(num) for num in char_range.split('-')]
    low_index = indices[0] - 1
    high_index = indices[1] - 1
    vars = ( pass_and_policy,
             passwd,
             char,
             low_index,
             high_index,
    )

    if passwd[low_index] == char and passwd[high_index] != char:
        validity_message(vars, True)
        return True
    elif passwd[low_index] != char and passwd[high_index] == char:
        validity_message(vars, True)
        return True
    else:
        validity_message(vars, False)
        return False


def validity_message(vars, is_valid):
    '''Print a message about the validity based on the value of `is_valid`'''
    # unpack tuples from `vars`
    pass_and_policy, passwd, char, low_index, high_index  = vars

    if is_valid:
        print(f'{pass_and_policy} is a valid password-policy pair.')
    else:
        print(f'{pass_and_policy} is NOT a valid password-policy pair!')

    print(f'    Policy requires that {char} be at either position {low_index + 1} or {high_index + 1}')
    print(f'    Password is: {passwd}')
    print(f'    Character at position {low_index + 1} is {passwd[low_index]}')
    print(f'    Character at position {high_index + 1} is {passwd[high_index]}')


def main():
    input_file = 'input.txt'
    passwords = read_input(input_file)
    validities = []

    for passwd in passwords:
        is_valid = validate_policy(passwd)
        validities.append(is_valid)

    num_valid = len([v for v in validities if v == True])
    print(f'ANSWER: the number of valid passwords is {num_valid}')


if __name__ == '__main__':
    main()
