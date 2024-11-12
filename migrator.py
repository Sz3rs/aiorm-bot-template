"""
Это мигратор для того, чтобы добавлять в базу данных новые колонки
"""
from models import *
from peewee import Model, OperationalError, SchemaManager, Database
from utils.db_api import db

COLORS = {
    'GREEN': '\033[32m',
    'BLUE': '\033[34m',
    'YELLOW': '\033[33m',
    'RED': '\033[31m',
    'RESET': '\033[0m',
}


def colored_print(text: str, color: str):
    print(f"{COLORS[color]}{text}{COLORS['RESET']}")


def get_model_class(model_name):
    """Возвращает класс модели по имени."""
    try:
        return globals()[model_name]
    except KeyError:
        print(f"Ошибка: модель с именем '{model_name}' не найдена.")
        return None


colored_print('Это мигратор. Он нужен для того, чтобы добавлять в вашу базу новые колонки: '
      'добавьте их сначала в модель, а потом запустите мигратор\n', 'BLUE')

model_name = input('Введите название модели, в которой появилась новая колонка: ')

model_class: Model
model_class = get_model_class(model_name)

if not model_class:
    colored_print('Не удалось загрузить модель. Проверьте правильность введенного имени.', 'RED')
    exit()

try:
    row = model_class.select().first()
    colored_print('Все и так в порядке!', 'GREEN')
    exit()
except OperationalError as e:
    missing_variable = str(e).split('no such column: t1.')[1]  # balance

    colored_print(f'Нужно добавить {missing_variable}', 'BLUE')

    column = getattr(model_class, missing_variable)

    full_query: str
    full_query = str(SchemaManager(model_class)._create_table().query()[0])
    end = ''
    if full_query[-1] == ')':
        full_query = full_query[:-1]

    query = full_query.split(f'"{missing_variable}"')[1].split(',')[0]
    query = missing_variable + query

    ctx = SchemaManager(model_class)._create_context()

    model_sql_name = ctx.sql(model_class).literal(' ').query()[0].strip()

    sql = f'ALTER TABLE {model_sql_name} ADD COLUMN {query}'

    default_column = ' DEFAULT '
    if column.default is not None:
        if column.default in [False, True]:
            default_column += '0' if column.default == False else '1'
        else:
            default_column += column.default
    else:
        default_column += 'NULL'

    sql += default_column
    sql += end
    colored_print(sql, 'YELLOW')

    q = input('Выполнить запрос? Y/n: ')
    if q.lower() != 'y':
        colored_print('Ок, выходим', 'YELLOW')
        exit()

    db.execute_sql(sql)

    colored_print('Готово!', 'GREEN')

