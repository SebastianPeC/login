from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox

#creamos ventana
ventana= Tk()
ventana.title= ("login")
ventana.geometry("800x500")
ventana.resizable(False,False)

#creamos primer frame
frame1= Frame(ventana)
frame1.pack(side=LEFT)

#creamos el label con la imagen
imagen= Image.open("login\\luffy.jpg")
imagen= ImageTk.PhotoImage(imagen)
label= Label(frame1,image=imagen,height=500,width=400)
label.grid(row=1,column=1)



#creamos segundo frame
frame2= Frame(ventana, padx=100)
frame2.pack(side=RIGHT)

#creamos lo que va dentro del segundo frame
login= Label(frame2,text="Login",height=4,font=("arial",20,"bold"))
login.grid(row=1,column=1)

usuario= Label(frame2,text="Usuario")
usuario.grid(row=2,column=1)
ingresarusuario= Entry(frame2,width=30)
ingresarusuario.grid(row=3,column=1)

clave= Label(frame2,text="clave")
clave.grid(row=4,column=1)
ingresarclave= Entry(frame2,width=30)
ingresarclave.grid(row=5,column=1)


#funcion para mostrar los datos en un messagebox

def mostrar():
    datos= f"usuario: {ingresarusuario.get()} \n contraseña: {ingresarclave.get()}"
    messagebox.showinfo("login",datos)

boton= Button(frame2,text="Ingresar",command=mostrar)
boton.grid(row=6,column=1)


ventana.mainloop()

