from pathlib import Path
import csv
import sys
from get_birthdays.get_birthdays import get_birthdays_per_week


def start():
    if len(sys.argv) < 2:
        print('''
        Ви не зазначили обов'язковий параметр Source. Формат запуску:
        reminder Source.csv
        де Source.csv - файл з даними колег 
        ''')
        exit(0)

    if sys.argv[1]:
        data_file = Path(sys.argv[1])
        with open(data_file, encoding='utf-8-sig') as csvfile:
            users = list(csv.DictReader(csvfile, delimiter=';'))
        get_birthdays_per_week(users)
