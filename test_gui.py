import PySimpleGUI as sg

layout = [[sg.Text("What's your name?")],
          [sg.Input()],
          [sg.Button('OK')]]

window = sg.Window('Hello App', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'OK':
        break

window.close()