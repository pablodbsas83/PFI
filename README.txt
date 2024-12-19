Proyecto Integrador Final
Curso Introducción a Python 2024


El proyecto consta de crear un programa en Python que gestione un inventario mediante una base de datos SQlite
El programa consta de 7 (siete) funciones principales que manejan los datos:

			registarProducto(): crea una tabla en la base datos y registra un producto en el inventario			                    
			mostrarProducto((): muestra todos los productos ingresados
			actualizarProducto(): actualiza el stock de un producto elegido
			eliminarProducto(): elimina un producto del inventario
			buscarProducto() :busca un producto en particular y tiene la capacidad de actualizar el stock y de eliminar el producto
			reporteBajoStock(): recibe un umbral de stock y compara con los stock de cada producto, duvuelve los productos que están bajo ese umbral
			salir()	:sale del programa
Estas funciones reciven un parametro que corresponde a la ruta de la base de datos
"inventario.db"

			
El programa tambien tiene 3 (tres) funciones secundarias 
        
            menu(): muestra el menú del programa
            validar(): valida las opciones para el menú
            borraPantalla() :borra la consola, reconoce el sistema operativo y usa los comandos adecuados

Se usaron las estructuras Try-Execept para manejar los errores de base de datos y los errores propios de la ejecución del programa, 
tales como los ingresos erroneos del usuario, tambien se usaron variables tipo boolean para manejar banderas lógicas en los distintos 
flujos de control

Los Archivos de este PFI son:
Este archivo README
un archivo "inventario.db"
un Archivo de código fuente en python "proyectoFinalDB.py"

El Archivo "inventario.db" no es necesario para el ejecución del programa, ya que el programa está preparado para generarlo, 
solo basta ingresar a la opción 1 del menú "Agregar Producto" para que el archivo se genere en la ruta específica que se declare en la 
variable:
 rutaBaseDatos = "inventario.db" este archivo.db se crea en el mismo directorio donde se encuentra en archivo proyectoFinalDB.py 
También puede ser indicada la ruta completa por ejemplo:
rutaBaseDatos = "/curso/Python/proyectoFinal/inventario.db" (entorno linux)

El programa fue desarrollado usando las herramientas del curso introducción a Python
se usaron :
            *Estructuras de control
            *Llamadas al usuario (función input())
            *uso de listas
            *uso de sqlite
            *librerias OS y Colorama
Ante dudas o bugs enviar un e-mail a: 

pablodbsas83@gmail.com

Este programa fue desarrollado mediante software libre

proyectoFinalDB_v2.4
  
#  Copyright 2024 Pablo Toledo <pablodbsas83@gmail.com>
#  



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



            




