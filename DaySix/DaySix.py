import logging as log


def run():
    entries = []
    with open('DaySixData.csv', 'r') as file:
        lines = file.read().splitlines()
        lines.append('')

    group = []
    count = {}
    for line in lines:
        if line == '':
            chars = 0
            big_set = set()
            log.debug(f'count {count}')
            group.append(count.copy())
            count = {}

        else:
            for c in line:
                count[c] = count.setdefault(c, 0) + 1

    total_count = 0
    for entry in group:
        total_count += len(entry.keys())

    log.info(f'entry sum {total_count}')


if __name__ == '__main__':
    log.basicConfig(format='%(levelname)s:%(message)s', level=log.DEBUG)
    run()
