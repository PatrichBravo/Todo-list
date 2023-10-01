#import functions
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
imput_box = sg.InputText (tooltip="Enter todo")
add_botton = sg.Button ("Add")
windows = sg.Window('My To-do App', layout=[[label], [imput_box,add_botton]])

windows.read()
windows.close() 