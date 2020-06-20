import os
import sys
import requests
import json
from pathlib import Path

def limpiar():
	os.system("cls")

#GESTION CANDIDATO
def gestionC():
	limpiar()
	print("GENTIONAR CANDIDATO ")
	print("1- Agregar candidato")
	print("2- Modificar candidato")
	print("3- Eliminar candidato")
	tmh = input("Que opcion desea: ")
	if(tmh == "1"):
		agregarc()
	elif(tmh == "2"):
		modificarc()
	elif(tmh == "3"):
		eliminar()
	else:
		print("Amigo debe de elegir algo valido")
		menu()

#Aqui se agregan los candidatos
def agregarc():
	limpiar()
	print("                                        =============VAMOS A AGREGAR UN CANDIDATO=========== ")
	cedula = input("Cual es la cedula del candidato?: ")
	nombre =input("cual es el nombre del candidato?: ")
	apellido = input("cual es el apellido del candidato?: ")
	fechaN   = input("cual es la fecha de nacimiento del candidato?ejemplo:dd/mm/aaaa ")
	tipodS = input("cual es el tipo de sangre?: ")
	partido = input("cual es partido del candidato? ")
	size = input("cual es el size del candidato?: ")
	telefono = input("cual es el telefono del candidato?" )
	celular = input("cual es el numero de celular del candidato? ")
	email = input("cual es el email del candidato?: ")
	direccion = input("cual la direccion del candidato?: ")
	personadc = input("cual es la persona de contacto?: ")
	telefonodc = input("cual es el telefono de contacto?: ")
	cont = cedula +"~"+nombre+"~"+apellido+"~"+fechaN+"~"+tipodS+"~"+partido+"~"+size+"~"+telefono+"~"+celular+"~"+email+"~"+direccion+"~"+personadc+"~"+telefonodc
	rs = requests.post("http://adamix.net/api/itla/registrarDato",data={'matricula': '20186212', 'clave': '12345', 'contenido': cont })
	print(rs)
	input("Datos guardados, presione enter para continuar")
	menu()

#MODIFICAR	
def modificarc():
	limpiar()
	datos = requests.get("http://adamix.net/api/itla/misDatos/20186212/12345").text
	datos = datos.split("\n")

	print("Esto son los candidatos\n")
	for f in datos:
	    fila = f.split("&")
	    candi = fila[2]
	    candi = candi.split("~")
	    print("ID: "+fila[0])
	    print("Cedula del candidato: " + candi[1])
	    print("Nombre del candidato: " + candi[2])
	    print("------------------------------------------------------------------------------------------------------- \n")
	    pass
	print("Modifique el candidato\n")
	num = input("Elija un candidato introduciendo ID: " + " ")
	for h in datos:
		high = h.split("&")
		cc = high[2]
		cc = cc.split("~")
		if num == high[0]:
			cc[0]
			cc[1]
			cc[2]
			cc[3]
			cc[4]
			cc[5]
			cc[6]
			cc[7]
			cc[8]
			cc[9]
			cc[10]
			cc[11]
			cc[12]
			cedula = input("La cedula del candidato es: " + cc[0] + " Esciba la cedula si desea reemplazarla: ") 
			if not cedula:
				cedula = cc[0]
			nombre =input("El nombre del candidato es: "+ cc[1] + " Esciba la nombre si desea reemplazarla: ")
			if not nombre:
				nombre = cc[1]
			apellido = input("El apellido del candidato es: "+ cc[2] + " Esciba la apellido si desea reemplazarlo: ")
			if not apellido:
				apellido = cc[2]
			fechaN   = input("La fecha de nacimiento del candidato es: "+ cc[3] + " Esciba la fecha de nacimiento si desea reemplazarla: ejemplo:dd/mm/aaaa ")
			if not fechaN:
				fechaN = cc[3]
			tipodS = input("El tipo de sangre es: "+ cc[4] + " Esciba el tipo de sangre si desea reemplazarlo, sino preione enter: ")
			if not tipodS:
				tipodS = cc[4]
			partido = input("El partido del candidato es: "+ cc[5] + " Esciba el partido si desea reemplazarlo, sino preione enter: ")
			if not partido:
				partido = cc[5]
			size = input("El size del candidato es: "+ cc[6] + " Esciba el size si desea reemplazarlo, sino preione enter: ")
			if not size:
				size = cc[6]
			telefono = input("El telefono del candidato es: "+ cc[7] + " Esciba el telefono si desea reemplazarlo, sino preione enter: ")
			if not telefono:
				telefono = cc[7]
			celular = input("El numero de celular del candidato es: "+ cc[8] + " Esciba el celular si desea reemplazarlo, sino preione enter: ")
			if not celular:
				celular = cc[8]
			email = input("El Email del candidato es: "+ cc[9] + " Esciba el Email si desea reemplazarlo, sino preione enter: ")
			if not email:
				email = cc[9]
			direccion = input("L direccion del candidato es: "+ cc[10] + " Esciba la direccion si desea reemplazarla, sino preione enter: ")
			if not direccion:
				direccion = cc[10]
			personadc = input("La persona de contacto es: "+ cc[11] + " Esciba la persona si desea reemplazarla, sino preione enter, sino preione enter: ")
			if not personadc:
				personadc = cc[11]
			telefonodc = input("El telefono de contacto es: "+ cc[12] + " Esciba el telefono de contacto si desea reemplazarlo, sino preione enter: ")
			if not telefonodc:
				telefonodc = cc[12]
	cont = cedula +"~"+nombre+"~"+apellido+"~"+fechaN+"~"+tipodS+"~"+partido+"~"+size+"~"+telefono+"~"+celular+"~"+email+"~"+direccion+"~"+personadc+"~"+telefonodc
	rs = requests.post("http://adamix.net/api/itla/registrarDato",data={'matricula': '20186212', 'clave': '12345', 'contenido': cont })
	rs2 = requests.get("http://adamix.net/api/itla/eliminarDato/" +num+ "/12345")
	print(rs)
	print(rs2)
	input("Datos modificados, presione enter para continuar")
	menu()



