from day1_part1 import open_input, sums_to_x


def threesum_2020(numbers, index):
    '''Given a list of numbers, return a tuple of the three that sum to 2020'''
    first = numbers[index]
    print(f'Setting first to {first}')
    diff = 2020 - first
    print(f'Looking for two numbers that sum to {diff}')
    rest = [x for x in numbers if x != first]

    second_and_third = sums_to_x(rest, diff)
    if second_and_third:
        return (first, second_and_third[0], second_and_third[1])
    else:
        return threesum_2020(numbers, index+1)


def ensure_sum(f, s, t, num):
    '''Given 3 numbers `f`, `s`, and `t`, and a sum `num`, ensure that f, s, and t sum to num'''
    try:
        assert f + s + t == num
    except AssertionError:
        print(f'The numbers {f}, {s}, and {t} do not sum to {num}')
        return False
    else:
        return True


def main():
    numbers = open_input('input.txt')
    first, second, third = threesum_2020(numbers, 0)
    is_correct = ensure_sum(first, second, third, 2020)
    if is_correct:
        print(f'First: {first}, second: {second}, third: {third}')
        print(f'ANSWER: {first * second * third}')


if __name__ == '__main__':
    main()
