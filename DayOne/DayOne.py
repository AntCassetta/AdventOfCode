import csv
import logging as log

def run():

    data = []
    sum_2020 = []
    answer = 0
    with open('DayOne/DayOneData.csv', 'r') as csvfile:
        spamreader = csv.reader(csvfile, delimiter='\n')
        for row in spamreader:
            data.append(row)
    log.info('number of data points {0}'.format(len(data)))
    x = 0
    y = 0
    for i in data:
        x = int(i[0])
        for n in data:
            y = int(n[0])
            if (x != y) and (x + y == 2020):
                sum_2020.append((x, y))

    log.info('Matched pairs equal to 2020 is {0}'.format(sum_2020))
    answer = sum_2020[0][0] * sum_2020[0][1]
    log.info('Answer {0}'.format(answer))

    # puzzle two
    puzzle_two = []
    z = 0
    for i in data:
        x = int(i[0])
        for n in data:
            y = int(n[0])
            for o in data:
                z = int(o[0])
                if (x != y) and (x != z) and (y != z) and ((x + y + z) == 2020):
                    puzzle_two.append((x, y, z))

    log.info('three sum to 2020 {0}'.format(puzzle_two))

    answer = (puzzle_two[0][0] * puzzle_two[0][1] * puzzle_two[0][2])
    log.info('puzzle two answer {0}'.format(answer))


if __name__ == '__main__':
    log.basicConfig(format='%(levelname)s:%(message)s', level=log.DEBUG)
    run()
