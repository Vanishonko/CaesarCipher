import PySimpleGUI as sg
import encrypt as enc

sg.theme("Dark Amber")

layout = [  [sg.Text("Key", font = "default 15 bold", k = "inputKey"), sg.Slider(range = (1, 25), font = "default 15", orientation = "horizontal", expand_x = True, tooltip = "Your desired key")],
            [sg.Text("Input your text", font = "default 20")],
            [sg.Multiline(font = "default 20", size = (None, 5), expand_y = True, expand_x = True, no_scrollbar = True)],
            [sg.Text("Output", font = "default 20")],
            [sg.Output(font = "default 20", size = (None, 5), expand_y = True, expand_x = True)],
            [sg.Button("Encode", font = "default 15 bold"), sg.Button("Decode", font = "default 15 bold"), sg.Button("Bruteforce", font = "default 15 bold"), sg.Button("Exit", font = "default 15 bold")]]

window = sg.Window('Caesar Cipher', layout, resizable = True)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Exit":
        break
    if event == "Encode":
        print(enc.encrypt(int(values[0]), values[1]))
    if event == "Decode":
        print(enc.decrypt(int(values[0]), values[1]))
    if event == "Bruteforce":
        print(enc.bruteforce(values[1]))

window.close()
