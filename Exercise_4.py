def read_file_with_messages(name_file):
    with open(name_file) as file:
        return list(file)


def search_word(user_word, list_of_words):
    counter_words = 0
    for line in list_of_words:
        if user_word in line.lower():
            counter_words += 1
    return f'Ищем: {user_word}\nНайдено сообщений: {counter_words}'


if __name__ == '__main__':
    word = input('Введите слово: ').lower()
    try:
        print(search_word(word, read_file_with_messages('files_for_ex4/messages.txt')))
    except FileNotFoundError:
        print('Нет файла с сообщениями')
