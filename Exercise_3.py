import csv


def read_base_students(name_data_base):
    list_data_base = []
    with open(name_data_base) as file_data_base:
        data_base = csv.DictReader(file_data_base)
        for line in data_base:
            list_data_base.append(line)
    return list_data_base


def sort_students(base_list, file_name_good_students, file_name_bad_students):
    file_bad = open(file_name_bad_students, 'w')
    file_good = open(file_name_good_students, 'w')
    file_bad.close()
    file_good.close()
    with open(file_name_bad_students, 'a') as file_failed:
        with open(file_name_good_students, 'a') as file_passed:
            for student in base_list:
                if int(student['балл']) >= 75:
                    file_passed.write(student['Фамилия']+'\n')
                else:
                    file_failed.write(student['Фамилия']+'\n')


sort_students(read_base_students('dict_students.csv'), 'files_for_ex3/passed.txt', 'files_for_ex3/failed.txt')
