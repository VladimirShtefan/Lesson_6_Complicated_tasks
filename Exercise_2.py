import csv


def get_definition(request, file_name):
    with open(file_name) as file:
        system_dict = csv.DictReader(file)
        for line in system_dict:
            for key, definition in line.items():
                if request == key.lower():
                    return definition
    temp = '\n- '.join(line)
    return f"По вашему запросу ничего не найдено, могу предложить:\n- {temp}"


if __name__ == '__main__':
    print(get_definition(input('Введите термин: ').lower(), 'files_for_ex2/Dictionary.csv'))
