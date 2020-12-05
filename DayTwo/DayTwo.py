import csv
import logging as log


def run():
    valid_count = 0
    puzzle_two_count = 0
    with open('DayTwoData.csv', 'r') as csvfile:
        spam_reader = csv.reader(csvfile, delimiter='\n')
        for row in spam_reader:
            line = row[0].split()
            log.debug(row)
            log.debug('{0}'.format(line))
            values = line[0].split('-')
            char = line[1].replace(':', '')
            password = line[-1]
            log.debug('{0} {1}, {2}'.format(values, char, password))
            min_required = int(values[0])
            max_allowed = int(values[1])
            count = int(password.count(char))
            log.debug('min {0}, max {1}, count {2}'.format(min_required, max_allowed, count))
            is_valid = min_required <= count <= max_allowed
            if is_valid:
                valid_count += 1
            # Puzzle two
            first_position = min_required
            second_position = max_allowed
            is_first = char == password[(min_required - 1)]
            is_second = char == password[(max_allowed - 1)]

            if (is_first and not is_second) or (not is_first and is_second):
                puzzle_two_count += 1

    log.info('valid count is {0}'.format(valid_count))
    log.info('valid count puzzle two is {0}'.format(puzzle_two_count))


if __name__ == '__main__':
    log.basicConfig(format='%(levelname)s:%(message)s', level=log.DEBUG)
    run()