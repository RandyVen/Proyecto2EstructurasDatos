
from neo4j import GraphDatabase
from Database import Database
from Classes.Career import *
import tkinter as tk

uri = "bolt://localhost:7687"

driver = GraphDatabase.driver(uri, auth=("neo4j", "password"))
db = Database("bolt://localhost:7687", "neo4j", "password")

career_name = "Prueba"

# Prueba para crear a base de datos.
db.deleteCareer(career_name)

nodeType1 = "Clase"
nodeType2 = "Persona"
nodeType3 = "gusto"

materias = []
personas = []
hobbies = []

# Prueba para obtener todos de un tipo
result1 = db.getAllType(nodeType1)
for record in result1:
    materias.append(record[0]["nombre"])

result2 = db.getAllType(nodeType2)
for record in result2:
    personas.append(record[0]["nombre"])

result3 = db.getAllType(nodeType3)
for record in result3:
    hobbies.append(record[0]["nombre"])

root = tk.Tk()
root.geometry('700x700')
root.title("UVG - Recomendacion de Carreras")

preguntas_dict = {0: [],
                  1: [],
                  2: []}

preguntas_list = ["En cual de las siguientes materias consideras que tienes un mejor desempeño",
                  "A cual de las siguientes figuras publicas le tienes mayor admiracion ",
                  "Cual de los siguientes pasatiempos es el que mas disfrutas hacer"]

preguntas_dict[0] = materias
preguntas_dict[1] = personas
preguntas_dict[2] = hobbies

res = []
answers_list = []

index = tk.IntVar()
resp_var = tk.StringVar()

global final_txt
final_txt = tk.Label(text="", font="arial 18")
final_txt.place(x=25, y=250)

global label
label = tk.Label(text=preguntas_list[0], font="arial 12")
label.place(x=-50, y=-50)

global welcome
welcome = tk.Label(text="Presiona el boton de inicio para comenzar", font="arial 14 bold")
welcome.place(x=150, y=120)

global radio1
radio1 = tk.Radiobutton(variable=resp_var)
radio1.place(x=-50, y=-50)

global radio2
radio2 = tk.Radiobutton(variable=resp_var)
# radio2 = tk.Radiobutton(text=preguntas_dict[0][1], variable=resp_var, value=preguntas_dict[0][1])
radio2.place(x=-50, y=-50)

global radio3
radio3 = tk.Radiobutton(variable=resp_var)
# radio3 = tk.Radiobutton(text=preguntas_dict[0][2], variable=resp_var, value=preguntas_dict[0][2])
radio3.place(x=-50, y=-50)

global radio4
radio4 = tk.Radiobutton(variable=resp_var)
# radio4 = tk.Radiobutton(text=preguntas_dict[0][3], variable=resp_var, value=preguntas_dict[0][3])
radio4.place(x=-50, y=-50)

global radio5
radio5 = tk.Radiobutton(variable=resp_var)
# radio5 = tk.Radiobutton(text=preguntas_dict[0][4], variable=resp_var, value=preguntas_dict[0][4])
radio5.place(x=-50, y=-50)

global radio6
radio6 = tk.Radiobutton(variable=resp_var)
# radio6 = tk.Radiobutton(text=preguntas_dict[0][5], variable=resp_var, value=preguntas_dict[0][5])
radio6.place(x=-50, y=-50)

global radio7
radio7 = tk.Radiobutton(variable=resp_var)
# radio7 = tk.Radiobutton(text=preguntas_dict[0][6], variable=resp_var, value=preguntas_dict[0][6])
radio7.place(x=-50, y=-50)

global radio8
radio8 = tk.Radiobutton(variable=resp_var)
# radio8 = tk.Radiobutton(text=preguntas_dict[0][7], variable=resp_var, value=preguntas_dict[0][7])
radio8.place(x=-50, y=-50)

global radio9
radio9 = tk.Radiobutton(variable=resp_var)
# radio9 = tk.Radiobutton(text=preguntas_dict[0][8], variable=resp_var, value=preguntas_dict[0][8])
radio9.place(x=-50, y=-50)

global radio10
radio10 = tk.Radiobutton(variable=resp_var)
# radio10 = tk.Radiobutton(text=preguntas_dict[0][9], variable=resp_var, value=preguntas_dict[0][9])
radio10.place(x=-50, y=-50)

global radio11
radio11 = tk.Radiobutton(variable=resp_var)
# radio11 = tk.Radiobutton(text=preguntas_dict[0][10], variable=resp_var, value=preguntas_dict[0][10])
# radio11.place(x=-50, y=-50)

global radio12
radio12 = tk.Radiobutton(variable=resp_var)
# radio12 = tk.Radiobutton(text=preguntas_dict[0][11], variable=resp_var, value=preguntas_dict[0][11])
radio12.place(x=-50, y=-50)

