import sys


def read_input(input_file):
    '''Read the input file and return it in digestible chunks'''
    try:
        with open(input_file, 'r') as inp:
            input_str = inp.read()
            input_list = input_str.split('\n')
            return input_list
    except:
        print(f'Failed to read specified input file {input_file} with exception {sys.exc_info()}')
        sys.exit(1)


def find_base_bags(rule_list):
    base_bags = []
    for rule in rule_list:
        if 'contain no other bags' in rule.lower():
            color = rule.split(' ')[:2]
            color_str = ' '.join(color)
            print(f'The {color_str} bag is a base bag')
            base_bags.append(color)

    return base_bags


def main():
    input_file = 'test_input.txt'
    bag_rules = read_input(input_file)

    for rule in bag_rules:
        print(rule)

    # Find all base cases, i.e. all bags that contain no other bags
    # Find the parent bags for the base cases, i.e. the bags that contain the base case bags
    # Repeat step 2 until you have reached the outermost of all bags
    # For each lineage discovered above, create a list of bag colors where index 0 is the outermost and index -1 is the innermost (base)
    # Identify the bags whose index in each list of colors is less than the index of "shiny gold" and whose lineage contains "shiny gold"
    # Return / print the count of bags identified in the previous step

    base_bags = find_base_bags(bag_rules)
    print(f'There are {len(base_bags)} base bags')


if __name__ == '__main__':
    main()
