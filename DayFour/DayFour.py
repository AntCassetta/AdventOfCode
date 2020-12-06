import logging as log
import re

def run():
    pass_ports = []
    valid_count = 0
    valid_passports = []

    with open('DayFourData.bat', 'r') as file:
        lines = file.read().splitlines()
        lines.append('')
        passport = {}
        for line in lines:
            if line == '':
                pass_ports.append(passport.copy())
                passport = {}
            else:
                line = line.split(' ')
                # log.debug(f'{line}')
                for item in line:
                    item = item.split(":")
                    key = item[0]
                    value = item[1]
                    # log.debug(f'{key}, {value}')
                    passport[key] = value

    for doc in pass_ports:
        if is_valid(doc):
            valid_count += 1
            valid_passports.append(doc.copy())
        else:
            continue
    for passport in valid_passports:
        log.debug(f'valid pass ports {passport["hcl"]}')
    log.info(f'Valid Passport count {valid_count}')


def is_valid(doc):
    key_list = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

    valid_byr = [1920, 2002]
    valid_iyr = [2010, 2020]
    valid_eyr = [2020, 2030]
    valid_cm = [150, 195]
    valid_in = [59, 76]
    valid_hcl = re.compile(r'#([a-zA-Z0-9]){6, 6}$')
    valid_ecl = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    valid_pid = re.compile(r'^\d{9}')
    for key in key_list:
        if key not in doc.keys():
            log.error('invalid missing keys')
            return False
    try:
        if int(doc['byr']) not in range(valid_byr[0], valid_byr[-1]+1):
            log.error('invalid byr')
            return False
        if int(doc['iyr']) not in range(valid_iyr[0], valid_iyr[-1]+1):
            log.error('invalid iyr')
            return False
        if int(doc['eyr']) not in range(valid_eyr[0], valid_eyr[-1]+1):
            log.error('invalid eyr')
            return False
        if doc['hgt'].endswith('cm'):
            if int(doc['hgt'].replace('cm', '')) not in range(valid_cm[0], valid_cm[-1]+1):
                log.error('invalid hgt cm')
                return False
        elif doc['hgt'].endswith('in'):
            if int(doc['hgt'].replace('in', '')) not in range(valid_in[0], valid_in[-1]+1):
                log.error('invalid hgt in')
                return False
        else:
            return False
        if not (doc['hcl'].startswith('#') or len(doc['hcl']) == 7):
            log.error('invalid hcl')
            return False
        if doc['ecl'] not in valid_ecl:
            log.error('invalid ecl')
            return False
        if not (len(doc['pid']) == 9 or not int(doc['pid'])):
            log.error('invalid pid')
            return False
    except ValueError as e:
        log.error(e)
        return False
    return True


if __name__ == '__main__':
    log.basicConfig(format='%(levelname)s:%(message)s', level=log.INFO)
    run()