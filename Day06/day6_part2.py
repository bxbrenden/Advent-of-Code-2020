from day6_part1 import read_input, sum_list_of_sets
import sys


def entry_to_set_all(entry):
    '''Given an entry from the list of questionnaire responses, return a set of unique chars that appeared in ALL instances of the entry'''
    # See if multiple entries exist by looking for a newline
    if '\n' in entry:
        # if multiple entries, each one needs to be a set
        entries = [set(x) for x in entry.split('\n') if x != '']
        yes_all = set.intersection(*entries)
    else:
        yes_all = set(entry)

    return yes_all


def main():
    input_file = 'input.txt'
    questions = read_input(input_file)

    yes_all = []
    for q in questions:
        yall = entry_to_set_all(q)
        yes_all.append(yall)

    answer = sum_list_of_sets(yes_all)
    print(f'ANSWER: the sum of the lengths of all sets is {answer}')


if __name__ == '__main__':
    main()
