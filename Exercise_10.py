import csv


def read_file_with_snakes(file_name):
    with open(file_name) as file:
        snakes = csv.DictReader(file)
        for line in snakes:
            sum_points = 0
            count = 0
            for value in line.values():
                if value.isdigit():
                    sum_points += int(value)
                    count += 1
            average = round(sum_points/count, 2)
            print(f"{line['имя']}: {average}")


if __name__ == '__main__':
    try:
        read_file_with_snakes('files_for_ex10/snakes.csv')
    except FileNotFoundError:
        print('Фаил не найден')
