import logging as log


def run():
    seat_ids = []
    seat_data = []

    with open('DayFiveData.csv', 'r') as file:
        seat_data = file.read().splitlines()

    for seat in seat_data:
        row = [*range(0, 127 + 1)]
        column = [*range(0, 7 + 1)]
        for i in seat:
            if i == "F":
                row_mid = len(row) // 2
                row = row[:row_mid]
                log.debug(f'F row {row}')
            if i == "B":
                row_mid = len(row) // 2
                row = row[row_mid:]
                log.debug(f'B row {row}')
            if i == "L":
                col_mid = len(column) // 2
                column = column[:col_mid]
                log.debug(f'L Column {column}')
            if i == "R":
                col_mid = len(column) // 2
                column = column[col_mid:]
                log.debug(f'R Column {column}')

        log.debug(f'end row {row}, column {column}')
        row_val = row[0]
        col_val = column[0]
        seat_id = ((row_val * 8) + col_val)
        seat_ids.append(seat_id)

    log.info(f'Highest boarding pass ID {max(seat_ids)}')
    return seat_ids


def my_seat(seat_map):
    seat_map.sort()
    seat = [x for x in range(seat_map[0], seat_map[-1] + 1) if x not in seat_map]
    log.info(f'My seat is: {seat}')


if __name__ == '__main__':
    log.basicConfig(format='%(levelname)s:%(message)s', level=log.DEBUG)
    taken_seats = run()
    my_seat(taken_seats)
