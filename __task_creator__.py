import __app__
import __task__
from __task__ import Task
from utils import __data_utils__
from utils.__data_utils__ import DataUtils, get_local_data_time


def add_task_by_steps():
    print("Enter title")
    title = __app__.get_input_string()
    print("Enter data in format: " + DataUtils.format)
    data = input()
    local_date_time = __data_utils__.get_local_data_time(data)
    print("Enter description")
    description = __app__.get_input_string()
    return Task(title, local_date_time, description)


def add_task_by_pattern():
    while True:
        print("Enter title, data (in format " + DataUtils.format + ") and description using delimiter ';'")
        pattern = __app__.get_input_string()
        if TaskCreator.is_string_valid(pattern):
            return __task__.get_task_from_string(pattern)
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
