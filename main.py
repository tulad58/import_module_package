from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import datetime


def get_datetime_now():
    return datetime.now()

if __name__ == '__main__':
    print(get_employees())
    print(calculate_salary())
    print(get_datetime_now())
