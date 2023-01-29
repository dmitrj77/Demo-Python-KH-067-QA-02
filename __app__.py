from __task__ import get_task_from_string, Task
from __task_creator__ import add_task_by_pattern, add_task_by_steps
from __init__ import tasks_path, delete_path, tasks, delete_tasks
from utils.__data_utils__ import DataUtils, get_local_data_time
from utils.__file_utils__ import create_if_not_exists, read_file, write_file

create_if_not_exists(tasks_path)
create_if_not_exists(delete_path)
for line in read_file(tasks_path):
    if line != 0:
        tasks.append(get_task_from_string(line))
for line in read_file(delete_path):
    if line != 0:
        delete_tasks.append(get_task_from_string(line))


def show_task(tasks_list):
    temp = list()
    temp.append(tasks_list)
    for task in temp:
        print(Task.to_string(task))


def show_tasks_by_id(tasks_list):
    i = 0
    while i < len(tasks_list):
        print(f"Id:{i}", Task.to_string(tasks_list[i]))
        i += 1


def get_correct_data():
    data = input()
    try:
        local_data_time = get_local_data_time(data)
    except ValueError as e:
        print(e)
    return local_data_time


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
    while True:
        if user_choice > max_choice:
            print("Pls input a correct number")
            user_choice = get_number()
        else:
            break
    return user_choice


def get_number():
    while type:
        outnumber = input()
        try:
            numberplate = int(outnumber)
        except ValueError:
            print('"' + outnumber + '"' + ' Not Number')
        else:
            break
    return abs(numberplate)


def write_tasks(file_path, tasks_list):
    string_list = list()
    for task in tasks_list:
        string_task = Task.get_string_for_file(task)
        string_list.append(string_task)
    write_file(file_path, string_list)


