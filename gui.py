from modules import functions
import PySimpleGUI as gui
import time
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass

clock = gui.Text("", key="clock")
label = gui.Text("Type in a todo")
input_box = gui.InputText(tooltip="Enter todo", key="todo", expand_x=True)
add_todo_button = gui.Button("Add")
todos_box = gui.Listbox(values=functions.read_from_file(),
                        key="items",
                        enable_events=True,
                        size=(65, 15), expand_x=True, expand_y=True)
edit_button = gui.Button("Edit")
complete_button = gui.Button("Complete")
export_to_file_button = gui.Button("Export to file")
settings_button = gui.Button("Settings")
exit_button = gui.Button("Exit")
refresh_button = gui.Button("Refresh")

window = gui.Window("Todo App",
                    layout=[[clock],
                            [todos_box],
                            [label],
                            [input_box],
                            [add_todo_button, edit_button, complete_button,
                             settings_button, refresh_button, exit_button]],
                    font=("Helvetica", 15), resizable=True)


def save_to_file(list_box_items):
    """Window popup to save file"""
    layout = [[gui.Text('Choose a file type'),
               gui.Button(".csv"),
               gui.Button(".json"),
               gui.Button(".xls")]]
    file_window = gui.Window('File Type', layout, finalize=True, font=("Helvetica", 15))

    file_event, file_values = file_window.read()

    match file_event:
        case ".xls":
            functions.export_to_excel("files/todos.xls", list_box_items)
        case ".csv":
            functions.export_to_csv("files/todos.csv", list_box_items)
        case ".json":
            functions.export_to_json("files/todos.json", list_box_items)

    file_window.close()


def open_themes_popup():
    themes = gui.theme_list()
    layout = [[[gui.Text('Choose a Theme')],
              gui.Combo(themes, key="-THEMES-", enable_events=True)]]
    themes_window = gui.Window('Themes', layout, font=("Helvetica", 15))

    while True:
        themes_event, themes_values = themes_window.read()
        print(themes_values)
        if themes_event == gui.WIN_CLOSED:
            break
        gui.theme(themes_values["-THEMES-"][0])

    themes_window.close()


def open_settings_popup(list_box_items):
    layout = [[gui.Button("Export to File"),
              gui.Button("Themes"),
              gui.Button("About")]]
    settings_window = gui.Window('Settings', layout, font=("Helvetica", 15))

    while True:
        settings_event, settings_value = settings_window.read()
        match settings_event:
            case "Export to File":
                save_to_file(list_box_items)
            case "Themes":
                open_themes_popup()
            case "About":
                gui.popup("Todo List app \n\n R.Hull \n\n 2023", font=("Helvetica", 15), title="About")
            case gui.WIN_CLOSED:
                break

    settings_window.close()


while True:
    event, values = window.read(timeout=200)
    window["clock"].update(value=time.strftime("%b %d, %Y %I:%M %p"))
    match event:
        case "Add":
            todos = functions.read_from_file()
            todos.append(values["todo"] + "\n")
            functions.write_to_file(todos)
            window["items"].update(values=todos)
        case "Edit":
            try:
                todo_to_edit = values["items"][0]
                new_todo = values["todo"]
                todos = functions.read_from_file()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_to_file(todos)
                window["items"].update(values=todos)
                window["warning_message"].update(value="")
            except IndexError:
                gui.popup("Please select a todo", font=("Helvetica", 15))
        case "Complete":
            try:
                remove_todo = values["items"][0]
                todos = functions.read_from_file()
                todos.pop(todos.index(remove_todo))
                functions.write_to_file(todos)
                window["items"].update(values=todos)
                window["todo"].update(value="")
            except IndexError:
                gui.popup("Please select a todo", font=("Helvetica", 15))
        case "Settings":
            todos = functions.read_from_file()
            open_settings_popup(todos)
        case "Refresh":
            window.refresh()
        case "items":
            window["todo"].update(value=values["items"][0])
        case "Exit":
            window.close()
        case gui.WIN_CLOSED:
            break

window.close()

if __name__ == "__main__":
    print("Hello from functions")
