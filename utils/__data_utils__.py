from datetime import datetime


def get_string_format(data_object):
    return data_object.strftime(DataUtils.format)


def get_local_data_time(data_time):
    try:
        data_object = datetime.strptime(data_time, DataUtils.format)
        return data_object
    except ValueError as e:
        print('This line has a problem:', e)


class DataUtils:
    format = "%d.%m.%Y %H:%M"
