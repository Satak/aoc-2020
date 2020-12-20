import os
import re

data_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data.txt')


with open(data_file) as f:
    data = f.read().strip().split('\n')


def get_min_max(line):
    min_count, max_count = re.search(r'^\d+-\d+', line).group(0).split('-')
    return int(min_count), int(max_count)


def get_letter(line):
    return re.search(r'[^0-9]:', line).group(0).split(':')[0]


def get_pw(line):
    return re.search(r':\s\w+', line).group(0).split(': ')[1]


def main(data):
    counter1 = 0
    counter2 = 0

    for line in data:
        min_count, max_count = get_min_max(line)
        letter = get_letter(line)
        pw = get_pw(line)

        # part one
        if min_count <= pw.count(letter) <= max_count:
            counter1 += 1

        # part two
        has_min = pw[min_count-1] == letter
        has_max = pw[max_count-1] == letter
        found_letters = [has_min, has_max]
        if any(found_letters) and not all(found_letters):
            print(line)
            counter2 += 1

    return counter1, counter2


print(main(data))
