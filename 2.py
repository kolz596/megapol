"""
после обработки файла был создан массив, который я отсортировал по кол-ву сотрудников при помощи сортировки "пузырьком".

"""
a = []
with open('vacancy.csv','r',encoding='UTF-8') as file:
    for i in file:
        a.append(i.split(';'))
for i in range(1,len(a)):
    for j in range(1,len(a)-1):
        if int(a[i][2]) < int(a[j][2]):
            a[j],a[i] = a[i], a[j]
for vacancy in a:
    if vacancy[3] == 'классный руководитель':
        print("В компании "+vacancy[4]+" есть заданная профессия: "+vacancy[3]+","+" з/п в такой компании составит:"+vacancy[0])
        break