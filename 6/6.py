import os


def get_data(file_name='data.txt'):
    data_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), file_name)

    with open(data_file) as f:
        return f.read().strip().split('\n')


def main():
    data = get_data()


if __name__ == '__main__':
    main()
