import FreeSimpleGUI as sg
import functions as f

appname = "ToDo Application"

sg.theme('DarkAmber')  # Add a touch of color
layout = [
    [sg.Text("", key="clock", font=("Helvetica", 20))],
    [sg.Text("Enter a to-do")],
    [sg.Input(k='new_todo', size=(100, 2))],
    [sg.Button('Add', size=(8, 1))],
    [sg.Button('Complete', size=(8, 1))],
    [sg.Listbox(values=f.get_todos(), size=(45, 10), pad=(5, 5), k='todo_list', enable_events=True), sg.Button('Edit')],
    [sg.Button('Close', size=(10, 1))],
    [sg.Button('Exit', size=(10, 1))]
]

window = sg.Window('Hello App', layout, font='Helvetica 20', size=(300, 200), resizable=True)

while True:
    event, values = window.read(timeout=100)
    window['clock'].update(value=f.time().strftime("%b %d, %Y %H:%M:%S"))
    match event:
        case "Add":
            try:
                todo = values['new_todo']
                f.add_todo(todo)
                window['todo_list'].update(values = f.get_todos())
            except ValueError:
                sg.popup("Please enter a valid todo")
        case "Edit":
            try:
                todo_to_edit = values['todo_list'][0]
                new_todo = values['new_todo']
                f.update_todo_index(todo_to_edit, new_todo)
                window['todo_list'].update(values = f.get_todos())
                sg.popup("Updated successfully", font=("Helvetica", 20))
            except IndexError:
                sg.popup("Please select a todo to edit")
        case "Complete":
            try:
                todo_to_complete = values['todo_list'][0]
                todos = f.get_todos()
                todos.remove(todo_to_complete)
                f.write_todos(todos)
                window['todo_list'].update(values = todos)
                window['new_todo'].update(value="")
            except IndexError:
                sg.popup("Please select a todo to complete")
        case "todo_list":
            try:
                selected_todo = values['todo_list'][0]
                window['new_todo'].update(selected_todo)
            except IndexError:
                pass
        case "Exit":
            break
        case "Close":
            break
            # exit()

window.close()

# foula.py