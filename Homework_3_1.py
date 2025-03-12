from datetime import datetime


def get_days_from_today(date):
    try:
        get_date = datetime.strptime(date, "%Y-%m-%d")
        current_date = datetime.today()
        diff_day = current_date - get_date
        return diff_day.days
    except ValueError:
        return "Неправильний формат вхідних даних для дати. Необхідно ввести 'YYYY-MM-DD'"


print(get_days_from_today("2025-02-10"))