import logging as log


def run(right, down):
    hill_data = []
    tree_count = 0
    with open('DayThreeData.csv', 'r') as file:
        hill_data = file.read().splitlines()
        log.debug(hill_data)

    i = down
    position = right
    line_len = len(hill_data[0])

    while i < len(hill_data):
        next_position = hill_data[i][position]
        is_tree = next_position == '#'
        if is_tree:
            tree_count += 1
        position = position + right
        if position >= line_len:
            position = position - line_len
        i += down

    log.info('Number of trees encountered is {0}'.format(tree_count))
    return tree_count


if __name__ == '__main__':
    log.basicConfig(format='%(levelname)s:%(message)s', level=log.INFO)
    total = 1
    total *= run(1, 1)
    total *= run(3, 1)
    total *= run(5, 1)
    total *= run(7, 1)
    total *= run(1, 2)
    log.info(f'total of all paths {total}')


