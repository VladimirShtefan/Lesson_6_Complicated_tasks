from csv import DictReader


def read_file_expenses(file_name):
    """

    Args:
        file_name: путь к фалу с данными

    Returns: список с словарями данных

    """
    with open(file_name) as file:
        dict_ = []
        expenses_dict = DictReader(file)
        for line in expenses_dict:
            dict_.append(line)
        return dict_


def print_results(dict_expenses):
    """

    Args:
        dict_expenses: список с словарями данных

    Returns: выводит результаты на экран

    """
    len_dict = len(dict_expenses)
    sum_value = 0
    for expense in dict_expenses:
        sum_value += int(expense['Сумма'])
    print(f'Всего позиций: {len_dict}')
    print(f'Сумма: {sum_value}')


def main():
    try:
        print_results(read_file_expenses('files_for_ex8/expenses.csv'))
    except FileNotFoundError:
        print('Фаил не найден')


if __name__ == '__main__':
    main()
