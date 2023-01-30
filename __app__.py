import __task__
import __task_creator__
from __init__ import tasks_path, delete_path, tasks, delete_tasks
from utils import __file_utils__, __data_utils__
from utils.__data_utils__ import DataUtils
from utils.__file_utils__ import create_if_not_exists, read_file, FileUtils

create_if_not_exists(tasks_path)
create_if_not_exists(delete_path)
for line in read_file(tasks_path):
    if line != 0:
        tasks.append(__task__.get_task_from_string(line))
for line in read_file(delete_path):
    if line != 0:
        delete_tasks.append(__task__.get_task_from_string(line))


def show_task(tasks_list):
    temp = list()
    temp.append(tasks_list)
    for task in temp:
        print(__task__.Task.to_string(task))


def show_task_by_id(tasks_list):
    i = 0
    while i < len(tasks_list):
        print(f"ID: {i}", __task__.Task.to_string(tasks_list[i]))
        i += 1


def et_correct_data():

    def out_put_menu(menu):
    list_menu = list(menu)
    i = 0
    while i < len(list_menu):
        if i == 0:
            print(list_menu[0])
            i += 1
        elif i < len(list_menu) - 1:
            print(f"[{i}] " + list_menu[i])
            i += 1
        else:
            print("[0] " + list_menu[i])
            i += 1


def get_user_choice(max_choice):
    user_choice = get_number()
    while user_choice > max_choice:
        if user_choice > max_choice:
            print("Pls input a correct number")
            user_choice = input()
    return user_choice


def get_number():
    while type:
        outnumber = input()
        try:
            numberplate = int(outnumber)
        except ValueError:
            print('"' + outnumber + '"' + 'Not Number')
        else:
            break
    return abs(numberplate)





def write_tasks(file_path):
    string_list = list()
    for task in tasks:
        string_task = task.get_string_for_file(task)
        string_list.append(string_task)
        __file_utils__.write_file(file_path, string_list)


def get_correct_data():
    data = input()
    while True:
        try:
            local_data_time = __data_utils__.get_local_data_time(data)
            break
        except ValueError as e:
            print("Incorrect format of data. Please try again. Correct format: " + DataUtils.format)

        data = input()
    return local_data_time


def run_precondition():
    for task_string in __file_utils__.read_file(tasks_path):
        task = __task__.get_task_from_string(task_string)
        tasks.append(task)

    for task_string in __file_utils__.read_file(delete_path):
        task = __task__.get_task_from_string(task_string)
        delete_tasks.append(task)

    print("[Organizer] is designed to schedule user's activity. "
          + "It was created by KH-JAVA-067-QA-01 team."
          + "\nIt has a console implementation and allows you to create, edit, view, delete and restore tasks."
          + "\nTo use the application please choose a number from the menu and follow the prompts."
          + "\nEnjoy :)")


def run():
    user_choice = -1
    while user_choice != 0:
        main_menu = ["MAIN MENU", "Add task", "Edit Task", "Show tasks", "Delete task", "Quit"]
        out_put_menu(main_menu)
        user_choice = get_user_choice(max_choice=4)
        # Add task menu
        if user_choice == 1:
            while user_choice != 0:
                add_menu = ["ADD TASK", "By step", "By pattern", "Back"]
                out_put_menu(add_menu)
                user_choice = get_user_choice(max_choice=2)
                # Add task by steps menu
                if user_choice == 1:
                    task = __task_creator__.add_task_by_steps()
                    if task != 0:
                        tasks.append(task)
                        write_tasks(tasks_path)
                        print("Tasks created successfully")
                        print(task.to_string(tasks[len(tasks) - 1]))
                        by_step_menu = ["Choose from the menus bellow", "Add task", "Main Menu"]
                        out_put_menu(by_step_menu)
                        user_choice = get_user_choice(max_choice=1)
                # Add task by pattern
                elif user_choice == 2:
                    task = __task_creator__.add_task_by_pattern()
                    if task != 0:
                        tasks.append(task)
                        write_tasks(tasks_path)
                        print("Tasks created successfully")
                        print(task.to_string(tasks[len(tasks) - 1]))
                        by_step_menu = ["Choose from the menus bellow", "Add task", "Main Menu"]
                        out_put_menu(by_step_menu)
                        user_choice = get_user_choice(max_choice=1)
                    # Cancel
                elif user_choice == 0:
                    user_choice = 0
                else:
                    print("Please make correct choice")

            user_choice = -1

        # Edit task menu
        elif user_choice == 2:
            while user_choice != 0:
                edit_menu = ["EDIT TASK", "Existing ", "Restore task", "Back"]
                out_put_menu(edit_menu)
                user_choice = get_user_choice(max_choice=2)
                # Existing task menu
                if user_choice == 1:
                    show_task(tasks)
                    print("Please enter Id: ")
                    user_choice_id = get_user_choice(len(tasks) - 1)
                    while user_choice != 0:
                        print(task[user_choice_id])
                        edit_task = ["EXISTING", "Title ", "Date", "Description", "Back"]
                        out_put_menu(edit_task)
                        user_choice = get_user_choice(max_choice=3)
                        if user_choice == 1:
                            print("Please enter new Title: ")
                            new_title = get_input_string()
                            task[user_choice_id].__task__.set_title(new_title)
                            print("Please enter new Title: ")
                        elif user_choice == 2:
                            print("Please enter new Date in format " + DataUtils.format)
                            new_date = get_correct_data()
                            tasks[user_choice_id].__task__.set_local_data_time(new_date)
                            print("You have successfully changed Date:\n")

            pass

        # Showing tasks
        elif user_choice == 3:
            pass

        # Delete menu
        elif user_choice == 4:

            pass
        # Cancel

        elif user_choice == 0:
            user_choice = 0
        else:
            print("Please make correct choice")


def get_input_string():
    while True:
        input_text = input()
        if len(input_text) == 0:
            print("Parameter can not be empty. Please try again")
        else:
            return input_text
