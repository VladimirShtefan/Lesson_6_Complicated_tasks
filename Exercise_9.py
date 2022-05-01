from csv import DictReader


def read_file_with_questions(file_name):
    """

    Args:
        file_name: путь к файлу с вопросами

    Returns: список словарей с вопросами

    """
    with open(file_name) as file:
        dict_ = []
        questions_dict = DictReader(file)
        for line in questions_dict:
            dict_.append(line)
        return dict_


def checking_for_correct(questions_list):
    """

    Args:
        questions_list: список словарей с вопросами

    Returns: выводит результаты на экран

    """
    for line in questions_list:
        print(f'''░░░░░░░░░░\nQuestion {line['Номер вопроса']}. {line['вопрос']}\n[ ] {line['первый ответ']}\n[ ] {line['второй ответ']}''')
        answer = input('Введите ответ: ').lower()
        if answer == line['верный ответ'].lower():
            print('Верно')
        else:
            print(f"Нет. Верный ответ – {line['верный ответ']}")


def main():
    try:
        checking_for_correct(read_file_with_questions('files_for_ex9/questions.csv'))
    except FileNotFoundError:
        print('Фаил не найден')


if __name__ == '__main__':
    main()