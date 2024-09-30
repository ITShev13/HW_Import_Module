# Вариант с импортом конкретных функций
from application.salary import calculate_salary
from application.db.people import get_employees
from application.file_excel.unloading_XL import unloading_empl


# вариант с импортом через *
from application.db.people import *
from application.salary import *
from application.file_excel.unloading_XL import *