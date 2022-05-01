from csv import DictReader


def read_file_with_snakes(file_name):
    '''

    Args:
        file_name: имя файла для чтения

    Returns: список с словарями змей

    '''
    with open(file_name) as file:
        snakes = DictReader(file)
        dict_ = []
        for line in snakes:
            dict_.append(line)
        return dict_


def get_results(list_snakes):
    """

    Args:
        list_snakes: список с словарями змей

    Returns: выводит на экран результат

    """
    for line in list_snakes:
        sum_points = 0
        count = 0
        for value in line.values():
            if value.isdigit():
                sum_points += int(value)
                count += 1
        average = round(sum_points/count, 1)
        print(f"{line['имя']}: {average}")


def main():
    try:
        get_results(read_file_with_snakes('files_for_ex10/snakes.csv'))
    except FileNotFoundError:
        print('Фаил не найден')


if __name__ == '__main__':
    main()
