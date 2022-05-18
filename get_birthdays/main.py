from pathlib import Path
import csv
import sys
from get_birthdays.get_birthdays import get_birthdays_per_week
# from get_birthdays import get_birthdays_per_week


# if __name__ == '__main__':
def start():
    output_mode = '0'
    if len(sys.argv) < 2:
        print('''
        Ви не зазначили обов'язковий параметр Source. Формат запуску:
        reminder Source.csv [output_mode=0]
        де Source.csv - файл з даними колег,
        output_mode - форма виведення:
         0 - виведення починається з поточного дня (gj pfvjdxedfyy.),
         1 - виведення починається з наступного понеділка (в понеділок - з поточного дня),
         2 - виведення починається з поточного дня (в понеділок та неділю - з минулої суботи)
        ''')
        exit(0)

    if len(sys.argv) > 2 and sys.argv[2] in ('1', '2'):
        output_mode =sys.argv[2]

    if sys.argv[1]:
        data_file = Path(sys.argv[1])
        with open(data_file, encoding='utf-8-sig') as csvfile:
            users = list(csv.DictReader(csvfile, delimiter=';'))
        get_birthdays_per_week(users, output_mode)
