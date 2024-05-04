from datetime import datetime


def is_valid_iso(date_string):
    try:
        datetime.fromisoformat(date_string)
        return True
    except ValueError:
        return False


def not_valid_data():
    return 'Невалидный запрос. Пример запроса: \n{"dt_from": "2022-09-01T00:00:00", "dt_upto": "2022-12-31T23:59:00", "group_type": "month"}'

def not_valid_json():
    return 'Допустимо отправлять только следующие запросы: \n{"dt_from": "2022-09-01T00:00:00", "dt_upto": "2022-12-31T23:59:00", "group_type": "month"} \n{"dt_from": "2022-10-01T00:00:00", "dt_upto": "2022-11-30T23:59:00", "group_type": "day"} \n{"dt_from": "2022-02-01T00:00:00", "dt_upto": "2022-02-02T00:00:00", "group_type": "hour"}'
