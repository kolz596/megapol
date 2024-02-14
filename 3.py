import csv
def f(comp: str)->str:
    """
    на обработку функции поступает название компании.
    если данное название присутствует в файле vacancy.csv, то функция возвращает ее название, вакансию и зарплату.

    :param comp: название компании, строковый тип данных
    :return:
    """

    with open('vacancy.csv','r',encoding='UTF-8') as file:
        reader = csv.DictReader(file, ["Salary","Work_Type","Company_Size","Role","Company"],delimiter = ";")
        for company in reader:
            flag = True
            if company["Company"] == comp:
                return f"В {company['Company']} найдена вакансия: {company['Role']}. З/п составит: {company['Salary']}"
            else:
                flag = False
        if flag == False:
            return f"К сожалению, ничего не удалось найти"

flag1 = True
while flag1 == True:
    comp = input()
    if comp == "None":
        flag1 = False
    else:
        print(f(comp))