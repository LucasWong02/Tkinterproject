from tkinter import *
from tkinter import Toplevel
import sqlite3

#                   Access to my SQL database

conn = sqlite3.connect('users.db')
c = conn.cursor()

                    # Funcionamiento de Ingreso #

def myClick():
    def validacion():
        nombre = str(Ingreso_Usuario.get())
        contraseña = str(ingreso_Contra.get())

        def photo(): #Trataba con un codigo de Stack pero no se adhiere a mi proyecto
            novi = Toplevel()
            canvas = Canvas(novi, width=300, height=200)
            canvas.pack(expand=YES, fill=BOTH)
            png = PhotoImage(file='image.png')
            # image not visual
            canvas.create_image(50, 10, image=png, anchor=NW)
            # assigned the gif1 to the canvas object
            canvas.png = png

        for i in range(len(Usuarios)):
            if contraseña == Usuarios[nombre]:
                Nueva_Ingreso = Tk()
                photo = Button(Nueva_Ingreso, command=photo, height=5, width=20).pack()
                mensaje = Label(Nueva_Ingreso, text='Bienvenido(a)!')
                mensaje.pack()
            else:
                mensaje2 = Label(new, text='Tu usuario o contraseña no son correctos')
                mensaje2.pack()


    new = Toplevel()
    new.title("Ingresar")
    label = Label(new, text='Hola!. Por favor pon tu Usuario y Contraseña')
    label.pack()
    # Cuadros para poner ususario
    label2 = Label(new, text='Usuario')
    label2.pack()

    nombre = StringVar()
    Ingreso_Usuario = Entry(new, textvariable=nombre, width="50")
    Ingreso_Usuario.pack()


    label3 = Label(new, text='Contraseña')
    label3.pack()

    contraseña = StringVar()
    ingreso_Contra = Entry(new, textvariable=contraseña, width="50")
    ingreso_Contra.pack()


    # Boton de Ingresar
    B1 = Button(new, text='Ingresar!', command=validacion)
    B1.pack()
    # Boton de Registro
    B1 = Button(new, text='Registrate!', command=agregar)
    B1.pack()
    # Boton de Quit
    B2 = Button(new, text='EXIT', command=new.quit)
    B2.pack()


                        # Funcionamiento de Registro #
def agregar():
    def validacion():
        contrasena = str(ingreso_Contra.get())
        contrasena2 = str(ingreso_Contra2.get())
        if(contrasena==contrasena2):
            mensaje = Label(new2, text='Ya estas registrado!')
            mensaje.pack()
            c.execute("INSERT INTO users VALUES (nombre, contrasena)")
            conn.commit()
        else:
            mensaje2 = Label(new2, text='Las contraseñas no son iguales!')
            mensaje2.pack()

    new2 = Toplevel()
    new2.title("Ingresar")

    # Cuadros para poner ususario
    label2 = Label(new2, text='Usuario')
    label2.pack()
    #NOMBRE DE USUARIO
    nombre = StringVar()
    Ingreso_Usuario = Entry(new2, textvariable=nombre, width="50")
    Ingreso_Usuario.pack()

    label3 = Label(new2, text='Contraseña')
    label3.pack()

    #CONTRASEÑA INICIAL
    contrasena = StringVar()
    ingreso_Contra = Entry(new2, textvariable=contrasena, width="50")
    ingreso_Contra.pack()

    label3 = Label(new2, text='Repita su contraseña')
    label3.pack()

    #REP DE CONTRASEÑA
    contrasena2 = StringVar()
    ingreso_Contra2 = Entry(new2, textvariable=contrasena2, width="50")
    ingreso_Contra2.pack()

    B1 = Button(new2, text='Registrarme', command=validacion)
    B1.pack()
    B2 = Button(new2, text='EXIT', command=new2.quit)
    B2.pack()



### MAIN ###
Usuarios = {'Lucas':'1234', 'Tomas':'2345'}  # Usuario:Contraseña

root = Tk()
myLabel = Label(root, text="Hello World!")
root.title('OLD')
myLabel.pack()

myButton1 = Button(root, text="Ingresar", padx=50, command=myClick)
myButton1.pack()

myButton2 = Button(root, text="Registrarse", padx=50, command=agregar)
myButton2.pack()

root.mainloop()
