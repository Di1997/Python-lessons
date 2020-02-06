import os


def get_file_dir(file_name: str) -> str:
    return os.path.join(os.getcwd(), "files", file_name + ".txt")


def read_file_by_name(file_name: str) -> list:
    with open(get_file_dir(file_name)) as file:
        return file.readlines()


def hw_read(file_name: str) -> list:
    return read_file_by_name(file_name)
