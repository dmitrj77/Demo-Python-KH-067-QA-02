from datetime import datetime


def get_string_format(data_object):
    return data_object.strftime(DataUtils.format)


def get_local_data_time(data_time):
    while True:
        try:
            data_object = datetime.strptime(data_time, DataUtils.format)
            break
        except ValueError as e:
            print('This line has a problem:', e)
        data_time = input()
    return data_object


class DataUtils:
    format = "%d.%m.%Y %H:%M"
