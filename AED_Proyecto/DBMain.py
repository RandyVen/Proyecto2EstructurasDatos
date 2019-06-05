
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
nodeType4 = "Carrera"

materias = []
personas = []
hobbies = []
carreras = []

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

result4 = db.getAllType(nodeType4)
for record in result4:
    carreras.append(record[0]["nombre"])

root = tk.Tk()
root.geometry('700x700')
root.title("Recomendador de Carreras")

preguntas_dict = {0: [],
                  1: [],
                  2: []}

preguntas_list = ["En cual de las siguientes materias consideras que tienes un mejor desempeño",
                  "A cual de las siguientes figuras publicas le tienes mayor admiracion ",
                  "Cual de los siguientes pasatiempos es el que mas disfrutas hacer"]

textos = ["Cual materia se relaciona con la nueva carrera",
          "Cual de las siguientes figuras publicas se relaciona con la carrera",
          "De los siguientes hobbies, cual se asocia a la carrera"]

preguntas_dict[0] = materias
preguntas_dict[1] = personas
preguntas_dict[2] = hobbies

res = []
answers_list = []
new = []
new_career_list = []

index = tk.IntVar()
resp_var = tk.StringVar()
input_var = tk.StringVar()
cont = tk.IntVar()

global add_txt
add_txt = tk.Label(text="Ingrese el nombre de la nueva carrera", font="arial 16")
add_txt.place(x=-50, y=-50)

global final_txt
final_txt = tk.Label(text="", font="arial 18")
final_txt.place(x=25, y=250)

global label
label = tk.Label(text=preguntas_list[0], font="arial 12")
label.place(x=-50, y=-50)

global welcome
welcome = tk.Label(text="Se lo mas sincero para responder las preguntas", font="arial 14 bold")
welcome.place(x=150, y=120)

global input
input = tk.Entry(textvar=input_var)
input.place(x=-50, y=-50)

global radio1
radio1 = tk.Radiobutton(variable=resp_var)
radio1.place(x=-50, y=-50)

global radio2
radio2 = tk.Radiobutton(variable=resp_var)
radio2.place(x=-50, y=-50)

global radio3
radio3 = tk.Radiobutton(variable=resp_var)
radio3.place(x=-50, y=-50)

global radio4
radio4 = tk.Radiobutton(variable=resp_var)
radio4.place(x=-50, y=-50)

global radio5
radio5 = tk.Radiobutton(variable=resp_var)
radio5.place(x=-50, y=-50)

global radio6
radio6 = tk.Radiobutton(variable=resp_var)
radio6.place(x=-50, y=-50)

global radio7
radio7 = tk.Radiobutton(variable=resp_var)
radio7.place(x=-50, y=-50)

global radio8
radio8 = tk.Radiobutton(variable=resp_var)
radio8.place(x=-50, y=-50)

global radio9
radio9 = tk.Radiobutton(variable=resp_var)
radio9.place(x=-50, y=-50)

global radio10
radio10 = tk.Radiobutton(variable=resp_var)
radio10.place(x=-50, y=-50)

global radio11
radio11 = tk.Radiobutton(variable=resp_var)
radio11.place(x=-50, y=-50)

global radio12
radio12 = tk.Radiobutton(variable=resp_var)
radio12.place(x=-50, y=-50)

global radio13
radio13 = tk.Radiobutton(variable=resp_var)
radio13.place(x=-50, y=-50)

global radio14
radio14 = tk.Radiobutton(variable=resp_var)
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


def recommend_():
    res = []
    query = db.recommend1(answers_list[0], answers_list[1], answers_list[2])
    for record in query:
        res.append(Career(record[0]["nombre"], record[0]["facultad"]))

    if len(res) == 0:
        query = db.recommend2(answers_list[0], answers_list[1])
        for record in query:
            res.append(Career(record[0]["nombre"], record[0]["facultad"]))

    if len(res) == 0:
        query = db.recommend3(answers_list[0])
        for record in query:
            res.append(Career(record[0]["nombre"], record[0]["facultad"]))
    final = "Las carreras recomendadas para ti son:\n\n"
    for rec in res:
        final += rec.name + "\n"
    final_txt['text'] = final
    final_txt.place(x=125, y=300)
    end_['text'] = "Salir"
    end_['command'] = exit_
    print(answers_list)


