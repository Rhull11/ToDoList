from modules import functions
import PySimpleGUI as gui

label = gui.Text("Type in a todo")
input_box = gui.InputText(tooltip="Enter todo", key="todo", expand_x=True)
add_todo_button = gui.Button("Add")
todos_box = gui.Listbox(values=functions.read_from_file(),
                        key="items",
                        enable_events=True,
                        size=(45, 10), expand_x=True, expand_y=True)
edit_button = gui.Button("Edit")
complete_button = gui.Button("Complete")
export_to_file_button = gui.Button("Export to file")

window = gui.Window("Todo App",
                    layout=[[todos_box],
                            [label],
                            [input_box],
                            [add_todo_button, edit_button, complete_button, export_to_file_button]],
                    font=("Helvetica", 15), resizable=True)

while True:
    event, values = window.read()
    match event:
        case "Add":
            todos = functions.read_from_file()
            todos.append(values["todo"] + "\n")
            functions.write_to_file(todos)
        case "Edit":
            todo_to_edit = values["items"][0]
            new_todo = values["todo"]
            todos = functions.read_from_file()
            todos[todos.index(todo_to_edit)] = new_todo
            functions.write_to_file(todos)
            window["items"].update(values=todos)
        case "items":
            window["todo"].update(value=values["items"][0])
        case gui.WIN_CLOSED:
            break

window.close()
