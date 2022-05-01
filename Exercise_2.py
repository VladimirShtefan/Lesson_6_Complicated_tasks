from csv import DictReader


def get_definition(request, file_name):
    """

    Args:
        request: термин введенный пользователем
        file_name: имя файла для с терминами и определениями

    Returns:

    """
    with open(file_name) as file:
        system_dict = DictReader(file)
        for line in system_dict:
            for key, definition in line.items():
                if request == key.lower():
                    return definition
    temp = '\n- '.join(line)
    return f"По вашему запросу ничего не найдено, могу предложить:\n- {temp}"


def main():
    """

    Returns: выводит на экран результат

    """
    try:
        print(get_definition(input('Введите термин: ').lower(), 'files_for_ex2/Dictionary.csv'))
    except FileNotFoundError:
        print('Нет файла с терминами')


if __name__ == '__main__':
    main()
