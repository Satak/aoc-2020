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
