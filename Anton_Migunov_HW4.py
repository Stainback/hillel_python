"""
1. Создать txt файл, в нем написать текст.
 - Считать данные с файла и вывести в консоль
 - Считать данные с этого же файла и записать в новый файл
 - Считать данные с этого же файла, преобразовать (любые операции) и записать в этот же файл с разделителем
   (пробел, точка, запятая и тп)
"""


def read_text_from_file(file):
    with open(file, "r") as f:
        text = f.read()
    return text


def copy_text_to_file(file):
    text = read_text_from_file(file)
    with open(f"misc/new_{file[5::]}", "w") as new_f:
        new_f.write(text)


def changed_text_to_file(file):
    text = list(read_text_from_file(file))
    for symbol in text:
        if symbol in ("a", "o", "i"):
            text.remove(symbol)
    text = ''.join(text)
    with open(file, "a") as f:
        f.write("***\n" + text)


def main1():
    file = 'misc/HW4_Text.txt'
    print(read_text_from_file(file))
    copy_text_to_file(file)
    changed_text_to_file(file)


# if __name__ == "__main__":
#     main1()

"""
2. Преобразовать дату. Нужно написать код, который из Feb 12 2019 2:41PM сделает 2019-02-12 14:41:00
"""
from datetime import datetime


def reformat_date(date_string):
    return datetime.strptime(date_string, "%b %d %Y %I:%M%p").isoformat(sep=' ')


def main2():
    date_string = "Feb 12 2019 2:41PM"
    r_date = reformat_date(date_string)
    print(r_date, type(r_date))


# if __name__ == "__main__":
#     main2()

"""
3. Напишите программу, которая принимает год, и возвращает список дат всех понедельников в данном году.
   Работа с датами (можно использовать любые модули и гуглить)
"""
import calendar


def validate(year: str):
    return all((year.isdigit(), len(year) == 4))


def mondays(year: int):
    mondays_list = []
    for month in range(1, 12):
        for week in calendar.monthcalendar(year, month):
            if week[0] != 0:
                mondays_list.append(datetime(year, month, week[0]).isoformat())
    return mondays_list


def main3():
    year = input('Enter a year in format YYYY: ')
    if validate(year):
        date_list = mondays(int(year))
        print(date_list)
    else:
        raise ValueError


# if __name__ == "__main__":
#     assert mondays(2022)[0] == '2022-01-03'
#     main3()
