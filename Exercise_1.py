Name_file_miles = 'files_for_ex1/miles.txt'
Name_file_kilometers = 'files_for_ex1/kilometers.txt'


def convert_miles(file_txt):
    """

    Args:
        file_txt: пусть к файлу с длинами в милях

    Returns: список из значений переведенных из миль в км

    """
    kilometers_list = []
    try:
        with open(file_txt) as file:
            for line in file:
                kilometers_list.append(str(float(line) * 1.609)+'\n')
    except FileNotFoundError:
        return ['Фаил не найден']
    return kilometers_list


def write_results(file_txt, list_txt):
    """

    Args:
        file_txt: пусть к файлу для записи результатов перевода
        list_txt: список из значений переведенных из миль в км

    Returns:

    """
    with open(file_txt, 'w') as file_kilometers:
        file_kilometers.writelines(list_txt)


def main():
    write_results(Name_file_kilometers, convert_miles(Name_file_miles))


if __name__ == '__main__':
    main()
