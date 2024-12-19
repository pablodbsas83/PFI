#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  proyectoFinalDB_v2.4
#  
#  Copyright 2024 Pablo Toledo <pablodbsas83@gmail.com>
#  
#	Proyecto final con Base de Datos


#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
import os			#importa la libreria OS para usar el comando del sistema operativo "borrar pantalla"
import sqlite3 		#importa la libreria de Sqlite3 para usar la base de datos
from colorama import init, Fore, Back #importo la libreria colorama para dar color a los textos
init(autoreset=True)
#rutaBaseDatos = "/media/tpa/backup/cursos2024/Python/proyectoFinal/inventario.db"    # La ruta para crear la base de datos debe indicarse aquí
rutaBaseDatos = "inventario.db" 													  #ruta para crear el inventario en la carpeta local


############################### FUNCIÓN QUE BORRA LA TERMINAL ########################################

def borraPantalla():			#Función que borra la terminal
	if os.name == "nt":			#si el S.O es windows
		os.system("cls")
	else:
		os.system("clear")		#si el S.O. es linux o Mac

######################## FUNCIÓN QUE VALIDA OPCIONES DEL MENÚ #############################

def validar(opcion):			
	op=opcion
	while op<0 or op >7:
		borraPantalla()
		print(Fore.RED+"\t\t\t*****ERROR!!!*****")
		print(Fore.GREEN+"Ingrese una opción Válida")
		
		input(Fore.GREEN+"Presione ENTER para continuar ")
		op=menu()
	return op


######################################3 FUNCIÓN PARA SALIR DEL PROGRAMA ##################################
def salir():					
	print(Fore.RED+"¿Desea Salir? S/N")
	op2=input().lower()
	if op2 == 'n':
		op=''
		return op
	else:
		borraPantalla()#borra la terminal
		print(Fore.RED+"\n\n\t\t\t***Saliendo***")
		input(Fore.RED+"\nPRESIONE ENTER PARA SALIR")
		op=7
		return op	

#######################################    FUNCIÓN QUE MUESTRA EL MENÚ DEL PROGRAMA #############################
def menu():								
	try:
		borraPantalla()
		titulo="MENÚ TIENDA ELECTRÓNICA"
		marco='*'
		print("\t"+Fore.GREEN+marco*len(titulo))	
		print("\t"+Back.BLACK+Fore.GREEN+titulo)
		print("\t"+Fore.GREEN+marco*len(titulo))
		print(Fore.BLUE+"""
		1-Agregar Producto
		2-Mostrar Productos
		3-Actualizar Producto
		4-Eliminar Producto
		5-Buscar Producto
		6-Reporte de Stock
		""")
		print(Fore.RED+"\t\t7-SALIR")
			
		return int(input(Fore.GREEN+"Ingrese una Opción: "))
	except Exception as error:										#valida que solo se ingresen números
		print(Fore.GREEN+"Ingrese números entre 1 y 7")
		print(Fore.RED+"REINTENTE")
		return 0
		

	
