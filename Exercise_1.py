list_kilometers = []

with open('files_for_ex1/miles.txt') as file_miles:
    list_miles = file_miles.readlines()

for line in list_miles:
    list_kilometers.append(str(float(line.replace('\n', '')) * 1.609)+'\n')

with open('files_for_ex1/kilometers.txt', 'w') as file_kilometers:
    file_kilometers.writelines(list_kilometers)
