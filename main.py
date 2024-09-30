from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import datetime, date
from application.file_excel.unloading_XL import unloading_empl


if __name__ == '__main__':
    datetime_date = datetime.today().date() # вариант с использованием модуля datetime е(сли в дальнейшем будет использоваться и время)
    # datetime_date = datetime.now().date() # еще вариант возврата даты
    date_date = date.today() # вариант с использованием модуля date (если нужно только дату без времени)
    print(datetime_date)
    print(date_date)

    print(calculate_salary())
    print(get_employees())
    print(unloading_empl())