#Aqui eliminammos los candidatos.
def eliminar():
	limpiar()
	print("Que candidato desea borrar.\n")
	datos = requests.get("http://adamix.net/api/itla/misDatos/20186212/12345").text
	datos = datos.split("\n")
	print("Esto son los candidatos\n")
	for f in datos:
	    fila = f.split("&")
	    candi = fila[2]
	    candi = candi.split("~")  
	    print("ID: "+fila[0])
	    print("Nombre del candidato: " + candi[1])
	    print("-------------------------------------------------------------------------------------------------------- \n")
	num = input("digite la candidato que quieres borrar: " + " ") 
	rs = requests.get("http://adamix.net/api/itla/eliminarDato/" +num+ "/12345")
	print(rs)
	print("Candidato eliminado")
	input()
	menu()



#GESTION DE ACTIVIDADES
def actividades():
	limpiar()
	num = ""
	datos = requests.get("http://adamix.net/api/itla/misDatos/20186212/12345").text
	datos = datos.split("\n")
	print("")

	print("Esto son los candidatos\n")
	for f in datos:
	    fila = f.split("&")
	    candi = fila[2]
	    candi = candi.split("~")
	    print("ID: "+fila[0])
	    print("Cedula del candidato: " + candi[0])
	    print("Nombre del candidato: " + candi[1])
	    print("---------------------------------------------------------------------------------------------------------\n") 
	    pass
	

	num = input("Elija un candidato introduciendo ID: " + " ")
	for h in datos:
		high = h.split("&")
		cc = high[2]
		cc = cc.split("~")
		if num == high[0]:
			candidatoA = cc[1] 
			print("Agregue actividad al candidato\n")
			print("A seleccionado a "+ candidatoA)
			descripcionA = input("Cual es la descripcion de la actividad?: ")
			fechaA = input("cual es la fecha de la actividad?: ")
			costoA =input("cual es el costo de la actividad?: ")
			LugarA  = input("cual es el lugar de la acividad?: ")
	cont = candidatoA+"~"+descripcionA+"~"+fechaA+"~"+costoA+"~"+LugarA
	rs = requests.post("http://adamix.net/api/itla/registrarDato",data={'matricula': '20186212', 'clave': '12346', 'contenido': cont })
	print(rs)
	input("Datos guardados, presione enter para continuar")
	menu()

	
			


#REPORTES DE CANDIDATOS
def reportesc():
	limpiar()
	print("                               ======================REPORTES DE CANDIDATOS========================= ")
	print("1- Listado de candidatos")
	print("2- Listado de actividades")
	print("3- Listado de candidatos con signo zodiacal")
	print("4- Exportar candidato")
	tmq = input("Que opcion desea: ")
	if(tmq == "1"):
		listaC()
	elif(tmq == "2"):
		listaA()
	elif(tmq == "3"):
		listazodiaco()
	elif(tmq == "4"):
		exportar()
	else:
		print("Amigo debe de elegir algo valido")
		menu()


#LISTA DE CANDIDATOS
def listaC():
	limpiar()
	print("                                  =============ESTOS SON LOS CANDIDATOS EXISTENTES===========")
	datos = requests.get("http://adamix.net/api/itla/misDatos/20186212/12345").text
	datos = datos.split("\n")
	print("aqui estan")
	for f in datos:
		fila = f.split("&")
		candi = fila[2]
		candi = candi.split("~")
		print("Cedula: " + candi[0])
		print("Nombre: " + candi[1])
		print("Apellido: " + candi[2])
		print("Fecha de nacimiento: " + candi[3])
		print("Tipo de sangre: " + candi[4])
		print("Partido: " + candi[5])
		print("Size del traje: " + candi[6])
		print("telefono: " + candi[7])
		print("Celular: " + candi[8])
		print("Email: " + candi[9])
		print("Direccion: " + candi[10])
		print("Persona de contacto: " + candi[11])
		print("Telefono de contacto: " + candi[12])
		print("-------------------------------------------------------------------------------------------------------- \n")
	input("presione enter para continuar")
	menu()

