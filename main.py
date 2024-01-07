import PySimpleGUI as sg

# Define the window's contents
layout = [[sg.Text("K"), sg.DropDown("y=kx+b, y=gb", size=10)],
          [sg.Input(key='-INPUTK-', values=''), sg.Input(key='-INPUTX-'), sg.Input(key='-INPUTB-')],
          [sg.Button('submit')]]

# Create the window
window = sg.Window('Window Title', layout)

# Display and interact with the Window using an Event Loop
while True:
    event, values = window.read()
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED:
        break
    # Output a message to the window
    print(values['-INPUTX-'])
    
# Finish up by removing from the screen
window.close()