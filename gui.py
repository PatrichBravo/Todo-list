import functions
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText (tooltip="Enter todo", key="todo")
add_botton = sg.Button ("Add")
windows = sg.Window('My To-do App',
                    layout=[[label], [input_box,add_botton]],
                    font=('helvetica' , 20))

while True:
    event, values = windows.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
        case sg.WIN_CLOSED:
            break
    
windows.close() 