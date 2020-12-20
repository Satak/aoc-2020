import os


def get_data(file_name='data.txt'):
    data_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), file_name)

    with open(data_file) as f:
        return f.read().strip().split('\n')


def row_to_int(item):
    return int(item[:-3].replace('F', '0').replace('B', '1'), 2)


def column_to_int(item):
    return int(item[-3:].replace('L', '0').replace('R', '1'), 2)


def calc_id(item):
    row = row_to_int(item)
    column = column_to_int(item)
    return row * 8 + column


def main():
    seat_ids = sorted([calc_id(item) for item in get_data()])

    max_id = max(seat_ids)
    print('max seat id:', max_id)

    last_seat = seat_ids[0] - 1
    for seat in seat_ids:
        if seat - last_seat != 1:
            print('your seat:', seat - 1)
        last_seat = seat


if __name__ == '__main__':
    main()
