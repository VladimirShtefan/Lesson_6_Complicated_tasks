import csv


def read_file_with_questions(file_name):
    with open(file_name) as file:
        questions_dict = csv.DictReader(file)
        for line in questions_dict:
            print(f'''░░░░░░░░░░\nQuestion {line['Номер вопроса']}. {line['вопрос']}
[ ] {line['первый ответ']}\n[ ] {line['второй ответ']}''')
            answer = input('Введите ответ: ').lower()
            if answer == line['верный ответ'].lower():
                print('Верно')
            else:
                print(f"Нет. Верный ответ – {line['верный ответ']}")


if __name__ == '__main__':
    try:
        read_file_with_questions('files_for_ex9/questions.csv')
    except FileNotFoundError:
        print('Фаил не найден')