import logging as log


def run():
    entries = []
    with open('DaySixData.csv', 'r') as file:
        lines = file.read().splitlines()
        lines.append('')

    group = []
    count = {}
    line_cnt = 0
    for line in lines:
        if line == '':
            log.debug(f'count {count}')
            count['line_cnt'] = line_cnt
            group.append(count.copy())
            count = {}
            line_cnt = 0

        else:
            line_cnt += 1
            for c in line:
                if c != 'line_cnt':
                    count[c] = count.setdefault(c, 0) + 1

    total_count = 0
    for entry in group:
        hold = entry.pop('line_cnt')
        total_count += len(entry.keys())
        entry['line_cnt'] = hold

    log.info(f'entry sum {total_count}')
    return group


def puzzle_two(group_data):
    run_cnt = []
    cnt = 0
    for entry in group_data:
        lines = entry.pop('line_cnt')

        for key in entry.keys():
            if entry[key] == lines:
                cnt += 1

        run_cnt.append(cnt)
        cnt = 0
    log.info(f'running count: {sum(run_cnt)}')


if __name__ == '__main__':
    log.basicConfig(format='%(levelname)s:%(message)s', level=log.DEBUG)
    counts = run()
    puzzle_two(counts)
