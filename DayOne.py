import csv
import logging as log

def run():

    data = []
    sum_2020 = []
    answer = 0
    with open('DayOneData.csv', 'r') as csvfile:
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
            # TODO check that you dont get the same pair in diff order Cassetta 11/05/2020
            if (x != y) and (x + y == 2020):
                log.info('x {0} + {1} = {2}'.format(x, y, (x+y)))
                sum_2020.append((x, y))

    log.info('Matched pairs equal to 2020 is {0}'.format(sum_2020))
    answer = sum_2020[0][0] * sum_2020[0][1]
    log.info('Answer {0}'.format(answer))

if __name__ == '__main__':
    log.basicConfig(format='%(levelname)s:%(message)s', level=log.DEBUG)
    run()
