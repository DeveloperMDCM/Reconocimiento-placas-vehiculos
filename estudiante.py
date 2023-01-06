# Moises Canaria CECAR 
from tkinter import *
from tkinter import ttk
import pymysql
from tkinter import messagebox
import customtkinter
import base64
from PIL import Image, ImageTk
import io
import os
import csv
import cv2
width, height = 700, 400
import webbrowser
import requests
import threading

from datetime import datetime
import shutil
import time
global placa_detectada
cap = cv2.VideoCapture(0)
PATH = os.path.dirname(os.path.realpath(__file__))

def leer_placa(img):
    # estos parametros depende del tipo de placa a leer segun el pais
    regions = ['gb', 'it']
    # Se abre el archivo de datos .csv
    with open(img, 'rb') as fp:
        # se pide la consulta al servidor
        response = requests.post(
            'https://api.platerecognizer.com/v1/plate-reader/',
            data=dict(regions=regions),  # Opcional
            # se sube la foto al servidor
            # Se le envia el token a la APi de la web http://docs.platerecognizer.com/
            # Aqui tienes que colocar tu propio Token suscribiendote a la pagina
            files=dict(upload=fp),
            headers={'Authorization': 'Token 14fde66f98e57ed984a08eab164233951e135e97 '})
    return response.json()  # retorna el json con los datos procesados
# imprimir response.json() para ver los datos

