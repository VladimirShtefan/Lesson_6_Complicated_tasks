list_kilometers = []
try:
    with open('files_for_ex1/miles.txt') as file_miles:
        list_miles = file_miles.readlines()
except FileNotFoundError:
    list_miles = ['0.0']
    print('Нет файла с милями')

for line in list_miles:
    list_kilometers.append(str(float(line.replace('\n', '')) * 1.609)+'\n')

with open('files_for_ex1/kilometers.txt', 'w') as file_kilometers:
    file_kilometers.writelines(list_kilometers)
