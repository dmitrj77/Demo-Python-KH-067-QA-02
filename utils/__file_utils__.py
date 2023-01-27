class FileUtils:
    message = list()


def create_if_not_exists(file_path):
    try:
        file = open(file_path, "a")
        try:
            file.read(file_path)
        except Exception as e:
            print(e)
        finally:
            file.close()
    except Exception as ex:
        print(ex)


def read_file(file_path):
    with open(file_path, "r", encoding='utf-8') as file:
        file_list = list()
        lines = file.readlines()
        for line in lines:
            if line != "\n":
                file_list.append(line)
            else:
                continue
    return file_list


def write_file(file_path, string_list):
    with open(file_path, "w") as file:
        for line in string_list:
            file.write(f'{line}\n')
