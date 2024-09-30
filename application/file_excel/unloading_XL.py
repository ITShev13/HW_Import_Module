from openpyxl import Workbook
from openpyxl.styles import Font
from datetime import datetime, date


def unloading_empl (): # выгрузка конкретным бухгалтером данных о сотруднике из БД
    wb = Workbook() # создаем книгу excel
    wsa = wb.active # попадаем в активный лист
    style = Font(name='Times New Roman', size=16)
    style_accounted = Font(name='Times New Roman', size=16, color='0070C0')
    wsa['A5'] = 'name_employee' # имя сотрудника (можно брать из БД)
    wsa['B5'] = 'surname_employee' # фамилия сотрудника (можно брать из БД)
    wsa['A7'] = f'name surname accountant and {date.today()}' # ФИО бухгалтера (возможно использовать зарегистрированного пользователя)
    wsa['A5'].font = style
    wsa['B5'].font = style
    wsa['A7'].font = style_accounted
    wsa.column_dimensions['A'].width = 52
    wsa.column_dimensions['B'].width = 40
    wb.save('employee.xlsx') # сохраняем файл excel
    return 'Создан файл .excel'

if __name__ == '__main__': # для проверки запускаемого файла и предотвращения исполнения кода в данном файле
    unloading_empl()


