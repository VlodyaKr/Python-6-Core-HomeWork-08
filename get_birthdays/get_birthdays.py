"""
Модуль get_birthdays містить функцію get_birthdays_per_week(colleagues: list, run_day: datetime) -> None для виведення
списку Днів Народження на найближчий тиждень.
"""

import datetime


def get_birthdays_per_week(users: list, run_day=datetime.datetime.now().date()) -> None:
    """Функція get_birthdays_per_week(colleagues: list, run_day: datetime) -> None виводить список Днів Народження в
    найближчі 7 днів. В понеділок та неділю виведення починається з минулої суботи, в інші дні - з поточного дня.
    :param users: список словників users, кожен словник в якому обов'язково має ключі name: str - ім'я
    та birthday: str - дата формату str 'DD.MM.YYYY'
    :param run_day: дата, на яку потрібно вивести результат. По замовчуванню - поточна дата.
    :return: None
    """
    date_dict = empty_dates(run_day)
    for user in users:
        bday = datetime.datetime.strptime(user['birthday'], '%d.%m.%Y').date()
        for key, value in date_dict.items():
            if bday.month == key.month and bday.day == key.day:
                value.append(user['name'])

    print('Happy birthday next week!')
    for k, v in date_dict.items():
        print(f"{datetime.datetime.strftime(k, '%A')}: {', '.join(v) if v else '-'}")


def empty_dates(run_day: datetime) -> dict:
    """Допоміжна функція empty_dates(run_day: datetime) -> dict створює словник, ключами якого є найближчі 7 днів, а
    значеннями - порожні списки. В понеділок та неділю словник починається з минулої суботи, в інші дні - з поточного
    дня run_day.
    :param run_day: дата запуску програми
    :return: словник для обробки основною процедурою.
    """
    if run_day.weekday() == 0:
        begin_day = -2
    elif run_day.weekday() == 6:
        begin_day = -1
    else:
        begin_day = 0
    date_dict = {run_day + datetime.timedelta(days=i): [] for i in range(begin_day, begin_day + 7)}
    return date_dict
