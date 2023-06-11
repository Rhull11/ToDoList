from modules import functions
import PySimpleGUI as gui

label = gui.Text("Type in a todo")
input_box = gui.InputText(tooltip="Enter todo", key="todo")
add_todo_button = gui.Button("Add")

window = gui.Window("Todo App",
                    layout=[[label], [input_box, add_todo_button]],
                    font=("Helvetica", 15))

while True:
    event, values = window.read()
    match event:
        case "Add":
            todos = functions.read_from_file()
            todos.append(values["todo"] + "\n")
            functions.write_to_file(todos)
        case gui.WIN_CLOSED:
            break

window.close()