#############    FUNCÍON QUE REGISTRA UN PRODUCTO EN EL INVENTARIO   ##########################
def registarProducto(rutaBaseDatos):
	borraPantalla()
	print(Fore.BLUE+"REGISTRAR PRODUCTO")
	op=None
	while op!='n':
		conectarBaseDatos = sqlite3.connect(rutaBaseDatos)  #conexión/crear la base de datos
		punteroBaseDatos= conectarBaseDatos.cursor()			#puntero a la base de datos para las consultas

        #el puntero crea la tabla con los campos necesarios
		punteroBaseDatos.execute("""CREATE TABLE IF NOT EXISTS productos(	
								id INTEGER PRIMARY KEY AUTOINCREMENT,
								nombre TEXT NOT NULL,
								descripcion TEXT,
								categoria TEXT NOT NULL,
								cantidad INTEGER NOT NULL,
								precio REAL NOT NULL)
								"""
								)
		punteroBaseDatos.execute("SELECT * FROM productos") #recupera los nombres de la base de datos
		inventario = punteroBaseDatos.fetchall() #guarda una lista de tuplas en inventario
		
		nombre=input("Nombre del Producto: ").lower()		#pide al usuario el nombre del producto		
		while len(nombre)==0:								#valida que el usuario no deje el nombre vacio
			print(Fore.RED+"Ingrese un nombre")
			nombre=input("Nombre del Producto: ").lower()		#pide al usuario el nombre del producto		
			
		for productos in inventario:					#verifica que el producto no exista en el inventario
			if nombre == productos[1]:
				print(Fore.RED+"El producto ya existe")
				print(f"ID: {productos[0]}\n\nProducto: {productos[1]}\n Descripción: {productos[2]}\n Categoria: {productos[3]}\n Stock: {productos[4]}\n Precio: ${productos[5]}\n")
				return 0										#Si existe lo informa y sale de la función
		#si el producto NO existe en el inventario pide los demás campos 
		descripcion=input("Descripción: \n").lower()
		cant=True										#bandera para validar el ingreso de un stock valido
		while cant:
			try:
				cantidad=int(input("Ingrese el Stock: "))
				cant=False
			except Exception:
				print(Fore.RED+"Error, Ingrese un valor")
				cant=True
		prec=True										#Bandera para validar el ingreso de un precio válido
		while prec:
			try:
				precio= float(input("Ingrese precio: "))
				prec=False
			except Exception:
				print(Fore.RED+"Error, Ingrese un valor")
				#cantidad=int(input("Ingrese el Stock: "))
				prec=True	
				
		categoria=input("Ingrese la categoria: ").lower()
		input("Presione una tecla para continuar")
		borraPantalla()
		print(Fore.GREEN+"\nVerificación de Datos: \n")					#muestra al usuario los datos ingresados
		print(f"""PRODUCTO: {nombre}\nDESCRIPCIÓN: {descripcion}\nSTOCK : {cantidad}\nPRECIO:$ {precio}\nCATEGORÍA: {categoria}""")
		print(f"\n\nDesea ingresar el producto {nombre.upper()} al Inventario s/n: ")
		opcion=input().lower()															#Si el usuario verifica los datos se carga en la base de datos
		while opcion!='s' and opcion!='n':												#valida que lo ingresado solo sea S o N
				print("Error, ingrese s o n")
				opcion=input().lower()
		if opcion == 's':
			orden= "INSERT INTO productos(nombre,descripcion,categoria,cantidad,precio) VALUES(?,?,?,?,?)" #orden que crea un nuevo registro en la base de datos
			datos= (nombre, descripcion,categoria, cantidad, precio) #datos de los campos en la base de datos
			punteroBaseDatos.execute(orden, datos) #ejecuta la orden con los datos
			conectarBaseDatos.commit() #escribe los cambios en la base de datos
			print(f"\nEl producto {nombre.upper()} ha sido ingresado al INVENTARIO\n")   #informa al usuario el exito
			init(autoreset=True)

		if opcion == 'n':											#si no se aprueba no se guarda nada y se informa
			print(Fore.RED+"Producto NO guardado")
		op=input(Fore.GREEN+"Desea ingresar otro producto s/n: ").lower()		#pregunta si quiere ingresar otro producto
	conectarBaseDatos.close()                                      #cierra la conexíon con la base de datos										
	
			
#################     FUNCIÓN QUE MUESTRA EL INVENTARIO COMPLETO ########################################		

