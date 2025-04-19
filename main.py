import FreeSimpleGUI as sg
 
 
def km_to_miles(km):
    result = float(km) / 1.6
    return result
 
 
label = sg.Text("Kilometers: ")
input_box = sg.InputText(tooltip="Enter km", key="kms")
miles_button = sg.Button("Convert")
 
output = sg.Text(key="output")
 
 
window = sg.Window('Km to Miles Converter',
                   layout=[[label, input_box], [miles_button, output]],
                   font=('Helvetica', 20))
 
while True:
    event, values = window.read()
    match event:
        case "Convert":
            km = values["kms"]
            result = km_to_miles(km)
            window['output'].update(value=result)
        case sg.WIN_CLOSED:
            break
 
window.close()