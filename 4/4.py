import os
import re

STRICT_CHECK = True
PRINT_INVALID_PASSPORTS = False


class Passport:
    def __init__(self, byr, iyr, eyr, hgt, hcl, ecl, pid, cid='', strict=True):
        if strict:
            assert self.validate_range(byr, 1920, 2002, 'byr')
            assert self.validate_range(iyr, 2010, 2020, 'iyr')
            assert self.validate_range(eyr, 2020, 2030, 'eyr')
            assert self.validate_height(hgt)
            assert self.validate_hair_color(hcl)
            assert self.validate_eye_color(ecl)
            assert self.validate_passport_id(pid)
        self.byr = int(byr)
        self.iyr = int(iyr)
        self.eyr = int(eyr)
        self.hgt = hgt
        self.hcl = hcl
        self.ecl = ecl
        self.pid = pid
        self.cid = cid

    def __str__(self):
        return f'byr:{self.byr} iyr:{self.iyr} eyr:{self.eyr} hgt:{self.hgt} hcl:{self.hcl} ecl:{self.ecl} pid:{self.pid} cid:{self.cid}'

    def validate_range(self, value, min_value, max_value, field=''):
        '''
        validate byr (Birth Year) & iyr (Issue Year) & eyr (Expiration Year)
        byr: four digits; at least 1920 and at most 2002
        iyr: four digits; at least 2010 and at most 2020
        eyr: four digits; at least 2020 and at most 2030
        hgt: cm between 150, 193, in between 59, 76
        '''
        try:
            is_valid_value = min_value <= int(value) <= max_value
            assert is_valid_value
        except:
            raise ValueError(
                f'Range validation failed: min: {min_value} value: {value} max: {max_value} field: {field}')

        return is_valid_value

    def validate_height(self, value):
        ranges = {
            'cm': (150, 193),
            'in': (59, 76)
        }

        try:
            height = re.search(r'^\d+', value).group(0)
            unit = re.search(r'(in|cm)$', value).group(0)
            return self.validate_range(height, *ranges[unit], 'height')
        except:
            raise ValueError(
                f'Height (hgt:{value}) failed, value {value} not in ranges: {ranges}')

    def validate_hair_color(self, value):
        try:
            re.search(r'^#[a-f0-9]{6}$', value).group(0)
            return True
        except:
            raise ValueError(
                f'Hair color (hcl:{value}) failed, not match "#[0-9a-f]6 digits"')

    def validate_eye_color(self, value):
        try:
            re.search(r'^(amb|blu|brn|gry|grn|hzl|oth)$', value).group(0)
            return True
        except:
            raise ValueError(
                f'Eye color (ecl:{value}) failed, not match amb|blu|brn|gry|grn|hzl|oth')

    def validate_passport_id(self, value):
        try:
            re.search(r'^\d{9}$', value).group(0)
            return True
        except:
            raise ValueError(
                f'Passport ID (pid:{value}) failed, not match 9 digit number')


def get_passport_data(file_name):
    data_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), file_name)

    with open(data_file) as f:
        data = f.read().strip()

    return re.split(r'\n\s*\n', data)


def count_valid_passports(passports):
    valid_passport_count = 0
    for index, passport in enumerate(passports):
        passport_params_array = []
        try:
            passport_params_array = sorted(re.split(r'\s', passport))
            passport = Passport(**dict([param.split(':')
                                        for param in passport_params_array]), strict=STRICT_CHECK)
            valid_passport_count += 1
        except Exception as err:
            if PRINT_INVALID_PASSPORTS:
                print(index, err, '---', passport_params_array)
    return valid_passport_count


def main():

    passports = get_passport_data('data.txt')
    valid_passport_count = count_valid_passports(passports)

    print('Valid Passports:', valid_passport_count, f'/ {len(passports)}\n')


if __name__ == '__main__':
    main()
