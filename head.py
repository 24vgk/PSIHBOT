from datetime import date


def day():
    # Выводит сегодняшнюю дату
    x = str(date.today())
    d = x[8:] + '.' + x[5: 7] + '.' + x[: 4]
    return d


def day_old():
    # Выводит сегодняшнюю дату
    x = str(date.today())
    d = x[8:] + '.' + x[5: 7] + '.' + x[: 4]
    return d


# TOKEN = '' # Продуктив БОТ
TOKEN = '5277442787:AAFHBMpjAZddToduAJUuDzVbSEhReWGxWPY' # Бот для проверки!
