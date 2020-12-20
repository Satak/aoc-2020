import os

data_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data.txt')


with open(data_file) as f:
    data = f.read().split('\n')


def part_one(data):
    stop = False
    for index1, num1 in enumerate(data):
        for index2, num2 in enumerate(data):
            if num1 and num2 and index1 != index2 and int(num1) + int(num2) == 2020:
                res = int(num1) * int(num2)
                print(f'{num1} + {num2} == 2020')
                print(f'{num1} * {num2} == {res}')
                stop = True
                break
        if stop:
            break


def part_two(data):
    stop = False
    for index1, num1 in enumerate(data):
        for index2, num2 in enumerate(data):
            for index3, num3 in enumerate(data):
                if num1 and num2 and num3 and len(set([index1, index2, index3])) != 1 and int(num1) + int(num2) + int(num3) == 2020:
                    res = int(num1) * int(num2) * int(num3)
                    print(f'{num1} + {num2} + {num3} == 2020')
                    print(f'{num1} * {num2} * {num3} == {res}')
                    stop = True
                    break
            if stop:
                break
        if stop:
            break


part_one(data)
part_two(data)
