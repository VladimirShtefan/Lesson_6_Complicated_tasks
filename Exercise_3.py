from csv import DictReader


def read_base_students(name_data_base):
    """

    Args:
        name_data_base: фаил с списком студентов и баллами

    Returns: список разделенный на разных людей

    """
    list_data_base = []
    with open(name_data_base) as file_data_base:
        data_base = DictReader(file_data_base)
        for line in data_base:
            list_data_base.append(line)
    return list_data_base


def sort_students(base_list, file_name_good_students, file_name_bad_students):
    """

    Args:
        base_list: список разделенный на разных людей
        file_name_good_students:  список с студентами поступившими
        file_name_bad_students: список с студентами провалившие экзамен

    Returns:

    """
    file_bad = open(file_name_bad_students, 'w')
    file_good = open(file_name_good_students, 'w')
    file_bad.close()
    file_good.close()
    with open(file_name_bad_students, 'a') as file_failed, open(file_name_good_students, 'a') as file_passed:
        for student in base_list:
            if int(student['балл']) >= 75:
                file_passed.write(student['Фамилия']+'\n')
            else:
                file_failed.write(student['Фамилия']+'\n')


def main():
    try:
        sort_students(read_base_students('files_for_ex3/dict_students.csv'), 'files_for_ex3/passed.txt', 'files_for_ex3/failed.txt')
    except FileNotFoundError:
        print('Нет файла с данными о студентах')


if __name__ == '__main__':
    main()
