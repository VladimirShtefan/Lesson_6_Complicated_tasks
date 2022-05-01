def read_line_in_file(name_file):
    """

    Args:
        name_file: путь к фалу с разметкой дороги

    Returns: список дороги по линиям

    """
    with open(name_file) as file:
        return file.readlines()


def lidar(data, position=3):
    """

    Args:
        data: список дороги по линиям
        position: стартовая позиция машины

    Returns: направление движения

    """
    if not data:
        return print('Фаил с дорогой пуст')
    for line in data:
        line = line.rstrip().replace(' ', '')
        try:
            if line[position-1] != '▓':
                print('stay')
                position = position
            elif line[position-2] != '▓' and position-2 >= 0:
                print('rigth')
                position = position - 1
            elif line[position] != '▓' and position != len(line):
                print('left')
                position = position + 1
            else:
                return print('stop')
        except IndexError:
            return print('Вы стоите на обочине')


def main():
    try:
        lidar(read_line_in_file('files_for_ex5/furry_road.txt'), 1)
    except FileNotFoundError:
        print('Нет файла для чтения')


if __name__ == '__main__':
    main()
