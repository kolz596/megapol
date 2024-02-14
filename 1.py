import csv
with open('vacancy.csv', 'r',encoding='UTF-8') as file, open('vacancy_new.csv', 'w',encoding='UTF-8',newline='') as new_file:
    reader = csv.DictReader(file, delimiter = ";")
    writer = csv.DictWriter(file, ['company', 'role', 'Salary'], delimiter = ";")
    writer.writeheader()
    for row in reader:
        if
        
        writer.writerow(row)
