# Програма для виведення списку днів народження на найближчий тиждень

### *Python 6 Core HomeWork 08*
[![Language](https://img.shields.io/badge/language-python-blue)](https://www.python.org)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/VlodyaKr/Python-6-Core-HomeWork-08)
![GitHub Release Date](https://img.shields.io/github/release-date/VlodyaKr/Python-6-Core-HomeWork-08?style=plastic)
![GitHub repo size](https://img.shields.io/github/repo-size/VlodyaKr/Python-6-Core-HomeWork-08?style=plastic)
![GitHub all releases](https://img.shields.io/github/downloads/VlodyaKr/Python-6-Core-HomeWork-08/total)
[![GitHub issues](https://img.shields.io/github/issues/VlodyaKr/Python-6-Core-HomeWork-08?style=plastic)](https://github.com/VlodyaKr/Python-6-Core-HomeWork-08/issues)
[![GitHub forks](https://img.shields.io/github/forks/VlodyaKr/Python-6-Core-HomeWork-08?style=plastic)](https://github.com/VlodyaKr/Python-6-Core-HomeWork-08/network)
[![GitHub stars](https://img.shields.io/github/stars/VlodyaKr/Python-6-Core-HomeWork-08?style=plastic)](https://github.com/VlodyaKr/Python-6-Core-HomeWork-08/stargazers)
___
#### Формат запуску з консолі:
#### ***`reminder Source.csv`***
де ***`Source.csv`*** - файл з даними колег,

в яком роздільник полів - `;` та обов'язкові поля: 

`name` - ім'я колеги,

`birthday` - дата у форматі `DD.MM.YYYY`.

Для прикладу можна взяти файл `test/test.csv`

___
#### Завдання:
Потрібно реалізувати корисну функцію для виведення списку колег, яких треба привітати з днем народження протягом тижня. 
У нас є список словників, кожен словник в ньому обов'язково має ключі `name` і `birthday`. Така структура представляє 
модель списку користувачів з їхніми іменами та днями народження. `name` - це рядок з ім'ям користувача, а `birthday` - 
це `datetime` об'єкт, в якому записано день народження. 
Задача: написати функцію `get_birthdays_per_week`, яка отримує на вхід список `users` та виводить у консоль (за 
допомогою `print`) список користувачів, яких треба привітати протягом тижня.
___
#### Розгортання
- Завантажте проєкт на локальний диск
- Розархівуйте завантажений архів 
- Встановіть пакет:
`pip install -e .`
___
#### Розгортання (варіант 2)
- Встановіть пакет:
`pip install -i https://test.pypi.org/simple/ get-birthdays==0.1.0`
___
#### Автор
[![GitHub Contributors Image](https://contrib.rocks/image?repo=VlodyaKr/Python-6-Core-HomeWork-08)](https://github.com/VlodyaKr)

#### Володимир Кравченко
[Написати автору листа](mailto:vlodya@gmail.com?subject=Python-6-Core-HomeWork-08)
___
#### Ліцензія
[![GitHub license](https://img.shields.io/github/license/VlodyaKr/Python-6-Core-HomeWork-08?style=plastic)](https://github.com/VlodyaKr/Python-6-Core-HomeWork-08/blob/main/LICENSE)

Цей проєкт ліцензується відповідно до ліцензії MIT — подробиці див. у файлі [LICENSE](https://github.com/VlodyaKr/Python-6-Core-HomeWork-08/blob/main/LICENSE)
