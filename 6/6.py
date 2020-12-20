'''part2
abc

a
b
c

ab
ac

a
a
a
a

b
This list represents answers from five groups:

In the first group, everyone (all 1 person) answered "yes" to 3 questions: a, b, and c.
In the second group, there is no question to which everyone answered "yes".
In the third group, everyone answered yes to only 1 question, a. Since some people did not answer "yes" to b or c, they don't count.
In the fourth group, everyone answered yes to only 1 question, a.
In the fifth group, everyone (all 1 person) answered "yes" to 1 question, b.
In this example, the sum of these counts is 3 + 0 + 1 + 1 + 1 = 6.
'''

import os
import re


def get_data(file_name='data.txt'):
    data_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), file_name)

    with open(data_file) as f:
        data = f.read().strip()

    return re.split(r'\n\s*\n', data)


def main():
    data = get_data()
    sum_all = sum([len(set(d.replace('\n', ''))) for d in data])
    print(sum_all)


if __name__ == '__main__':
    main()