global radio13
radio13 = tk.Radiobutton(variable=resp_var)
# radio13 = tk.Radiobutton(text=preguntas_dict[0][12], variable=resp_var, value=preguntas_dict[0][12])
radio13.place(x=-50, y=-50)

global radio14
radio14 = tk.Radiobutton(variable=resp_var)
# radio14 = tk.Radiobutton(text=preguntas_dict[0][13], variable=resp_var, value=preguntas_dict[0][13])
radio14.place(x=-50, y=-50)


def print_():
    if resp_var.get() != "":
        radio1.place(x=100, y=-50)
        radio2.place(x=100, y=-50)
        radio3.place(x=100, y=-50)
        radio4.place(x=100, y=-50)
        radio5.place(x=100, y=-50)
        radio6.place(x=100, y=-50)
        radio7.place(x=100, y=-50)
        radio8.place(x=100, y=-50)
        radio9.place(x=100, y=-50)
        radio10.place(x=100, y=-50)
        radio11.place(x=100, y=-50)
        radio12.place(x=100, y=-50)
        radio13.place(x=100, y=-50)
        radio14.place(x=100, y=-50)
        index.set(index.get() + 1)
        print(index.get())
        answers_list.append(resp_var.get())
        print(resp_var.get())
        resp_var.set("")
        if index.get() < 3:
            if len(preguntas_dict[index.get()]) > 0:
                radio1['text'] = preguntas_dict[index.get()][0]
                radio1['value'] = preguntas_dict[index.get()][0]
                radio1.place(x=100, y=200)
            if len(preguntas_dict[index.get()]) > 1:
                radio2['text'] = preguntas_dict[index.get()][1]
                radio2['value'] = preguntas_dict[index.get()][1]
                radio2.place(x=100, y=250)
            if len(preguntas_dict[index.get()]) > 2:
                radio3['text'] = preguntas_dict[index.get()][2]
                radio3['value'] = preguntas_dict[index.get()][2]
                radio3.place(x=100, y=300)
            if len(preguntas_dict[index.get()]) > 3:
                radio4['text'] = preguntas_dict[index.get()][3]
                radio4['value'] = preguntas_dict[index.get()][3]
                radio4.place(x=100, y=350)
            if len(preguntas_dict[index.get()]) > 4:
                radio5['text'] = preguntas_dict[index.get()][4]
                radio5['value'] = preguntas_dict[index.get()][4]
                radio5.place(x=100, y=400)
            if len(preguntas_dict[index.get()]) > 5:
                radio6['text'] = preguntas_dict[index.get()][5]
                radio6['value'] = preguntas_dict[index.get()][5]
                radio6.place(x=100, y=450)
            if len(preguntas_dict[index.get()]) > 6:
                radio7['text'] = preguntas_dict[index.get()][6]
                radio7['value'] = preguntas_dict[index.get()][6]
                radio7.place(x=100, y=500)
            if len(preguntas_dict[index.get()]) > 7:
                radio8['text'] = preguntas_dict[index.get()][7]
                radio8['value'] = preguntas_dict[index.get()][7]
                radio8.place(x=400, y=200)
            if len(preguntas_dict[index.get()]) > 8:
                radio9['text'] = preguntas_dict[index.get()][8]
                radio9['value'] = preguntas_dict[index.get()][8]
                radio9.place(x=400, y=250)
            if len(preguntas_dict[index.get()]) > 9:
                radio10['text'] = preguntas_dict[index.get()][9]
                radio10['value'] = preguntas_dict[index.get()][9]
                radio10.place(x=400, y=300)
            if len(preguntas_dict[index.get()]) > 10:
                radio11['text'] = preguntas_dict[index.get()][10]
                radio11['value'] = preguntas_dict[index.get()][10]
                radio11.place(x=400, y=350)
            if len(preguntas_dict[index.get()]) > 11:
                radio12['text'] = preguntas_dict[index.get()][11]
                radio12['value'] = preguntas_dict[index.get()][11]
                radio12.place(x=400, y=400)
            if len(preguntas_dict[index.get()]) > 12:
                radio13['text'] = preguntas_dict[index.get()][12]
                radio13['value'] = preguntas_dict[index.get()][12]
                radio13.place(x=400, y=450)
            if len(preguntas_dict[index.get()]) > 13:
                radio14['text'] = preguntas_dict[index.get()][13]
                radio14['value'] = preguntas_dict[index.get()][13]
                radio14.place(x=400, y=500)
            label['text'] = preguntas_list[index.get()]
        else:
            radio1.destroy()
            radio2.destroy()
            radio3.destroy()
            radio4.destroy()
            radio5.destroy()
            radio6.destroy()
            radio7.destroy()
            radio8.destroy()
            radio9.destroy()
            radio10.destroy()
            radio11.destroy()
            radio12.destroy()
            radio13.destroy()
            radio14.destroy()
            label.destroy()
            next_.destroy()
            end_.place(x=285, y=650)
            end_['bg'] = 'black'
            final_txt['text'] = "Ya no hay más preguntas, haca clic para ver sus resultados"
            print("Ya no hay mas preguntas")


