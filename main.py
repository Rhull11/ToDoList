from modules import functions
import time

print("\n--ToDo List App--")

now = time.strftime("%b %d, %Y %I:%M %p")
print("It is", now)
while True:
    user_input = input("\nOptions:\n"
                       "1 - Add a todo\n"
                       "2 - Edit a todo\n"
                       "3 - Complete a todo\n"
                       "4 - View todos\n"
                       "5 - Export to file\n"
                       "Type 'exit' to close program.\n\n").casefold().strip()

    if user_input.startswith("1"):
        todo = input("Add a todo: ")
        todos = functions.read_from_file()
        todos.append(todo + "\n")
        functions.write_to_file(todos)
        print("\nTodo added!\n")
        functions.print_todos(todos)
    elif user_input.startswith("2"):
        try:
            todos = functions.read_from_file()
            functions.print_todos(todos)
            edit_todo = int(input("Edit a todo: ")) - 1
            if len(todos) != 0:
                todos[int(edit_todo)] = input("Please make your changes: ") + "\n"
                functions.write_to_file(todos)
                print("\nUpdated todos:\n")
                functions.print_todos(todos)
            else:
                print("Please have a todo in the list to edit...")
        except ValueError:
            print("Not a valid option. Please type the todo's number.")
            continue
    elif user_input.startswith("3"):
        try:
            todos = functions.read_from_file()
            functions.print_todos(todos)
            remove_todo = input("Complete a todo. type 'all' to complete all todos: ").casefold().strip()
            if remove_todo == "all":
                todos.clear()
                functions.write_to_file(todos)
                print("All todos have been completed!")
            elif len(todos) != 0:
                todos.pop(int(remove_todo) - 1)
                functions.write_to_file(todos)
                print(f"\nTodo, {remove_todo} was removed from the list.")
            else:
                print("\nPlease have a todo in the list to remove...")
        except IndexError:
            print(f"\nTodo, {remove_todo} does not exist. Please choose a todo that exists.")
            continue
        except ValueError:
            print("\nPlease type in a number to complete the todo.")
    elif user_input.startswith("4"):
        print("View Todos:\n")
        todos = functions.read_from_file()
        functions.print_todos(todos)
    elif user_input.startswith("5"):
        todos = functions.read_from_file()
        export_choice = input("Export to File \n Choose a format to export to (type in 'cancel' to cancel): \n"
                              "1 - .csv\n"
                              "2 - .json\n"
                              "3 - .xls\n\n").casefold().strip()
        if export_choice == "cancel":
            continue
        elif export_choice == "1":
            functions.export_to_file(export_choice, todos)
        elif export_choice == "2":
            functions.export_to_file(export_choice, todos)
        elif export_choice == "3":
            functions.export_to_file(export_choice, todos)
        else:
            print("Export for file type is not found...")
    elif user_input.startswith("exit"):
        break
    else:
        print("Please choose a valid option...")