# funcion para validar y guardar la placa leida
# funcion para validar y guardar la placa leida	
def validar_placa(data, fechas, horas):
    if data['results'] !=[]: 
        for result in data['results']:
            license_plate=result['plate']
			
         # se agrega la primera placa
                # lista_placas.append(license_plate.upper()) # se agrega la placa a la lista
                # #imprimr la placa leida con las veces que se encuentra en la lista
                # print(license_plate.upper(), lista_placas.count(license_plate.upper()))
                # # print(lista_placas)
				
        messagebox.showinfo("PLACA LEIDA", 'PLACA :' + license_plate.upper() )
		
        fecha = datetime.now()
        hora = datetime.now()
        fecha = fecha.strftime("%d/%m/%Y")
        hora = hora.strftime("%H:%M:%S")
        fechas.append(fecha)
        horas.append(hora)
		
        # Guardar todos los datos en un fichero .csv si no esta repetida
        # Si la placa no se encuentra en la lista mostrar un mensaje
        with open('save.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            # Guargar la exatitud de la lectura
            writer.writerow([fecha, hora, license_plate.upper(),
                            data['results'][0]['score']*100]  )
    
    else:  # cuando la imagen no tenga una placa
        messagebox.showerror("ERROR", 'La imagen NO FUE RECONOCIDA')
        # No se envia el response.json() porque no hay datos para guardar en el fichero .csv
        # se envia un mensaje de error
        print("La imagen NO FUE RECONOCIDA") 
    return data
fechas = []
horas = []
def AnalizarPlaca():
	foto = "temp.jpg"  # nombre de la imagen temporal a guardar
	_, frame = cap.read()
	cv2.imwrite(foto, frame)
	data = leer_placa(foto)
	validar_placa(data, fechas, horas)
def exportar():
            hora_actual = datetime.now()
            fecha = hora_actual.strftime("%d/%m/%Y")
            hora = hora_actual.strftime("%H:%M:%S")
             #Fecha remplaciar los / por -
            fecha = fecha.replace("/", "_")
            hora = hora.replace(":", "_")
            #Copiar el archivo save.csv a la carpeta exportar
            shutil.copy("save.csv", "exportar/"+'Reporte_'+fecha+'_'+hora+".csv")
            messagebox.showinfo( "Exportar", "Archivo exportado correctamente")            		
def Todos_user():
	webbrowser.open('http://127.0.0.1/conductores/index.php?page=conductores')  # Go to example.com
def Nuevo_user():
	webbrowser.open('http://127.0.0.1/conductores/index.php?page=form')  # Go to example.com
def mensaje():
    answer = messagebox.askyesno("Salir", "¿Desesa salir del sistema?, Confirme...")
    if(answer):
    	ventana.destroy()

class Student:
	def __init__(self,ventana):
		self.ventana=ventana
		self.ventana.title("Administrador de conductores")
		self.ventana.geometry("1560x800+00+00")
		# self.ventana.resizable(False,False)
		
		# Exit_btn=Button(ventana,text="Salir", width=7, bg="orange", font=("Arial",17,"bold"),command=mensaje)
		# Exit_btn.place(x=1200, y=40)
		#====Variables=====
		self.id_var=StringVar()
		self.placa_var=StringVar()
		self.nombre_var=StringVar()
		self.edad_var=StringVar()
		self.cedula_var=StringVar()
		self.color_var=StringVar()
		self.tipovehiculo_var=StringVar()
		self.genero_var=StringVar()
		self.ciudad_var=StringVar()
		self.tipopersona_var=StringVar()
		self.fecha_var=StringVar()
		self.buscar_por=StringVar()
		self.buscar_txt=StringVar()

		Manage_Frame=Frame(self.ventana,bd=4,relief=RIDGE, bg="black")
		Manage_Frame.place(x=0,y=0,width=720,height=630)
		
		Botones_Frame=Frame(self.ventana,bd=4,relief=RIDGE, bg="black")
		Botones_Frame.place(x=0,y=630,width=720,height=170)

		Camara=Frame(self.ventana, bg="black")
		Camara.place(x=1120,y=360,width=405,height=460)

		Foto_Frame=Frame(self.ventana, bg="black")
		Foto_Frame.place(x=720,y=360,width=400,height=460)

		

		# Create a Label to capture the Video frames
		label =Label(Camara,width=405,height=460, justify="center")
		label.grid(row=0, column=0)
		cap= cv2.VideoCapture(0)

		# Define function to show frame
		def show_frames():
			# Get the latest frame and convert into Image
			cv2image= cv2.cvtColor(cap.read()[1],cv2.COLOR_BGR2RGB)
			img = Image.fromarray(cv2image)
			# Convert image to PhotoImage
			imgtk = ImageTk.PhotoImage(image = img)
			label.imgtk = imgtk
			label.configure(image=imgtk)
			# Repeat after an interval to capture continiously
			label.after(20, show_frames)
		show_frames()

		def AnalizarPlaca():
			foto = "temp.jpg"  # nombre de la imagen temporal a guardar
			_, frame = cap.read()
			cv2.imwrite(foto, frame)
			data = leer_placa(foto)
			validar_placa(data, fechas, horas)
			
			for result in data['results']:
				license_plate=result['plate']
				placa_detectadas=license_plate	
				print(placa_detectadas)	
				with open('save.csv', 'r') as file:
					reader = csv.reader(file)
					data = list(reader)
					id_fila = len(data)	
								
				txt_search= customtkinter.CTkEntry(master=Detail_Frame,textvariable=self.buscar_txt, width=100, text_font=("Arial", 10))
				txt_search.grid(row=0,column=3,pady=10,padx=20,sticky="w")	
				txt_search.insert(0, license_plate.upper())				
				search_btn= customtkinter.CTkButton(master=Detail_Frame,text="Buscar", width=10,text_font=("Arial", 15),command=self.buscar_data)
				search_btn.grid(row=0, column=4, padx=10, pady=10)
				def limpar_busqueda():
					txt_search= customtkinter.CTkEntry(textvariable=self.buscar_txt, width=100, text_font=("Arial", 10),command=limpar_busqueda)
					txt_search.delete("0",END)
				
				label_id = customtkinter.CTkLabel(master=Manage_Frame, text="Registros del dia: "+str(id_fila), fg_color=("white", "#f00"), corner_radius=8, text_font=("Bold", 20))
				label_id.grid(row=1, column=0, padx=0, pady=10, columnspan=5, sticky="nsew")																			
		# m_title=Label(Manage_Frame,, bg="blue", fg="white", font=("Arial",13,"bold"), width=30)
		m_title = customtkinter.CTkLabel(master=Manage_Frame, text="Informacion del conductor", fg_color=("black", "green"), corner_radius=8,text_font=("Arial", 25), width=100)
		m_title.grid(row=0, column=0, columnspan=5,padx=40, pady=60, sticky="nsew")
		# lbl_id=Label(Manage_Frame,text="id:", bg="yellow", fg="red", font=("Arial",10,"bold"))
		# lbl_id.grid(row=1,column=0,pady=10,padx=20,sticky="w")
		# txt_id=Entry(Manage_Frame, textvariable=self.id_var , font=("Arial",10,"bold"), bd=5, relief=GROOVE)
		# txt_id.grid(row=1,column=1,pady=10,padx=20,sticky="e")
		label_placa = customtkinter.CTkLabel(master=Manage_Frame, text="Placa", fg_color=("black", "green"), corner_radius=8, width=100, text_font=("Arial", 15))
		label_placa.grid(row=2, column=0, padx=16,pady=25, sticky="s", columnspan=1)
		label_placa = customtkinter.CTkEntry(master=Manage_Frame, textvariable=self.placa_var, fg_color=("black", "black"), corner_radius=8, justify='center',border_color="#ccc",width=200)
		label_placa.grid(row=2, column=1, padx=5,pady=25, sticky="news", columnspan=1)
		label_nombre = customtkinter.CTkLabel(master=Manage_Frame, text="Nombre", fg_color=("black", "green"), corner_radius=8, width=100,text_font=("Arial", 15))
		label_nombre.grid(row=2, column=3, padx=5,pady=25, sticky="s", columnspan=1)
		label_nombre = customtkinter.CTkEntry(master=Manage_Frame, textvariable=self.nombre_var, fg_color=("black", "black"), corner_radius=8, justify='center',border_color="#ccc",width=200)
		label_nombre.grid(row=2, column=4, padx=5,pady=25, sticky="news", columnspan=1)
		
		label_edad = customtkinter.CTkLabel(master=Manage_Frame, text="Edad", fg_color=("black", "green"), corner_radius=8, width=100,text_font=("Arial", 15))
		label_edad.grid(row=3, column=0, padx=5,pady=25, sticky="s", columnspan=1)
		label_edad = customtkinter.CTkEntry(master=Manage_Frame, textvariable=self.edad_var, fg_color=("black", "black"), corner_radius=8, justify='center',border_color="#ccc",width=200)
		label_edad.grid(row=3, column=1, padx=5,pady=25, sticky="news", columnspan=1)
		label_cedula = customtkinter.CTkLabel(master=Manage_Frame, text="Cedula", fg_color=("black", "green"), corner_radius=8, width=100,text_font=("Arial", 15))
		label_cedula.grid(row=3, column=3, padx=5,pady=25, sticky="s", columnspan=1)
		label_cedula = customtkinter.CTkEntry(master=Manage_Frame, textvariable=self.cedula_var, fg_color=("black", "black"), corner_radius=8, justify='center',border_color="#ccc",width=200)
		label_cedula.grid(row=3, column=4, padx=5,pady=25, sticky="news", columnspan=1)

		label_color = customtkinter.CTkLabel(master=Manage_Frame, text="Color", fg_color=("black", "green"), corner_radius=8, width=100,text_font=("Arial", 15))
		label_color.grid(row=4, column=0, padx=5,pady=25, sticky="s", columnspan=1)
		label_tipo = customtkinter.CTkLabel(master=Manage_Frame, text="Tipo", fg_color=("black", "green"), corner_radius=8, width=100,text_font=("Arial", 15))
		label_tipo.grid(row=4, column=3, padx=5,pady=25, sticky="s", columnspan=1)

		
		label_genero = customtkinter.CTkLabel(master=Manage_Frame, text="Genero", fg_color=("black", "green"), corner_radius=8, width=100,text_font=("Arial", 15))
		label_genero.grid(row=4, column=0, padx=5,pady=25, sticky="s", columnspan=1)
		combobox_genero = customtkinter.CTkComboBox(master=Manage_Frame, variable=self.genero_var, values=["M","F","Otro"],border_color="#ccc",dropdown_text_color="white", text_color="white" , button_color="red",width=200)
		combobox_genero.grid(row=4, column=1, padx=20, pady=25, sticky="s")
		label_ciudad = customtkinter.CTkLabel(master=Manage_Frame, text="Ciudad", fg_color=("black", "green"), corner_radius=8, width=100,text_font=("Arial", 15))
		label_ciudad.grid(row=4, column=3, padx=5,pady=25, sticky="s", columnspan=1)
		label_ciudad = customtkinter.CTkEntry(master=Manage_Frame, textvariable=self.ciudad_var, fg_color=("black", "black"), corner_radius=8, justify='center',border_color="#ccc",width=200)
		label_ciudad.grid(row=4, column=4, padx=5,pady=25, sticky="news", columnspan=1)

		label_rol = customtkinter.CTkLabel(master=Manage_Frame, text="Rol", fg_color=("black", "green"), corner_radius=8, width=100,text_font=("Arial", 15))
		label_rol.grid(row=5, column=0, padx=5,pady=25, sticky="s", columnspan=1)
		combobox_rol = customtkinter.CTkComboBox(master=Manage_Frame, variable=self.tipopersona_var, values=["Estudiante", "Docente", "Administrativo", "Visitante"],border_color="#ccc",dropdown_text_color="white", text_color="white" ,width=200)
		combobox_rol.grid(row=5, column=1, padx=20, pady=25, sticky="s")
		label_color = customtkinter.CTkLabel(master=Manage_Frame, text="Color", fg_color=("black", "green"), corner_radius=8, width=100,text_font=("Arial", 15))
		label_color.grid(row=5, column=3, padx=5,pady=25, sticky="s", columnspan=1)
		label_color = customtkinter.CTkEntry(master=Manage_Frame, textvariable=self.color_var, fg_color=("black", "black"), corner_radius=8, justify='center',border_color="#ccc",width=200)
		label_color.grid(row=5, column=4, padx=5,pady=25, sticky="news", columnspan=1)

		label_tipo = customtkinter.CTkLabel(master=Manage_Frame, text="Tipo", fg_color=("black", "green"), corner_radius=8, width=100,text_font=("Arial", 15))
		label_tipo.grid(row=6, column=0, padx=5,pady=25, sticky="s", columnspan=1)
		combobox_tipo = customtkinter.CTkComboBox(master=Manage_Frame, variable=self.tipovehiculo_var, values=["Carro","Moto"],border_color="#ccc",dropdown_text_color="white", text_color="white" ,width=200)
		combobox_tipo.grid(row=6, column=1, padx=20, pady=25, sticky="s")
		label_fecha = customtkinter.CTkLabel(master=Manage_Frame, text="Fecha", fg_color=("black", "green"), corner_radius=8, width=100,text_font=("Arial", 15))
		label_fecha.grid(row=6, column=3, padx=5,pady=25, sticky="s", columnspan=1)
		label_fecha = customtkinter.CTkEntry(master=Manage_Frame, textvariable=self.fecha_var, fg_color=("black", "black"), corner_radius=8, justify='center',border_color="#ccc",width=200)
		label_fecha.grid(row=6, column=4, padx=5,pady=25, sticky="news", columnspan=1)
		# combobox_rol.configure(state="readonly")
		
        # Seccion botones del menu
		btn_Frame=Frame(Botones_Frame,relief=RIDGE, bg="black")
		btn_Frame.place(x=0,y=80,width=710, height=160,  anchor='w')

		Conductor_Frame=Frame(Foto_Frame,relief=RIDGE, bg="black")
		Conductor_Frame.place(x=0,y=370,width=600, height=700,  anchor='w')

		self.settings_image = self.load_image("/test_images/settings.png", 20)
		self.bell_image = self.load_image("/test_images/bell.png", 20)
		self.add_folder_image = self.load_image("/test_images/add-folder.png", 20)
		self.add_list_image = self.load_image("/test_images/add-folder.png", 20)
		self.nuevo_registro = self.load_image("/test_images/add-user.png", 20)
		self.analizar_placa = self.load_image("/test_images/car.png", 35)
		self.salir = self.load_image("/test_images/exit.png", 24)
		self.info = self.load_image("/test_images/info.png", 35)
		self.todos = self.load_image("/test_images/todos.png", 35)
		self.eliminar = self.load_image("/test_images/del.png", 25)
		self.actualizar = self.load_image("/test_images/update.png", 25)
		self.limpiar = self.load_image("/test_images/clear.png", 25)
		self.exportar = self.load_image("/test_images/export.png", 25)

		btn_placa = customtkinter.CTkButton(master=btn_Frame, image=self.analizar_placa, text="Analizar placa", width=130, height=60, border_width=2,corner_radius=10, compound="bottom", border_color="#8fff33", fg_color=("gray84", "gray25"),hover_color="#000", command=AnalizarPlaca)
		btn_placa.grid(row=1, column=0, padx=20, pady=7,columnspan=1,  sticky="news")
		btn_usuario = customtkinter.CTkButton(master=btn_Frame,image=self.info, text="Todos los registros", width=130, height=60, border_width=2,corner_radius=10, compound="bottom", border_color="#0f00cc", fg_color=("gray84", "gray25"),hover_color="#000", command=Todos_user)
		btn_usuario.grid(row=1, column=1, columnspan=1,padx=20, pady=7, sticky="nsew")
		btn_registro = customtkinter.CTkButton(master=btn_Frame, image=self.nuevo_registro,text="Nuevo registro", width=130, height=60, border_width=2,corner_radius=10, compound="bottom", border_color="#ff0", fg_color=("gray84", "gray25"),hover_color="#000", command=Nuevo_user)
		btn_registro.grid(row=1, column=2, columnspan=1, padx=20, pady=7, sticky="news")
		btn_salir = customtkinter.CTkButton(master=btn_Frame,image=self.salir, text="Salir del programa", width=130, height=60, border_width=2,corner_radius=10, compound="bottom", border_color="#ff0000", fg_color=("gray84", "gray25"),hover_color="#000",command=mensaje)
		btn_salir.grid(row=1, column=3, columnspan=1,padx=20, pady=10, sticky="nsew")
		btn_limpiar = customtkinter.CTkButton(master=btn_Frame,image=self.limpiar, text="Limpiar", width=130, height=60, border_width=2,corner_radius=10, compound="bottom", border_color="#cccccc", fg_color=("#cccccc", "gray25"),hover_color="#000",command=self.clear)
		btn_limpiar.grid(row=2, column=0, columnspan=1,padx=20, pady=10, sticky="nsew")
		btn_actualizar = customtkinter.CTkButton(master=btn_Frame,image=self.actualizar, text="Actualizar", width=130, height=60, border_width=2,corner_radius=10, compound="bottom", border_color="#cccccc", fg_color=("#cccccc", "gray25"),hover_color="#000",command=self.update_data)
		btn_actualizar.grid(row=2, column=1, columnspan=1,padx=20, pady=10, sticky="nsew")
		btn_eliminar = customtkinter.CTkButton(master=btn_Frame,image=self.eliminar, text="Eliminar", width=130, height=60, border_width=2,corner_radius=10, compound="bottom", border_color="#cccccc", fg_color=("#cccccc", "gray25"),hover_color="#000",command=self.delete_data)
		btn_eliminar.grid(row=2, column=2, columnspan=1,padx=20, pady=10, sticky="nsew")

		btn_exportar = customtkinter.CTkButton(master=btn_Frame,image=self.exportar, text="Exportar", width=130, height=60, border_width=2,corner_radius=10, compound="bottom", border_color="#cccccc", fg_color=("#cccccc", "gray25"),hover_color="#000", command=exportar)
		btn_exportar.grid(row=2, column=3, columnspan=1,padx=20, pady=10, sticky="nsew")
		# Foto del conductor
		self.home_image2 = self.load_image("./test_images/Info.png", 380)
		
		label_foto = customtkinter.CTkLabel(master=Conductor_Frame, image=self.home_image2 , corner_radius=8)
		label_foto.grid(row=0, column=0)

		Detail_Frame=Frame(self.ventana,bd=4,relief=RIDGE, bg="black")
		Detail_Frame.place(x=720,y=0,width=810,height=360)

		lbl_search=Label(Detail_Frame,text="Buscar por:", fg="red", font=("Arial",15,"bold"))
		lbl_search.grid(row=0,column=0,pady=10,padx=20,sticky="w")
		
		combobox_rol = customtkinter.CTkComboBox(master=Detail_Frame,variable=self.buscar_por, values=["id","Nombre","placa","cedula","genero"],dropdown_text_color="white", text_color="white" )
		combobox_rol.grid(row=0, column=2, padx=20, pady=10)
		combobox_rol.set("placa")
	
		

		

		showall_btn= customtkinter.CTkButton(master=Detail_Frame, text="Mostrar Todo", text_font=("Arial", 15) ,width=10,command=self.fetch_data)
		showall_btn.grid(row=0, column=5, padx=10, pady=10)

		Table_Frame=Frame(Detail_Frame,bd=4,relief=RIDGE, bg="crimson")
		Table_Frame.place(x=20,y=60,width=760,height=280)

		scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL )
		scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)

		self.Student_table=ttk.Treeview(Table_Frame,columns=("id","placa","nombre", "edad", "cedula", "color", "tipo_vehiculo", "genero", "ciudad", "tipo_persona", "fecha", "imagen"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
		scroll_x.pack(side=BOTTOM,fill=X)
		scroll_y.pack(side=RIGHT, fill=Y)
		scroll_x.config(command=self.Student_table.xview)
		scroll_y.config(command=self.Student_table.yview)
		style=ttk.Style()
		style.theme_use('clam')
		self.Student_table.heading("id", text="ID")
		self.Student_table.heading("placa", text="Placa")
		self.Student_table.heading("nombre", text="Nombre")
		self.Student_table.heading("edad", text="Edad")
		self.Student_table.heading("cedula", text="Cedula")
		self.Student_table.heading("color", text="Color")
		self.Student_table.heading("tipo_vehiculo", text="Vehiculo")
		self.Student_table.heading("genero", text="Genero")
		self.Student_table.heading("ciudad", text="Ciudad")
		self.Student_table.heading("tipo_persona", text="Rol")
		self.Student_table.heading("fecha", text="Fecha")
		self.Student_table.heading("imagen", text="imagen")
		self.Student_table['show']= 'headings'
		self.Student_table.column("id", width=4)
		self.Student_table.column("placa", width=100, anchor='center')
		self.Student_table.column("nombre", width=100, anchor='center')
		self.Student_table.column("edad", width=100, anchor='center')
		self.Student_table.column("cedula", width=100, anchor='center')
		self.Student_table.column("color", width=100, anchor='center')
		self.Student_table.column("tipo_vehiculo", width=100, anchor='center')
		self.Student_table.column("genero", width=100, anchor='center')
		self.Student_table.column("ciudad", width=100, anchor='center')
		self.Student_table.column("tipo_persona", width=100, anchor='center')
		self.Student_table.column("fecha", width=140, anchor='center')
		self.Student_table.column("imagen", width=100, anchor='center')
	
	


		self.Student_table.pack(fill=BOTH,expand=1)

		self.Student_table.bind("<ButtonRelease-1>", self.get_cursor)
	
		self.fetch_data()

	def agregar_personas(self):

		if self.placa_var.get()=="" or self.nombre_var.get()=="" or self.edad_var.get()=="" or self.cedula_var.get()=="" or self.color_var.get()=="" or self.tipovehiculo_var.get()=="" or self.genero_var.get()=="" or self.ciudad_var.get()=="" or self.tipopersona_var.get()=="" or self.fecha_var.get()=="":
			messagebox.showerror("Error", "Todos los campos son requeridos!!!")
		else:

			con=pymysql.connect(host="localhost", user="root",password="",database="conductores")
			cur=con.cursor()
			cur.execute("insert into personas values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
				self.placa_var.get(),
				self.nombre_var.get(),
				self.edad_var.get(),
				self.cedula_var.get(),
				self.color_var.get(),
				self.tipovehiculo_var.get(),
				self.genero_var.get(),
				self.ciudad_var.get(),
				self.tipopersona_var.get(),
				self.fecha_var.get(),
				self.id_var.get(),
				))
			con.commit()
			self.fetch_data()
			self.clear()
			con.close()
			messagebox.showinfo("Adelante...", "Se agregó correctamente el registro")

	def fetch_data(self):
		con=pymysql.connect(host="localhost", user="root",password="",database="conductores")
		cur=con.cursor()
		cur.execute("select * from personas")
		rows=cur.fetchall()
		if len(rows)!=0:
			self.Student_table.delete(*self.Student_table.get_children())
			for row in rows:
				self.Student_table.insert('',END,values=row)
			con.commit()
		con.close()

	def clear(self):
		self.placa_var.set("")
		self.nombre_var.set("")
		self.edad_var.set("")
		self.cedula_var.set("")
		self.color_var.set("")
		self.tipovehiculo_var.set("")
		self.genero_var.set("")
		self.ciudad_var.set("")
		self.tipopersona_var.set("")
		self.fecha_var.set("")
		self.home_image2 = self.load_image("./test_images/Info.png", 380)
		Foto_Frame=Frame(self.ventana, bg="black")
		Foto_Frame.place(x=720,y=360,width=400,height=460)
		Conductor_Frame=Frame(Foto_Frame,relief=RIDGE, bg="black")
		Conductor_Frame.place(x=0,y=370,width=600, height=700,  anchor='w')
		label_foto = customtkinter.CTkLabel(master=Conductor_Frame, image=self.home_image2 , corner_radius=8)
		label_foto.grid(row=0, column=0)
		def limpar_busqueda():
			txt_search= customtkinter.CTkEntry(textvariable=self.buscar_txt, width=100, text_font=("Arial", 10))
			txt_search.delete("0",END)
		limpar_busqueda()	
	def get_cursor(self,ev):
		cursor_row=self.Student_table.focus()
		contents=self.Student_table.item(cursor_row)
		row=contents['values']	
		self.placa_var.set(row[1])
		self.nombre_var.set(row[2])
		self.edad_var.set(row[3])
		self.cedula_var.set(row[4])
		self.color_var.set(row[5])
		self.tipovehiculo_var.set(row[6])
		self.genero_var.set(row[7])
		self.ciudad_var.set(row[8])
		self.tipopersona_var.set(row[9])
		self.fecha_var.set(row[10])
		# self.imagen_var.set(row[11])
		self.id_var.set(row[0])
		
		self.home_image2 = self.load_image("./Conductores/"+str(row[1])+'.jpg', 380)
		Foto_Frame=Frame(self.ventana, bg="black")
		Foto_Frame.place(x=720,y=360,width=400,height=460)
		Conductor_Frame=Frame(Foto_Frame,relief=RIDGE, bg="black")
		Conductor_Frame.place(x=0,y=370,width=600, height=700,  anchor='w')
		label_foto = customtkinter.CTkLabel(master=Conductor_Frame, image=self.home_image2 , corner_radius=8)
		label_foto.grid(row=0, column=0)
		# self.txt_direccion.delete("1.0",END)
		# self.txt_direccion.insert(END,row[6])

	def update_data(self):
		if self.placa_var.get()=="" or self.nombre_var.get()=="" or self.edad_var.get()=="" or self.cedula_var.get()=="" or self.color_var.get()=="" or self.tipovehiculo_var.get()=="" or self.genero_var.get()=="" or self.ciudad_var.get()=="" or self.tipopersona_var.get()=="" or self.fecha_var.get()=="":
			messagebox.showerror("Error", "Seleccione el registro a actualizar")
		else:

			con=pymysql.connect(host="localhost", user="root",password="",database="conductores")
			cur=con.cursor()
			cur.execute("update personas set placa=%s,nombre=%s,edad=%s,cedula=%s,color=%s,tipo_vehiculo=%s, genero=%s,ciudad=%s,tipo_persona=%s,fecha=%s where id=%s",(
				self.placa_var.get(),
				self.nombre_var.get(),
				self.edad_var.get(),
				self.cedula_var.get(),
				self.color_var.get(),
				self.tipovehiculo_var.get(),
				self.genero_var.get(),
				self.ciudad_var.get(),
				self.tipopersona_var.get(),
				self.fecha_var.get(),
				self.id_var.get(),
				# self.txt_direccion.get('1.0', END),
				
				))
			con.commit()
			self.fetch_data()
			self.clear()
			messagebox.showinfo("Actualizando", "Se actualizó correctamente el registro")
			con.close()

	def delete_data(self):
		if self.placa_var.get()=="" or self.nombre_var.get()=="" or self.edad_var.get()=="" or self.cedula_var.get()=="" or self.color_var.get()=="" or self.tipovehiculo_var.get()=="" or self.genero_var.get()=="" or self.ciudad_var.get()=="" or self.tipopersona_var.get()=="" or self.fecha_var.get()=="":
			messagebox.showerror("Error", "Seleccione el registro a eliminar")
		else:
			con=pymysql.connect(host="localhost", user="root",password="",database="conductores")
			cur=con.cursor()
			cur.execute("delete from personas where id=%s",self.id_var.get())
			con.commit()
			self.fetch_data()
			self.clear()
			messagebox.showinfo("Eliminar", "Se eliminó correctamente el registro")
			con.close()

	def buscar_data(self):
		con=pymysql.connect(host="localhost", user="root",password="",database="conductores")
		cur=con.cursor()
		cur.execute("select * from personas where "+str(self.buscar_por.get())+" LIKE '%"+str(self.buscar_txt.get())+"%'")
		rows=cur.fetchall()
		if len(rows)!=0:
			self.Student_table.delete(*self.Student_table.get_children())
			for row in rows:
				self.Student_table.insert('',END,values=row)
			con.commit()
		else:
			messagebox.showerror("Error", "La placa no se encuentra registrada registrela")
			self.home_image2 = self.load_image("./Conductores/0.jpg", 380)
			Foto_Frame=Frame(self.ventana, bg="black")
			Foto_Frame.place(x=720,y=360,width=400,height=460)
			Conductor_Frame=Frame(Foto_Frame,relief=RIDGE, bg="black")
			Conductor_Frame.place(x=0,y=370,width=600, height=700,  anchor='w')
			label_foto = customtkinter.CTkLabel(master=Conductor_Frame, image=self.home_image2 , corner_radius=8)
			label_foto.grid(row=0, column=0)
			self.placa_var.set("")
			self.nombre_var.set("")
			self.edad_var.set("")
			self.cedula_var.set("")
			self.color_var.set("")
			self.tipovehiculo_var.set("")
			self.genero_var.set("")
			self.ciudad_var.set("")
			self.tipopersona_var.set("")
			self.fecha_var.set("")
			def limpar_busqueda():
				txt_search= customtkinter.CTkEntry(textvariable=self.buscar_txt, width=100, text_font=("Arial", 10))
				txt_search.delete("0",END)
			limpar_busqueda()
		con.close()	
	def load_image(self, path, image_size):
		return ImageTk.PhotoImage(Image.open(PATH + path).resize((image_size, image_size)))	
ventana = Tk()
ob=Student(ventana)
ventana.mainloop()