def recommend1():
    res = []
    query = db.recommend1(answers_list[0], answers_list[1], answers_list[2])
    for record in query:
        res.append(Career(record[0]["nombre"], record[0]["facultad"]))
    final = "No se encontraron carreras para ti"
    for rec in res:
        final = "La carrera ideal para ti es:\n" + rec.name
    final_txt['text'] = final
    final_txt.place(x=125, y=300)
    end_['text'] = "Salir"
    end_['command'] = exit_
    print(answers_list)


def exit_():
    exit()


def start_():
    label.place(x=100, y=150)
    if len(preguntas_dict[index.get()]) > 0:
        radio1['text'] = preguntas_dict[0][0]
        radio1['value'] = preguntas_dict[0][0]
        radio1.place(x=100, y=200)
    if len(preguntas_dict[index.get()]) > 1:
        radio2['text'] = preguntas_dict[0][1]
        radio2['value'] = preguntas_dict[0][1]
        radio2.place(x=100, y=250)
    if len(preguntas_dict[index.get()]) > 2:
        radio3['text'] = preguntas_dict[0][2]
        radio3['value'] = preguntas_dict[0][2]
        radio3.place(x=100, y=300)
    if len(preguntas_dict[index.get()]) > 3:
        radio4['text'] = preguntas_dict[0][3]
        radio4['value'] = preguntas_dict[0][3]
        radio4.place(x=100, y=350)
    if len(preguntas_dict[index.get()]) > 4:
        radio5['text'] = preguntas_dict[0][4]
        radio5['value'] = preguntas_dict[0][4]
        radio5.place(x=100, y=400)
    if len(preguntas_dict[index.get()]) > 5:
        radio6['text'] = preguntas_dict[0][5]
        radio6['value'] = preguntas_dict[0][5]
        radio6.place(x=100, y=450)
    if len(preguntas_dict[index.get()]) > 6:
        radio7['text'] = preguntas_dict[0][6]
        radio7['value'] = preguntas_dict[0][6]
        radio7.place(x=100, y=500)
    if len(preguntas_dict[index.get()]) > 7:
        radio8['text'] = preguntas_dict[0][7]
        radio8['value'] = preguntas_dict[0][7]
        radio8.place(x=400, y=200)
    if len(preguntas_dict[index.get()]) > 8:
        radio9['text'] = preguntas_dict[0][8]
        radio9['value'] = preguntas_dict[0][8]
        radio9.place(x=400, y=250)
    if len(preguntas_dict[index.get()]) > 9:
        radio10['text'] = preguntas_dict[0][9]
        radio10['value'] = preguntas_dict[0][9]
        radio10.place(x=400, y=300)
    if len(preguntas_dict[index.get()]) > 10:
        radio11['text'] = preguntas_dict[0][10]
        radio11['value'] = preguntas_dict[0][10]
        radio11.place(x=400, y=350)
    if len(preguntas_dict[index.get()]) > 11:
        radio12['text'] = preguntas_dict[0][11]
        radio12['value'] = preguntas_dict[0][11]
        radio12.place(x=400, y=400)
    if len(preguntas_dict[index.get()]) > 12:
        radio13['text'] = preguntas_dict[0][12]
        radio13['value'] = preguntas_dict[0][12]
        radio13.place(x=400, y=450)
    if len(preguntas_dict[index.get()]) > 13:
        radio14['text'] = preguntas_dict[0][13]
        radio14['value'] = preguntas_dict[0][13]
        radio14.place(x=400, y=500)
    next_.config(state='normal')
    starts_.destroy()
    welcome.destroy()


label_0 = tk.Label(text="Escoja una de las respuestas a la pregunta", font="arial 18 bold")
label_0.place(x=110, y=50)

next_ = tk.Button(state='disabled', text="Siguiente", width=15, bg='black', fg='white', command=print_)
next_.place(x=550, y=650)

starts_ = tk.Button(text="Iniciar", width=15, bg='black', fg='white', command=start_)
starts_.place(x=285, y=650)

end_ = tk.Button(text="Ver resultados", width=15, bg='white', fg='white', command=recommend1)
end_.place(x=-50, y=-50)

root.mainloop()
