import csv


def read_file_expenses(file_name):
    len_dict = 0
    summ_value = 0
    with open(file_name) as file:
        expenses_dict = csv.DictReader(file)
        for line in expenses_dict:
            len_dict += 1
            summ_value += int(line['Сумма'])
    print(f'Всего позиций: {len_dict}')
    print(f'Сумма: {summ_value}')


if __name__ == '__main__':
    try:
        read_file_expenses('files_for_ex8/expenses.csv')
    except FileNotFoundError:
        print('Фаил не найден')