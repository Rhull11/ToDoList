# Todo List
A simple todo list application to manage your daily tasks.

Todos are saved and retrieved from a plain text file in files/todos.txt.

## Windows Installation
Download the [TodoApp.msi](https://github.com/Rhull11/ToDoList/releases/download/windows/TodoApp.msi) installer </br>

## Mac OS Installation
First, download for [Mac OS](https://github.com/Rhull11/ToDoList/releases/download/macos/TodoApp.dmg) </br></br>
After moving the app to your Applications folder, open a terminal there and type: </br>
```zsh
# clears all attributes to run this app
$ xattr -c <path/to/Todo.app>
```
When an application gets downloaded from any source other than those that Apple approves, the application gets an extended attribute "com.apple.Quarantine". The command above removes this attribute so the app can run. Otherwise, you get an "Todo.app is damaged and can’t be opened. You should move it to the trash" error.
