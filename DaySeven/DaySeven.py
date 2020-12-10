import logging as log


def get_rules():
    with open('DaySevenData.csv', 'r') as file:
        lines = file.read().splitlines()

    rules = {}
    inner_bags = {}

    for line in lines:
        line = line.replace('.', '').replace('bags', 'bag')
        line = line.split('contain')
        bags = line[1].split(',')
        outer_bag = line.pop(0).strip()
        log.debug(f'bag: {outer_bag}: line: {line}')

        for i in range(0, len(bags)):
            bags[i] = bags[i].strip()
            if bags[i][:1].isdigit():
                bag = bags[i][1:].strip()
                inner_bags[bag] = bags[i][:1]
            elif bags[i][:2].startswith('no'):
                bag = bags[i].strip()
                inner_bags[bag] = 0
            else:
                continue
        log.debug(f'Remaining inner bags: {inner_bags}')
        rules[outer_bag] = inner_bags.copy()
        inner_bags.clear()

    return rules


def get_possible_outer_bag(bag_color, luggage_rules):
    count = 0
    containing_bags = []

    for outer_bag in luggage_rules.keys():
        log.debug(f'Outer bag "{outer_bag}"')
        if outer_bag == bag_color:
            count += 1

        outer = luggage_rules[outer_bag]
        for key, value in outer.items():
            log.debug(f'Outer item key, value: {key}:{value}')
            try:
                if int(value) >= 1 and key == bag_color:
                    count += 1
                    containing_bags.append(outer_bag)
            except ValueError as e:
                log.error(f'{e}')

    return count, containing_bags


if __name__ == '__main__':
    log.basicConfig(format='%(levelname)s:%(message)s', level=log.DEBUG)
    bag_rules = get_rules()
    inner_color = 'shiny gold bag'

    total_count, master_container_bags = get_possible_outer_bag(bag_color=inner_color, luggage_rules=bag_rules)
    log.debug(f'Containing bags: {master_container_bags}')

    log.info(f'Number of possible outer bags for {inner_color} is {total_count}')
