# Задача 1.3.

# Напишите скрипт, который принимает от пользователя номер месяца, 
# а возвращает количество дней в нем.
# Результат проверки вывести на консоль
# Допущение: в феврале 28 дней
# Если номер месяца некорректен - сообщить об этом

import datetime

month_input = input("Введите, пожалуйста, номер месяца: ")
month = int(month_input)

pass
month_name = datetime.date(2023, month, 1).strftime('%B')
if 0 < month < 13:
    if month in (1, 3, 5, 7, 8, 10, 12):
        print(month_name,", " 'в этом месяце', 31, 'день')
    elif month in (4, 6, 9, 11):
        print(month_name,", " 'в этом месяце', 30, 'дней')
    elif month == 2:
        print(month_name,", " 'в этом месяце', 28, 'дней')
else:
    print('Такого месяца нет!')








