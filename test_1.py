from random import randint
import xlsxwriter
import datetime
import os
import crypt


def password_generator():  #создание паролей
    password = randint(1000, 9999)
    return str(password)


def login_creation(): #создание логинов
    start_number_login = int(input())
    with open('./test', encoding="utf-8") as file:
        seq = [item.split() for item in file.readlines()]
        for item in seq:
            item.append('usr_' + str(start_number_login))
            start_number_login += 1
            item.append(password_generator())
        return seq


def write_file(lst_login): #запись созданных логинов и паролей в exel таблицу
    output = datetime.date.today()

    workbook = xlsxwriter.Workbook(str(output) + '.xlsx')
    worksheet = workbook.add_worksheet()

    worksheet.write('A1', 'Фамилия')
    worksheet.write('B1', 'Имя')
    worksheet.write('D1', 'Логин')
    worksheet.write('E1', 'Пароль')
    worksheet.write('C1', 'Класс')
    for i, item in enumerate(lst_login, 2):
        worksheet.write('A' + str(i), item[0])
        worksheet.write('B' + str(i), item[1])
        worksheet.write('C' + str(i), item[2])
        worksheet.write('D' + str(i), item[3])
        worksheet.write('E' + str(i), item[4])
    workbook.close()


def user_add(lst_login): #добавление пользователя в ОС
    for item in lst_login:
        password = crypt.crypt(str(item[4]), "22")
        print(password)
        os.system("sudo useradd -d /home/{surname} -p {password} -c '{surname} {name} {klass}' {login}".format(surname=item[0], name=item[1], klass=item[2], login=item[3], password=password))


def user_del(lst_login):  # удаление пользователя по списку

    for item in lst_login:
        os.system("sudo userdel" + " -r " + item[3])

def main()
    lst_login = login_creation()
    write_file(lst_login)   
    user_add(lst_login)

main()


