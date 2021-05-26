import os

home_dir = os.getcwd()
files = os.listdir(home_dir)
counted_files = {}

for file_name in files:
    counter = 0
    if '.txt' in file_name:
        with open(file_name, encoding='UTF-8') as working_file:
            for line in working_file:
                counter += 1
            counted_files[counter] = file_name
counted_files = dict(sorted(counted_files.items()))

final_file = ''
counter = 0
for lines, file_name in counted_files.items():
    counter += 1
    with open(file_name, encoding='UTF-8') as working_file:
       final_file +=  file_name + '\n' + str(lines) + '\n'

       for line in working_file:
           final_file += (line.strip('\n') + ' |файл номер ' + str(counter) + '\n')
       print(final_file)

with open('end_file.txt', 'w', encoding='UTF-8') as f:
    f.write(final_file)