#LISTA DE ACTIVIDADES
def listaA():
	limpiar()
	print("                                     =============ESTOS SON LAS ACTIVIDADES EXISTENTES===========")
	datos = requests.get("http://adamix.net/api/itla/misDatos/20186212/12346").text
	datos = datos.split("\n")
	for f in datos:
		fila = f.split("&")
		candi = fila[2]
		candi = candi.split("~")
		print("Candidato: " + candi[0])
		print("Descripcion: " + candi[1])
		print("Fecha de la actividad: " + candi[2])
		print("Fecha de nacimiento: " + candi[3])
		print("Lugar de la actividad: " + candi[4])
		print("-------------------------------------------------------------------------------------------------------- \n")
	input("presione enter para continuar")
	menu() 

#LISTA DE CANDIDATO CON SIGNO ZODIACAL.	
def listazodiaco():
	limpiar()
	print("estos son los que has agregado")
	datos = requests.get("http://adamix.net/api/itla/misDatos/20186212/12345").text
	datos = datos.split("\n")
	signo = ["Capricornio","Acuario","Piscis","Aries","Tauro","Geminis","Cancer","Leo","Virgo","Libra","Escorpio","Sagitario"]
	fecha = [20, 19, 20, 20, 21, 21, 22, 22, 22, 22, 22, 21]
	print("Aqui estan los candidatos por signo zodiacal")
	for f in datos:
	    fila = f.split("&")
	    candi = fila[2]
	    candi = candi.split("~") 
	    zodiaco = candi[3]
	    zodiaco = zodiaco.split("/")
	    mes = zodiaco[1]
	    dia = zodiaco[0]
	    mes2 = int(mes)
	    dia2 = int(dia)
	    mes2 = mes2 - 1
	    if dia2 > fecha[mes2]:
	   		mes2 = mes2 + 1 
	    if mes2 == 12:
	    	mes2 = 0
	    	pass
	    print("Cedula: "+ candi[0])
	    print("Nombre del candidato: " + candi[1])
	    print("Su signo sodiacal es "+ signo[mes2])
	    print("-------------------------------------------------------------------------------------------------------- \n")
	input("presione enter para continuar")
	menu()




#EXPORTAR CANDIDATO
def exportar():
	limpiar()
	datos = requests.get("http://adamix.net/api/itla/misDatos/20186212/12345").text
	datos = datos.split("\n")
	for f in datos:
		fila = f.split("&")
		candi = fila[2]
		candi = candi.split("~")
		ubicacion = Path("C:/FELIZ/"+candi[0]+".html")
		if ubicacion.exists():
			archivo = open("C:/FELIZ/"+candi[0]+".html", "r")
			datos2 = archivo.read()
			archivo.close()
			candd2 = json.loads(datos2)
			print("Ya existe "+candi[1]+" en la carpeta FELIZ del disco local")
	

	print("Que candidato desea exportar.\n")
	datos = requests.get("http://adamix.net/api/itla/misDatos/20186212/12345").text
	datos = datos.split("\n")
	print("Esto son los candidatos\n")
	for f in datos:
	    fila = f.split("&")
	    candi = fila[2]
	    candi = candi.split("~")
	    print("ID: "+fila[0])
	    print("Cedula del candidato: " + candi[1])
	    print("Nombre del candidato: " + candi[2])
	    print("-------------------------------------------------------------------------------------------------------- \n")
	num = input("Seleccione un cadidato introduciendo la ID: " + " ")
	for h in datos:
		high = h.split("&")
		cc = high[2]
		cc = cc.split("~")
		if num == high[0]:
			infocan ="<html><titleCandidato</title><head><h2>Candidato: "+cc[1]+"</h2>Cedula: "+cc[0]+"<br> Nombre: "+cc[1]+"<br> Apellido: "+cc[2]+"<br> Tipo de sangre: "+cc[4]+"<br>Fecha de nacimiento: "+cc[3]+"<br> Partido: "+cc[5]+"<br> Size del traje: "+cc[6]+"<br>Telefono"+cc[7]+"<br> Celular: "+cc[8]+"<br>Email: "+cc[9]+"<br>Direccion: "+cc[10] +"<br> Persona de contacto: "+cc[11]+"<br> Telefono de contacto: "+cc[12]

			datos2 = json.dumps(infocan)
			f = open("C:/FELIZ/"+cc[0]+".html","w")
			f.write(datos2)
			f.close()
	print("Se exporto el candidato a la carpeta FELIZ del disco local")		
	input("presione enter para continuar")
	menu()	


#MENU PRINCIPAL
def menu():
	limpiar()
	print("                                       =============PROGRAMA DE CANDIDATOS===========\n")
	print("a- Gestionar Candidato\n")
	print("b- Gestionar Actividades\n")
	print("c- Reportes\n")
	print("d- salir\n")
	tmp = input("Que opcion desea: ")
	if(tmp == "a"):
		gestionC()
	elif(tmp == "b"):
		actividades()
	elif(tmp == "c"):
		reportesc()
	elif(tmp =="d"):
		limpiar()
		print("Adios :")
		sys.exit()
	else:
		print("Amigo debe de elegir algo valido")
		menu()
	input()
menu()





