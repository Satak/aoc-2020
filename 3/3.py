import os
from math import prod


data_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data.txt')

with open(data_file) as f:
    data = f.read().strip().split('\n')

TREE_SYMBOL = '#'


def count_trees(data, right, down):
    trees = 0
    index = right
    max_index = len(data[0])-1

    for line in data[down::down]:
        if line[index] == TREE_SYMBOL:
            trees += 1

        if index > max_index - right:
            index = index + right - max_index - 1
        else:
            index += right
    return trees


slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]

trees_array = [count_trees(data, *slope) for slope in slopes]

print('Trees product:', prod(trees_array))
