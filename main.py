"""This module returns all the possible combinations of all the lengths of a given string"""

def get_combinations(string: str):
    """Generates the combinations one by one"""

    for num in range(1, 2 ** len(string)):
        combiner = bin(num).replace('0b', '').zfill(len(string))
        combi = ''
        for index, state in enumerate(combiner):
            if state == '1':
                combi += string[index]
        yield combi

if __name__ == '__main__':
    sample = input('Enter any string: ')
    print(list(get_combinations(sample)))
