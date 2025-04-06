import FreeSimpleGUI as sg
import functions as f

appname = "ToDo Application"

layout = [
    [sg.Text("Enter a to-do")],
    [sg.Input(k='new_todo', size=(100, 2))],
    [sg.Button('Add', size=(5, 1))],
    [sg.Listbox(values=f.get_todos(), size=(45, 10), pad=(5, 5), k='todo_list', enable_events=True), sg.Button('Edit')],
    [sg.Button('Close', size=(10, 1))]
]

window = sg.Window('Hello App', layout, font='Helvetica 20', size=(300, 200), resizable=True)

while True:
    event, values = window.read()
    match event:
        case "Add":
            todo = values['new_todo']
            f.add_todo(todo)
            window['todo_list'].update(values = f.get_todos())
        case "Edit":
            try:
                todo_to_edit = values['todo_list'][0]
                new_todo = values['new_todo']
                f.update_todo_index(todo_to_edit, new_todo)
                window['todo_list'].update(values = f.get_todos())
                sg.popup("Updated successfully")
            except IndexError:
                sg.popup("Please select a todo to edit")
        case "todo_list":
            try:
                selected_todo = values['todo_list'][0]
                window['new_todo'].update(selected_todo)
            except IndexError:
                pass
        case "Close":
            break

window.close()

# foula.py