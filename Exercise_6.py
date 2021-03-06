def read_file_with_todo_list(name_file):
    """

    Args:
        name_file: путь к файлу с задачами

    Returns: словарь с задачами

    """
    dict_todo_list = {}
    with open(name_file) as file:
        for line in file:
            key, value = line.split(':')
            dict_todo_list[key] = value.rstrip()
        return dict_todo_list


def count_len_list(dict_todo):
    """

    Args:
        dict_todo: словарь с задачами

    Returns: сообщение с кол-вом дел

    """
    return print(f'В списке {len(dict_todo)} дел')


def count_len_todo_list(dict_todo):
    """

    Args:
        dict_todo: словарь с задачами

    Returns: сообщение сколько сделано дел из общего кол-ва

    """
    count_todo = 0
    for value in dict_todo.values():
        if 'to_do' in value.lower():
            count_todo += 1
    if count_todo == len(dict_todo):
        return 'Нет не выполненных дел'
    return f'Сделано {count_todo}/{len(dict_todo)}'


def check_done_tasks(dict_todo):
    """

    Args:
        dict_todo: словарь с задачами

    Returns: словарь с делами после опроса пользователя

    """
    for key, value in dict_todo.items():
        if 'done' in value.lower():
            print(f'{key} - сделано? (y/n)')
            answer = input()
            if answer == 'y':
                dict_todo[key] = ' TO_DO'
    return dict_todo


def write_dict_todo_in_file(file_name, dict_todo):
    """

    Args:
        file_name: путь к фаилу для записи дел
        dict_todo: словарь с делами

    Returns:

    """
    with open(file_name, 'w') as file:
        for key, value in dict_todo.items():
            file.write(f'{key}:{value}\n')


def main():
    dict_with_todo_list = read_file_with_todo_list('files_for_ex6/todo.txt')
    count_len_list(dict_with_todo_list)
    print(count_len_todo_list(dict_with_todo_list))
    if count_len_todo_list(dict_with_todo_list) != 'Нет не выполненных дел':
        print('Давай пройдемся по твоим делам!')
    write_dict_todo_in_file('files_for_ex6/todo.txt', check_done_tasks(dict_with_todo_list))
    print('Список дел обновлен, смотри файл')


if __name__ == '__main__':
    main()