def mostrarProducto(rutaBaseDatos):
	borraPantalla()
	print(Fore.BLUE+"MOSTRAR INVENTARIO")
	input("Presione una tecla para continuar")
	borraPantalla()
	try:
		conectarBaseDatos = sqlite3.connect(rutaBaseDatos)  #conexión/crear la base de datos
		punteroBaseDatos= conectarBaseDatos.cursor()			#puntero a la base de datos para las consultas
		punteroBaseDatos.execute("SELECT * FROM productos")
		inventario= punteroBaseDatos.fetchall()  #descarga una lista de tuplas en INVENTARIO
		
		if len(inventario)==0:							#Si el inventario está vacio, lo informa y sale de la función
			print(Fore.RED+"No hay productos para mostrar")
			return 0
		print(Fore.BLUE+"INVENTARIO")
		for producto in inventario:			#recorre el inventario para mostrar los datos
			print(f"\nID del Producto= {producto[0]} ")
			print(f"Nombre: {producto[1]}")
			print(f"Descripción: {producto[2]}")
			print(f"Categoria: {producto[3]}")
			print(f"Stock: {producto[4]} unidades")
			print(f"Precio Unitario: ${producto[5]}\n")
	except Exception as error:								#si hay un error con la base de datos lo informa
		print(Fore.RED+"Error en Base de Datos")
		conectarBaseDatos.close()
	finally:			
		conectarBaseDatos.close()

	
#########################   FUNCIÓN QUE ACTUALIZA EL STOCK DE UN PRODUCTO ####################################
		

def actualizarProducto(rutaBaseDatos):
	borraPantalla()
	noExiste=True						#bandera que indica que el producto no existe en el inventario
	op=''
	print(Fore.BLUE+"ACTUALIZAR STOCK")

	try:
		conectarBaseDatos = sqlite3.connect(rutaBaseDatos)  #conexión/crear la base de datos
		punteroBaseDatos= conectarBaseDatos.cursor()			#puntero a la base de datos para las consultas
		punteroBaseDatos.execute("SELECT * FROM productos")
		inventario= punteroBaseDatos.fetchall()  #descarga una lista de tuplas en INVENTARIO
		if len(inventario)==0:							#Si el inventario está vacio, lo informa y sale de la función
			print(Fore.RED+"No hay productos para actualizar")
			return 0 
		producto= input("Ingrese el nombre del producto: ")   #pide al usuario el nombre del producto
		while len(producto)==0:
			print(Fore.RED+"Error, Debe ingresar un nombre de producto")
			producto= input(Fore.GREEN+"Ingrese el nombre del producto: ")   #pide al usuario el nombre del producto

			
		for productos in inventario:
			if producto==productos[1]:
				print(Fore.GREEN+"PRODUCTO ENCONTRADO\n")
				print(f"Nombre: {productos[1]}")
				print(f"Descripción: {productos[2]}")
				print(f"Categoría: {productos[3]}")
				print(f"Stock: {productos[4]} Unidades")
				print(f"Precio Unitario: ${productos[5]}\n")
				stc=True										#valída que el ingreso del stock sea válido
				while stc:
					try:
						stock=int(input("Nuevo Stock: "))						#pide el nuevo valor del stock
						stc=False
					except Exception:
						print(Fore.RED+"Ingrese un Stock Válido")
						stc=True
						
				orden="UPDATE productos SET cantidad = ? WHERE id = ?"	#orden para el puntero a la base de datos
				datos= (stock, productos[0])							#datos: stock nuevo e id del producto
				punteroBaseDatos.execute(orden, datos)
				conectarBaseDatos.commit()
				conectarBaseDatos.close()
				print(f"Stock de {producto.upper()} ACTUALIZADO a {stock} unidades") 
				noExiste=False															#cambia la bandera a FALSE ya que el producto Si existe
				break
	except Exception as error:						#si hay un error con la base de datos lo informa
		print(Fore.RED+"Error en Base de Datos")
		#input(Fore.GREEN+" Presione Enter para volver al Menú")
		return 0
	if noExiste:												#si el producto no existe lo informa y da la opción de ingresarlo al inventario
		print(Fore.RED+"El producto no está en el inventario")
		op=input(Fore.GREEN+"Desea registar el producto? s/n: ").lower()	#invita al usuario a registrar ese producto
	if op=='s':
		registarProducto(rutaBaseDatos)							#llama a la función de Registro
		

############## FUNCIÓN QUE ELIMINA UN PRODUCTO ##################	

