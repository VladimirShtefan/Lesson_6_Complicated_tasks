def read_file_with_messages(name_file):
    """

    Args:
        name_file: путь к файлу с сообщениями

    Returns: список сообщений

    """
    with open(name_file) as file:
        return file.readlines()


def search_word(user_word, list_of_words):
    """

    Args:
        user_word: искомое слово введенное пользователем
        list_of_words: список сообщений в которых выполняем поиск

    Returns: результат поиска

    """
    counter_words = 0
    for line in list_of_words:
        if user_word in line.lower():
            counter_words += 1
    return f'Ищем: {user_word}\nНайдено сообщений: {counter_words}'


def main():
    word = input('Введите слово: ').lower()
    try:
        print(search_word(word, read_file_with_messages('files_for_ex4/messages.txt')))
    except FileNotFoundError:
        print('Нет файла с сообщениями')


if __name__ == '__main__':
    main()
