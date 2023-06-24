from modules import functions
import PySimpleGUI as gui

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

window = gui.Window("Todo App",
                    layout=[[todos_box],
                            [label],
                            [input_box],
                            [add_todo_button, edit_button, complete_button, export_to_file_button]],
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


while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.read_from_file()
            todos.append(values["todo"] + "\n")
            functions.write_to_file(todos)
            window["items"].update(values=todos)
        case "Edit":
            todo_to_edit = values["items"][0]
            new_todo = values["todo"]
            todos = functions.read_from_file()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_to_file(todos)
            window["items"].update(values=todos)
        case "Complete":
            remove_todo = values["items"][0]
            todos = functions.read_from_file()
            todos.pop(todos.index(remove_todo))
            functions.write_to_file(todos)
            window["items"].update(values=todos)
        case "Export to file":
            todos = functions.read_from_file()
            save_to_file(todos)
        case "items":
            window["todo"].update(value=values["items"][0])
        case gui.WIN_CLOSED:
            break

window.close()