def eliminarProducto(rutaBaseDatos):
	op='s'
	noExiste=True						#bandera que indica si el producto existe o no
	mensaje="El producto no Existe"
	borraPantalla()
	print(Fore.BLUE+"ELIMINAR PRODUCTO")

	try:
		conectarBaseDatos = sqlite3.connect(rutaBaseDatos)  #conexión/crear la base de datos
		punteroBaseDatos= conectarBaseDatos.cursor()			#puntero a la base de datos para las consultas
		punteroBaseDatos.execute("SELECT * FROM productos")
		inventario= punteroBaseDatos.fetchall()  #descarga una lista de tuplas en INVENTARIO	
		

		if len(inventario)==0:							#Si el inventario está vacio, lo informa y sale de la función
			print(Fore.RED+"No hay productos para Eliminar")
			return 0	
		while op=='s':
			if len(inventario)==0:							#Si el inventario está vacio, lo informa y sale de la función
				print(Fore.RED+"No hay productos para Eliminar")
				return 0
			producto= input("Ingrese el nombre del producto: ")   #pide al usuario el nombre del producto a eliminar
			while len(producto)==0:
				print(Fore.RED+"Error, Debe ingresar un nombre de producto")
				producto= input(Fore.GREEN+"Ingrese el nombre del producto: ")   #pide al usuario el nombre del producto
			for productos in inventario:
				if producto== productos[1]:
					noExiste=False									#cambia la bandera ya que el producto Si existe
					borraPantalla()
					print(Fore.GREEN+"PRODUCTO ENCONTRADO\n")
					print(f"Nombre: {productos[1]}")
					print(f"Descripción: {productos[2]}")
					print(f"Categoría: {productos[3]}")
					print(f"Stock: {productos[4]} Unidades")
					print(f"Precio Unitario: ${productos[5]}\n")
					borrar=input(f"Desea Eliminar el producto {productos[1]}? s/n: ").lower()  
					while borrar!='s' and borrar!='n':											#valida la opción
						print(Fore.RED+"Error, ingrese s o n")
						op=input().lower()
						borraPantalla()
						 
					if borrar == 's':											#si el producto existe pide verificación para eliminar
						orden= "DELETE FROM productos WHERE id = ?"				#orden para el puntero a la base de datos
						datos= (productos[0],)									#datos para el puntero
						punteroBaseDatos.execute(orden, datos)					#ejecuta la orden con los datos
						conectarBaseDatos.commit()
						conectarBaseDatos.close()
						print(f"\nProducto: {producto.upper()}")
						print(Fore.RED+" ELIMINADO")
						break
					else:
						borraPantalla()
						print(Fore.RED+"Atención!!!\n")									 #si no hay verificación se anula la eliminación 
						print(f"El producto {producto.upper()} NO fue eliminado")
						break
			if noExiste:															# si no existe se informa
				borraPantalla()
				print(Fore.RED+mensaje)
			op=input(Fore.GREEN+"Desea Eliminar otro producto? s/n: ").lower()					#pregunta si quiere eliminar otro producto
	except Exception as error:				#si hay un error con la base de datos lo informa
		print(Fore.RED+"Error en Base de Datos")
		conectarBaseDatos.close()
	
	finally:			
		conectarBaseDatos.close()


