def read_file(file_name):
    """

    Args:
        file_name: название файла с текстом

    Returns: строку с текстом

    """
    try:
        with open(f'files_for_ex7/{file_name}.txt') as file:
            text_file = file.read()
            return text_file
    except FileNotFoundError:
        return print('Не верное имя файла')


def get_results(text_file):
    """

    Args:
        text_file: строка с текстом

    Returns: результаты обработки

    """
    number_count_clause = 0
    count_string = len(text_file.split('\n'))
    print(f'Строк: {count_string}')
    count_words = text_file.count(' ')
    count_words_new_string = text_file.count('\n')
    print(f'Слов: {count_words+count_words_new_string-1}')
    count_symbols = len(text_file)
    print(f'Символов: {count_symbols}')
    for text in text_file.replace('\n', '').split('.'):
        try:
            if text.lstrip()[0].isupper():
                number_count_clause += 1
        except IndexError:
            continue
    print(f'Предложений: {number_count_clause}')


def main():
    name_file = input('Введите название файла: ')
    get_results(read_file(name_file))


if __name__ == '__main__':
    main()
