from anytree import Node, RenderTree
from pprint import pprint
import sys


def read_input(input_file):
    '''Read the input file and return it in digestible chunks'''
    try:
        with open(input_file, 'r') as inp:
            input_str = inp.read()
            input_list = input_str.split('\n')
            return [x for x in input_list if x != '']
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


def parse_container_bag(bag_rule):
    '''If a bag contains any other bags, parse it into usable pieces and return them'''
    # example bag of bags:
    #     plaid gold bags contain 4 dark lime bags, 3 drab aqua bags, 3 dim white bags, 2 mirrored brown bags.
    outer_delimiter = ' bags contain '
    inner_delimiter = ', '
    # Error out on base bags
    if 'contain no other bags' in bag_rule:
        print('`parse_container_bag` is only supposed to parse rules for bags that contain other bags. Skipping')
        return None
    else:
        spl = bag_rule.split(outer_delimiter)
        outer_bag = spl[0]
        inner_bags = spl[1]
        inner_bag_colors = []
        # if there is a comma in the second part of `spl`, it's a list of inner bags. Split them up
        if inner_delimiter in inner_bags:
            inner_spl = inner_bags.split(inner_delimiter)
            for inner_rule in inner_spl:
                rule_spl = inner_rule.split()
                try:
                    # might need this later, grab now
                    num_inner = int(rule_spl[0])
                except:
                    pass
                inner_color = ' '.join(rule_spl[1:3])
                inner_bag_colors.append(inner_color)
        else:
            rule_spl = spl[1].split()
            try:
                num_inner = int(rule_spl[0])
            except:
                pass
            inner_color = ' '.join(rule_spl[1:3])
            inner_bag_colors.append(inner_color)

    return {outer_bag: inner_bag_colors}


def bag_dict_to_node(bag_of_dicts):
    '''Hehe, a bag of dicts 😂'''
    nodes = []
    for k, v in bag_of_dicts.items():
        n1 = Node(k)
        nodes.append(n1)
        for val in v:
            n = Node(v, parent=n1)
            nodes.append(n)

    return nodes


def get_bag_tree(rules):
    '''Get the tree hierarchy of the bags of bags of bags of bags of bags of bags...'''
    # start with the root (base) bags
    base_bags = find_base_bags(rules)
    nodes = []
    for index, bb in enumerate(base_bags):
        exec(f'node_{index} = Node("{bb}")')
        exec(f'nodes.append(node_{index})')

    return nodes


def main():
    input_file = 'input.txt'
    bag_rules = read_input(input_file)

    # list where all tree nodes will live
    nodes = []

    #for rule in bag_rules:
    #    print(rule)

    base_bag_nodes = get_bag_tree(bag_rules)
    nodes.extend(base_bag_nodes)

    for rule in bag_rules:
        bag_dict = parse_container_bag(rule)
        if bag_dict:
            node = bag_dict_to_node(bag_dict)
            nodes.extend(node)

    for n in nodes:
        print(n)


if __name__ == '__main__':
    main()
