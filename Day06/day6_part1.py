import sys


def read_input(input_file):
    '''Get the input file into list form and return it'''
    try:
        with open(input_file, 'r') as inp:
            input_str = inp.read()
            input_list = [x for x in input_str.split('\n\n') if x != '']
            return input_list
    except:
        print(f'Failed to read input file: {sys.exc_info()}')
        sys.exit(1)


def entry_to_set(entry):
    '''Given an entry from the list of filled out questionnaires, turn them into a set of unique, lowercase chars and return it'''

    # First check if there are any newlines in the entry string
    if '\n' in entry:
        new_entry = set(''.join([x for x in entry.split('\n')]))
    else:
        new_entry = set(''.join([x for x in entry]))

    print(f'Converted entry {entry} into new entry {new_entry}')
    return new_entry


def sum_list_of_sets(char_sets):
    '''Using a list composed of the outputs of `entry_to_set`, return the sum of the lengths of all sets'''
    return sum([len(cs) for cs in char_sets])


def main():
    input_file = 'input.txt'
    questions = read_input(input_file)

    char_sets = []
    for q in questions:
        char_set = entry_to_set(q)
        char_sets.append(char_set)

    sum_of_set_lengths = sum_list_of_sets(char_sets)
    print(f'ANSWER: the sum of the lengths of all character sets is {sum_of_set_lengths}')



if __name__ == '__main__':
    main()