#############################FUNCIÓN QUE BUSCA UN PRODUCTO EN EL INVENTARIO###########################
def buscarProducto(rutaBaseDatos):
	borraPantalla()
	mensaje="El producto NO se encuentra en el inventario\n"
	noExiste=True												#bandera que indica si el producto existe o no
	buscar=True													#bandera que indica si el bucle principal sigue o no
	print(Fore.BLUE+"BUSCAR PRODUCTO")
	try:
		conectarBaseDatos = sqlite3.connect(rutaBaseDatos)  #conexión/crear la base de datos
		punteroBaseDatos= conectarBaseDatos.cursor()			#puntero a la base de datos para las consultas
		punteroBaseDatos.execute("SELECT * FROM productos")
		inventario= punteroBaseDatos.fetchall()  #descarga una lista de tuplas en INVENTARIO
		if len(inventario)==0:
			print(Fore.RED+"No hay productos para Buscar")
			return 0
		while buscar:
			producto= input("Ingrese el nombre del producto: ")					#pide al usuario el nombre del producto a buscar
			while len(producto)==0:												#valida que el usuario ingrese un nombre
				print(Fore.RED+"Error, Debe ingresar un nombre de producto")
				producto= input(Fore.GREEN+"Ingrese el nombre del producto: ")   #pide al usuario el nombre del producto
			for productos in inventario:
				if producto==productos[1]:
					print(Fore.GREEN+"PRODUCTO ENCONTRADO\n")
					print(f"ID: {productos[0]}")
					print(f"Nombre: {productos[1]}")
					print(f"Descripción: {productos[2]}")
					print(f"Categoría: {productos[3]}")
					print(f"Stock: {productos[4]} Unidades")
					print(f"Precio Unitario: ${productos[5]}\n")
					noExiste=False												#si lo encuentra pasa noExiste a FALSO
					break
			if not noExiste:													#Si la variable noExiste=False entonces NOT noExiste = True
				print(f"Desea realizar una operación sobre el producto: {productos[1]} s/n: ")	#pregunta al usuario si desea hacer algo con el registro encontrado
				op=input().lower()
				while op!='s' and op!='n':			#valida opción por si o por no S o N
					print(Fore.RED+"Error, ingrese s o n")
					op=input().lower()
					borraPantalla()
				if op=='s':							#si la opción es si, ofrece dos posibilidades
					borraPantalla()
					print(Fore.BLUE+"OPCIONES")
					print(Fore.GREEN+"1-Actualizar Stock")
					print(Fore.GREEN+"2-Eliminar Producto")
					op1=input("Elija una opción: ");
					while op1!='1' and op1!= '2':			#validación 
						print(Fore.RED+"Error, ingrese 1 o 2")
						op1=input().lower()
					if op1=='1':
						actualizarProducto(rutaBaseDatos)						#opción 1 cambiar Stock
						borraPantalla()
						op=input("\nDesea Buscar otro producto? s/n: ").lower()	 #pregunta al usuario si quiere buscar otro producto
						while op!='s' and op!='n':
							print(Fore.RED+"Error, ingrese s o n")
							op=input().lower()
						if op=='s':					# si la opción es Si, cambia buscar a True para quedarse en el bucle while principal
							buscar=True
						if op=='n':
							buscar= False			# si la opción es No, cambia buscar a False para salir del bucle while principal
					if op1=='2':
						eliminarProducto(rutaBaseDatos)				#opción 2 Eliminar producto
						borraPantalla()
						op=input("\nDesea Buscar otro producto? s/n: ").lower()	
						while op!='s' and op!='n':
							print(Fore.RED+"Error, ingrese s o n")
							op=input().lower()
						if op=='s':
							buscar=True
						if op=='n':
							buscar= False
				if op=='n':										#si la opción es No, ofrece buscar otro producto o salir de la función
					print("Desea buscar otro producto? s/n: ")
					op=input().lower()
					while op!='s' and op!='n':
						print(Fore.RED+"Error, ingrese s o n")
						op=input().lower()
						if op=='s':
							buscar=True
						if op=='n':
							buscar= False
			if noExiste:											#si no lo encuentra entonces noExiste es verdadero y lo informa
				print("\n")
				print(Fore.RED+mensaje)										#imprime el mensaje de la variable mensaje
				op=input("\nDesea Buscar otro producto? s/n: ").lower()	
				while op!='s' and op!='n':
					print(Fore.RED+"Error, ingrese s o n")
					op=input().lower()
				if op=='s':
					buscar=True
				if op=='n':
					buscar= False
					
	except Exception as error:									#si hay un error con la base de datos lo informa
		print(Fore.RED+"Error en Base de Datos")
		#print(f"Error en la base de datos: {error}")
		conectarBaseDatos.close()
	
	finally:			
		conectarBaseDatos.close()
	
	
		


