import csv
import json

from xlwt import Workbook

FILEPATH = "files/todos.txt"

def print_todos(items):
    """Prints the list of todos"""
    for index, item in enumerate(items):
        item = item.strip('\n')
        print(f"{index + 1}-{item}")


def export_to_file(filetype, items):
    """Exports todos into .csv, .json, or .xls file formats"""
    filepath = input("Export to File \nPlease specify the file path to save to: ")
    if filetype.startswith("1"):
        with open(filepath, 'w') as file:
            writer = csv.writer(file)
            writer.writerow(items)
    elif filetype.startswith("2"):
        with open(filepath, 'w') as file:
            json.dump(items, file)
    elif filetype.startswith("3"):
        wb = Workbook()
        sheet = wb.add_sheet("Todos 1", cell_overwrite_ok=True)
        for i in range(0, len(items)):
            sheet.write(i, 0, items[i])
        wb.save(filepath)
    else:
        print("Export for file type is not found...")


def read_from_file(filepath=FILEPATH):
    """Reads todos from .txt file"""
    with open(filepath, 'r') as file:
        items = file.readlines()
    return items


def write_to_file(items, filepath=FILEPATH):
    """Writes todos to .txt file"""
    with open(filepath, 'w') as file:
        file.writelines(items)


if __name__ == "__main__":
    print("Hello from functions")