def print2_():
    if resp_var.get() != "" or input_var.get() != "":
        if cont.get() < 1:
            print(input_var.get())
            new_career_list.append(input_var.get())
            cont.set(cont.get() + 1)
            add_txt['text'] = "Ingrese la facultad de la nueva carrera"
        else:
            if cont.get() < 2:
                new_career_list.append(input_var.get())
                cont.set(cont.get() + 1)
            if index.get() < 3:
                label.place(x=100, y=150)
                label['text'] = textos[index.get()]
            input.destroy()
            add_txt.destroy()
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
            if resp_var.get() != "":
                new_career_list.append(resp_var.get())
            resp_var.set("")
            input_var.set("")
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
                label['text'] = textos[index.get()]
                index.set(index.get() + 1)
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
                next2_.destroy()
                end_.place(x=285, y=650)
                end_['bg'] = 'black'
                end_['text'] = "Salir"
                end_['command'] = exit_
                final_txt['text'] = "Base de datos actualizada"
                final_txt.place(x=200, y=350)
                with driver.session() as session:
                    session.read_transaction(db.create_career_wLinks, new_career_list[1], new_career_list[0],
                                             new_career_list[2], new_career_list[3], new_career_list[4])
                print("Ya no hay mas preguntas")
                print(new_career_list)


def nexxt_():
    if input_var.get() not in carreras:
        pass
    else:
        db.deleteCareer(input_var.get())
        next2_.destroy()
        add_txt.destroy()
        input.destroy()
        final_txt['text'] = "Base de datos actualizada"
        final_txt.place(x=200, y=350)
        end_.place(x=285, y=650)
        end_['bg'] = 'black'
        end_['text'] = "Salir"
        end_['command'] = exit_


def exit_():
    exit()


def add_():
    next_.destroy()
    next2_.config(state='normal')
    add_txt.place(x=150, y=250)
    input.place(x=275, y=350)
    deletes_.destroy()
    adds_.destroy()


def delete_():
    next_.destroy()
    next2_.config(state='normal')
    next2_['command'] = nexxt_
    add_txt.place(x=150, y=250)
    add_txt['text'] = "Ingrese el nombre de la carrera a eliminar"
    input.place(x=275, y=350)
    deletes_.destroy()
    adds_.destroy()


def edit_():
    welcome.destroy()
    edits_.destroy()
    starts_.destroy()
    deletes_.place(x=200, y=400)
    adds_.place(x=400, y=400)


def start_():
    next2_.destroy()
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
    edits_.destroy()
    welcome.destroy()


label_0 = tk.Label(text="Escoja una de las respuestas a la pregunta", font="arial 18 bold")
label_0.place(x=110, y=50)

next_ = tk.Button(state='disabled', text="Siguiente", width=15, bg='black', fg='white', command=print_)
next_.place(x=550, y=650)

next2_ = tk.Button(state='disabled', text="Siguiente", width=15, bg='black', fg='white', command=print2_)
next2_.place(x=550, y=650)

starts_ = tk.Button(text="Iniciar", width=15, bg='black', fg='white', command=start_)
starts_.place(x=285, y=650)

edits_ = tk.Button(text="Editar", width=15, bg='black', fg='white', command=edit_)
edits_.place(x=50, y=650)

end_ = tk.Button(text="Ver resultados", width=15, bg='white', fg='white', command=recommend_)
end_.place(x=-50, y=-50)

adds_ = tk.Button(text="Agregar", width=15, bg='black', fg='white', command=add_)
adds_.place(x=-50, y=-50)

deletes_ = tk.Button(text="Eliminar", width=15, bg='black', fg='white', command=delete_)
deletes_.place(x=-50, y=-50)

root.mainloop()
