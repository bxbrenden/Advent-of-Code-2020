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
    '''Find the bags that contain no other bags and return them in a list of two-word, space-delimited color descriptions'''
    base_bags = []
    for rule in rule_list:
        if 'contain no other bags' in rule.lower():
            color = rule.split(' ')[:2]
            color_str = ' '.join(color)
            print(f'The {color_str} bag is a base bag')
            base_bags.append(color_str)

    return base_bags


def find_parent_bags(parents, base_bags):
    '''Starting with a list of parent bag rules and a list of base bags, construct a list of lists where each child list is
    a bag lineage. Each lineage goes from outermost bag (index 0) to the innermost base bag (index -1)'''

    # Each parent bag contains the string ' bags contain ' exactly once between the name of the parent bag and its list of children
    parent_delimiter = ' bags contain '
    for p in parents:
        parent_spl = p.split(parent_delimiter)
        parent_color = parent_spl[0]
        child_list = parent_spl[1]

        child_colors = []

        # if there is an instance of ', ' in child_list, it means there are mulitple child bags
        child_delimiter = ', '
        if child_delimiter in child_list:
            children = child_list.split(child_delimiter)
            for child in children:
                # we only care about child color for this part
                child_spl = child.split(' ')
                num_bags = int(child_spl[0])
                child_color = ' '.join(child_spl[1:3])
                child_colors.append(child_color)
        else:
            # we only care about child color for this part
            child_spl = child_list.split(' ')
            num_bags = int(child_spl[0])
            child_color = ' '.join(child_spl[1:3])
            child_colors.append(child_color)

        for cc in child_colors:
            if cc in base_bags:
                print(f'{parent_color} bags are the direct parents of {cc} bags')


def main():
    input_file = 'input.txt'
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

    parent_rules = [r for r in bag_rules if 'contain no other bags' not in r.lower()]

    lineages = find_parent_bags(bag_rules, base_bags)


if __name__ == '__main__':
    main()