def run_precondition():
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
                    task = add_task_by_steps()
                    if task != 0:
                        tasks.append(task)
                        write_tasks(tasks_path, tasks)
                        print("Tasks created successfully")
                        print(Task.to_string(tasks[len(tasks) - 1]))
                        by_step_menu = ["Choose from the menus bellow", "Add task", "Main Menu"]
                        out_put_menu(by_step_menu)
                        user_choice = get_user_choice(max_choice=1)
                # Add task by pattern
                elif user_choice == 2:
                    task = add_task_by_pattern()
                    if task != 0:
                        tasks.append(task)
                        write_tasks(tasks_path, tasks)
                        print("Tasks created successfully")
                        print(Task.to_string(tasks[len(tasks) - 1]))
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
                    show_tasks_by_id(tasks)
                    print("Please enter Id: ")
                    user_choice_id = get_user_choice(len(tasks) - 1)
                    while user_choice != 0:
                        if len(tasks) == 0:
                            print("List of tasks is empty")
                        else:
                            show_task(tasks[user_choice_id])
                        edit_task = ["EXISTING", "Title ", "Date", "Description", "Back"]
                        out_put_menu(edit_task)
                        user_choice = get_user_choice(max_choice=3)
                        # Edit title
                        if user_choice == 1:
                            print("Please enter new Title: ")
                            new_title = get_input_string()
                            task = tasks[user_choice_id]
                            task.set_title(new_title)
                            show_tasks_by_id(tasks)
                            write_tasks(tasks_path, tasks)
                            print("You have successfully changed Title:\n")
                        # Edit data
                        elif user_choice == 2:
                            print("Please enter new Date in format " + DataUtils.format)
                            new_date = get_correct_data()
                            task = tasks[user_choice_id]
                            task.set_local_data_time(new_date)
                            show_tasks_by_id(tasks)
                            write_tasks(tasks_path, tasks)
                            print("You have successfully changed Date:\n")
                        # Edit description
                        elif user_choice == 3:
                            print("Please enter new Description: ")
                            new_description = get_input_string()
                            task = tasks[user_choice_id]
                            task.set_description(new_description)
                            show_tasks_by_id(tasks)
                            write_tasks(tasks_path, tasks)
                            print("You have successfully changed Description:\n")
                        elif user_choice == 0:
                            user_choice = 0
                        else:
                            print("Please make your choice")
                    user_choice = -1
                # Recycle bin menu
                if user_choice == 2:
                    if len(delete_tasks) == 0:
                        print("Archive is empty!")
                    else:
                        show_tasks_by_id(delete_tasks)
                    print("Please enter Id: ")
                    user_choice_id = get_user_choice(len(delete_tasks) - 1)
                    while user_choice != 0:
                        bin_menu = ["RECYCLE BIN", "Data", "Back"]
                        out_put_menu(bin_menu)
                        user_choice = get_user_choice(max_choice=1)
                        # Change of data
                        if user_choice == 1:
                            print("Please enter new Date in format " + DataUtils.format)
                            new_date = get_correct_data()
                            task = delete_tasks[user_choice_id]
                            task.set_local_data_time(new_date)
                            tasks.append(delete_tasks.pop(user_choice_id))
                            write_tasks(delete_path, delete_tasks)
                            write_tasks(tasks_path, tasks)
                            print("You have successfully changed Date:\n")
                            show_tasks_by_id(tasks)
                        elif user_choice == 0:
                            user_choice = 0
                        else:
                            print("Please make your choice")
                    user_choice = -1
                # Back menu
                elif user_choice == 0:
                    user_choice = 0
                else:
                    print("Please make correct choice")
            user_choice = -1
        # Showing tasks
        elif user_choice == 3:
            while user_choice != 0:
                showing_menu = ["SHOW TASK", "All tasks", "By period", "Deleted tasks", "Back"]
                out_put_menu(showing_menu)
                user_choice = get_user_choice(max_choice=3)
                # All tasks
                if user_choice == 1:
                    all_menu = ["ALL TASKS"]
                    out_put_menu(all_menu)
                    show_tasks_by_id(tasks)
                    menu = ["Choose from the menus bellow", "Show Task", "Main Menu"]
                    out_put_menu(menu)
                    user_choice = get_user_choice(max_choice=1)
                # By filter
                elif user_choice == 2:
                    by_filter_menu = ["BY PERIOD"]
                    out_put_menu(by_filter_menu)
                    temp = list()
                    print("Format of data: " + DataUtils.format)
                    print("From: ")
                    data_from = get_correct_data()
                    print("To: ")
                    data_to = get_correct_data()
                    for task in tasks:
                        task_data = task.get_local_data()
                        is_time_range = task_data == data_from or task_data == data_to or (
                                data_from < task_data < data_to)
                        if is_time_range:
                            temp.append(task)
                    if len(temp) != 0:
                        show_tasks_by_id(temp)
                    else:
                        print("Tasks from period not found")
                    menu = ["Choose from the menus bellow", "Show Task", "Main Menu"]
                    out_put_menu(menu)
                    user_choice = get_user_choice(max_choice=1)
                # Deleted tasks
                elif user_choice == 3:
                    deleted_menu = ["DELETED TASK"]
                    out_put_menu(deleted_menu)
                    show_tasks_by_id(delete_tasks)
                    menu = ["Choose from the menus bellow", "Show Task", "Main Menu"]
                    out_put_menu(menu)
                    user_choice = get_user_choice(max_choice=1)
                # Back from Showing tasks
                elif user_choice == 0:
                    user_choice = 0
                else:
                    print("Please make your choice")
            user_choice = -1
        # Delete menu
        elif user_choice == 4:
            while user_choice != 0:
                delete_menu = ["DELETE TASK", "By Id", "By period", "Back"]
                out_put_menu(delete_menu)
                user_choice = get_user_choice(max_choice=2)
                # Delete by Id
                if user_choice == 1:
                    by_id_menu = ["BY ID", "Back"]
                    out_put_menu(by_id_menu)
                    show_tasks_by_id(tasks)
                    print("Input ID: ")
                    id_task = get_user_choice(max_choice=len(tasks) - 1)
                    temp = list()
                    temp.append(tasks[id_task])
                    show_tasks_by_id(temp)
                    delete_tasks.append(tasks.pop(id_task))
                    write_tasks(delete_path, delete_tasks)
                    write_tasks(tasks_path, tasks)
                    print("You have successfully deleted task")
                    menu = ["Choose from the menus bellow", "Delete task", "Back"]
                    out_put_menu(menu)
                    get_user_choice(max_choice=1)
                # Delete by period
                elif user_choice == 2:
                    by_period_menu = ["BY PERIOD", "Back"]
                    out_put_menu(by_period_menu)
                    show_tasks_by_id(tasks)
                    print("Input period")
                    print("Format of data: " + DataUtils.format)
                    print("From: ")
                    data_from = get_correct_data()
                    print("To: ")
                    data_to = get_correct_data()
                    tasks_to_delete = list()
                    for task in tasks:
                        task_data = task.get_local_data()
                        is_time_range = task_data == data_from or task_data == data_to or (
                                data_from < task_data < data_to)
                        if is_time_range:
                            tasks_to_delete.append(task)
                    for task in tasks_to_delete:
                        delete_menu.append(task)
                    write_tasks(delete_path, delete_tasks)
                    write_tasks(tasks_path, tasks)
                    print("You have successfully deleted tasks")
                    menu = ["Choose from the menus bellow", "Delete task", "Back"]
                    out_put_menu(menu)
                    user_choice = get_user_choice(max_choice=1)
                # Back
                elif user_choice == 0:
                    user_choice = 0
                else:
                    print("Please make your choice")
            user_choice = -1
        # To Main menu
        elif user_choice == 0:
            user_choice = 0
        else:
            print("Please make correct choice")
    user_choice = -1


def get_input_string():
    while True:
        input_text = input()
        if len(input_text) == 0:
            print("Parameter can not be empty. Please try again")
        else:
            return input_text