##################### FUNCIÓN QUE GENERA UN REPORTE DE BAJO STOCK #############################

def reporteBajoStock(rutaBaseDatos):
	borraPantalla()
	print(Fore.BLUE+"REPORTE DE BAJO STOCK")
	stockOk=True							#bandera que valida si el stock está por encima del parámetro de umbral
	try:
		conectarBaseDatos = sqlite3.connect(rutaBaseDatos)  #conexión/crear la base de datos
		punteroBaseDatos= conectarBaseDatos.cursor()			#puntero a la base de datos para las consultas
		punteroBaseDatos.execute("SELECT * FROM productos")
		inventario= punteroBaseDatos.fetchall()  #descarga una lista de tuplas en INVENTARIO
		borraPantalla()
		if len(inventario)==0:									#Si el inventario está vacio, lo informa y sale de la función
			print(Fore.RED+"No hay productos para reportar")
			return 0
		
		umb=True										#bandera para validar el ingreso de un umbral valido
		while umb:
			try:
				umbral=int(input("Ingrese el parámetro de Stock Bajo: "))
				umb=False
			except Exception:
				print(Fore.RED+"Error, Ingrese un valor")
				umb=True
	
		for productos in inventario:
			if productos[4]<=umbral:								#compara los stock de cada producto con el criterio de busqueda
				print(Fore.RED+"Producto con bajo Stock:\n")
				print(f"ID: {productos[0]}\n Producto: {productos[1]}\n Stock: {productos[4]}")	#si hay productos con bajo stock lo informa
				stockOk=False																   #cambia a False por existir productos con bajo Stock
		if stockOk:				#si ningún producto está por debajo del stock umbral lo informa				
				print(f"Ningun producto está por debajo del Stock Minimo de {umbral} unidades") #si no hay productos con bajo stock lo informa	
	except Exception as error:									#si hay un error con la base de datos lo informa
		print(Fore.RED+"Error en Base de Datos")
		conectarBaseDatos.close()
	finally:			
		conectarBaseDatos.close()			
				
			
############################ FUNCIÓN PRINCIPAL ####################################################
def main():
	texto= "PROYECTO FINAL CURSO PYTHON 2024"
	print("\n\n")
	print(Fore.RED+"\t\t"+"*"*len(texto))
	print("\n\t\t"+Fore.GREEN+texto)
	print("\n\t\t"+Fore.RED+"\t\tby Pablo Toledo")
	print(Fore.RED+"\t\t"+"*"*len(texto))

	input("PRESIONE UNA TECLA PARA CONTINUAR")
	op=''
	while op!= 7:								#Bucle que maneja la ejecución del programa, si se ingresa la opción 7 sale del programa
		op=validar(menu())
		if op==1:
			registarProducto(rutaBaseDatos)			#Llamado a la función que registra productos
			input("Presione Enter para continuar")
		elif op==2:
			mostrarProducto(rutaBaseDatos)			#Llamado a la Función que muestra todos los productos del inventario
			input("Presione Enter para continuar")
		elif op==3:
			actualizarProducto(rutaBaseDatos)			#Llamado a la función que actualiza el stock de un producto
			input("Presione Enter para continuar")
		elif op==4:
			eliminarProducto(rutaBaseDatos)				#Llamado a la función que Elimina productos
			input("Presione Enter para continuar")
		elif op==5:
			buscarProducto(rutaBaseDatos)				#Llamado a la función que busca un producto y tiene la capacidad de eliminar o actualizar el stock
			input("Presione Enter para continuar")
		elif op==6:
			reporteBajoStock(rutaBaseDatos)				#Llamado a la función que controla el stock mediante un valor de stock umbral
			input("Presione Enter para continuar")
		elif op==7:
			op=salir()									#Llamado a la función que sale del programa
		else:
			input(Fore.RED+"Error,"+Fore.GREEN+" presione Enter para continuar")
			
		
	return 0

############################# LLAMADO A LA FUNCIÓN PRINCIPAL ##########################################
main()   
