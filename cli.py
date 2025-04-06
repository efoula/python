import FreeSimpleGUI as sg
import zip_creator as zip

appname = "Files to Compress"

inputfiletext = sg.Text("Files to compress")
inputfile = sg.Input()
choosefile = sg.FilesBrowse("Choose", key="files")

inputcomptext = sg.Text("Destination to compress")
inputcomp = sg.Input()
choosecomp = sg.FolderBrowse("Choose", key="folder")

output_label = sg.Text(key="output")
compressbutton = sg.Button("Compress")

window = sg.Window(appname, layout=[[inputfiletext, inputfile, choosefile],[inputcomptext, inputcomp, choosecomp],[compressbutton]])

while True:
    event, values = window.read()
    filepaths = values['files'].split(";")
    folder = values['folder']
    zip.make_archive(filepaths, folder)
    window["output"].update(value="Files compressed successfully")


window.close()

# sg.window('Hello App', 'Hello World!', 'OK', 'What\'s your name?')
# Define the window's contents
# layout = [[sg.Text("What's your name?")],
#           [sg.Input(key='-INPUT-')],
#           [sg.Text(size=(40,1), key='-OUTPUT-')],
#           [sg.Button('Ok'), sg.Button('Quit')]]

# # Create the window
# window = sg.Window('Window Title', layout)

# # Display and interact with the Window using an Event Loop
# while True:
#     event, values = window.read()
#     # See if user wants to quit or window was closed
#     if event == sg.WINDOW_CLOSED or event == 'Quit':
#         break
#     # Output a message to the window
#     window['-OUTPUT-'].update('Hello ' + values['-INPUT-'] + "! Thanks for trying FreeSimpleGUI")

# # Finish up by removing from the screen
# window.close()