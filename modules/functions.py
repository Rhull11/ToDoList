import csv
import json

from xlwt import Workbook

FILEPATH = "todos.txt"

def print_todos(items):
    """Prints the list of todos"""
    for index, item in enumerate(items):
        item = item.strip('\n')
        print(f"{index + 1}-{item}")


def export_to_excel(filepath, items):
    """Exports todos to .xls file"""
    wb = Workbook()
    sheet = wb.add_sheet("Todos 1", cell_overwrite_ok=True)
    for i in range(0, len(items)):
        sheet.write(i, 0, items[i])
    wb.save(filepath)


def export_to_json(filepath, items):
    with open(filepath, 'w') as file:
        json.dump(items, file)


def export_to_csv(filepath, items):
    with open(filepath, 'w') as file:
        writer = csv.writer(file)
        writer.writerow(items)


def read_from_file(filepath=FILEPATH):
    """Reads todos from .txt file"""
    with open(filepath, 'r') as file:
        items = file.readlines()
    return items


def write_to_file(items, filepath=FILEPATH):
    """Writes todos to .txt file"""
    with open(filepath, 'w') as file:
        file.writelines(items)

