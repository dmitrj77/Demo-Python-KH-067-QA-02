import __app__
from __task__ import Task, get_task_from_string
from utils.__data_utils__ import DataUtils, get_local_data_time


def add_task_by_steps():
    print("Enter title")
    title = __app__.get_input_string()
    print("Enter data in format: " + DataUtils.format)
    date = input()
    local_date_time = __app__.get_compare_data(date)
    print("Enter description")
    description = __app__.get_input_string()
    return Task(title, local_date_time, description)


def add_task_by_pattern():
    while True:
        print("Enter title, data (in format " + DataUtils.format + ") and description using delimiter ';'")
        pattern = __app__.get_input_string()
        if TaskCreator.is_string_valid(pattern):
            return get_task_from_string(pattern)
        else:
            print("Try again")


class TaskCreator:
    @classmethod
    def is_string_valid(cls, pattern):
        task_fields = pattern.split(";")
        if len(task_fields) < 3:
            print("Error! Incorrect pattern")
            return False
        elif get_local_data_time(task_fields[1]):
            return True
        else:
            return False
