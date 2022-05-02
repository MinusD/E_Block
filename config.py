# Запуск
WINDOW_TITLE = 'Валютный помощник'
WINDOW_SIZE = None  # '600x280'
WINDOW_FONT_SIZE = None

# Общее
PADX = 30  # Размер отступа по горизонтали
PADY = 10  # Размер отступа по вертикали
CBR_URL = 'https://cbr.ru/scripts/XML_daily.asp'  # Адрес на сайт ЦБ
RUBLE_SLUG = 'Российский рубль'
MONTHS_SLUGS = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь',
                'Ноябрь', 'Декабрь']
QUARTERS_SLUGS = ['I квартал', 'II квартал', 'III квартал', 'IV квартал']


# Конвертор валют
SORT_CURRENCY_LIST = False  # Сортировать ли рубль в списке
RANDOM_START_CURRENCY = True  # Выбирать ли случайную валюта при запуске
SET_INITIAL_VALUE = 1  # Значение или None
NOT_NUMERIC_VALUE_ERROR = 'Не является числом!'
NO_END_CURRENCY_SELECTED_ERROR = 'Не выбрана конечная валюта!'

# Динамика курса
RANDOM_CURRENCY = True  # Выбирать ли в начале случайную валюту
NUMBER_OF_PERIODS = 4
