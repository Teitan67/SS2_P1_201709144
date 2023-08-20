from os import system
import os
from tkinter.filedialog import askopenfilename
import csv
from databases.SQLServer import runQuery
from databases.Querys import borrarModelo,crearModelo,cargarInformacion,consulta1,consulta2,consulta4,consulta5,consulta6,consulta7,consulta8,consulta9,consulta10

import asyncio
loop = asyncio.get_event_loop()

class Menu:

    __opciones=[]
    __registros=[]

    def __init__(self) -> None:
        self.opciones=[
            'Borrar modelo',
            'Crear modelo',
            'Extraer informacion',
            'Cargar informacion',
            'Realizar consultas',
            'Acerca de',
            'Salir'
        ]

        self.subOpciones=[
            'Consulta ',
            'Consulta ',
            'Consulta ',
            'Consulta ',
            'Consulta ',
            'Consulta ',
            'Consulta ',
            'Consulta ',
            'Consulta ',
            'Consulta ',
            'Regresar'
        ]
    
    def mostrar(self,error:bool,mainManu) -> None:
        system("cls")
        
        print('         __________________________           ')
        print('        |        PRACTICA 1        |          ')
        print('        |        PROCESO ETL       |          ')
        print('        |--------------------------|          \n')

        i = 0

        if(mainManu):
            for opcion in self.opciones:
                i = i + 1
                print("\t",i," - "+opcion)
        else:
            for opcion in self.subOpciones:
                i = i + 1
                print("\t",i," - "+opcion)
        if(error):
            print('\n            OPCION INCORRECTA!!               ')

        opcion = input('\nEscribe tu opcion: ')
        if(mainManu):
            self.ejecutarOpcion(opcion)
        else:
            self.ejecutarSubOpcion(opcion)
    
    def pausa(self,call):
        espera = input('Presiona cualquier tecla para continuar...\n')     
        self.mostrar(False,call)
    def ejecutarOpcion(self,opcion:str) -> None:
        if(opcion=='7'):
            pass
        elif(opcion=='3'):
            noEncabezado = False
            for r in self.__registros:
                
                query = """
                    insert into GeneralData(
                        EntregaId ,
                        Dia ,
                        Mes,
                        Anio,
                        NombreCliente,
                        Direccion,
                        NomreEmpleadoEntrega,
                        PuestoEmpleadoEntrega,
                        CiudadEntrega,
                        NombreProducto,
                        Descripcion,
                        Peso,
                        TiempoEntrega,
                        EstadoEntrega,
                        CostoEnvio,
                        PrecioProducto
                    )values(
                        '"""+ (r[0]  if(r[0]!=None) else '') +"""',
                        '"""+ (r[1]  if(r[1]!=None) else '') +"""',
                        '"""+ (r[2]  if(r[2]!=None) else '') +"""',
                        '"""+ (r[3]  if(r[3]!=None) else '') +"""',
                        '"""+ (r[4]  if(r[4]!=None) else '') +"""',
                        '"""+ (r[5]  if(r[5]!=None) else '') +"""',
                        '"""+ (r[6]  if(r[6]!=None) else '') +"""',
                        '"""+ (r[7]  if(r[7]!=None) else '') +"""',
                        '"""+ (r[8]  if(r[8]!=None) else '') +"""',
                        '"""+ (r[9]  if(r[9]!=None) else '') +"""',
                        '"""+ (r[10]  if(r[10]!=None) else '') +"""',
                        '"""+ (r[11]  if(r[11]!=None) else '') +"""',
                        '"""+ (r[12]  if(r[12]!=None) else '') +"""',
                        '"""+ (r[13]  if(r[13]!=None) else '') +"""',
                        '"""+ (r[14]  if(r[14]!=None) else '') +"""',
                        '"""+ (r[15]  if(r[15]!=None) else '') +"""'
                    )
                """
                if(noEncabezado):
                    res = runQuery(query)
                noEncabezado=True
            
            espera = input('Presiona cualquier tecla para continuar...\n')  
            contador = 1   
            for elemento in cargarInformacion:
                res = runQuery(elemento)
                espera = input('Tablas insertadas '+contador+'\n')    
                contador=contador+1 
            self.mostrar(False,True)           
        elif(opcion=='4'):
            filename = askopenfilename()

            with open(filename) as csv_file:
                csv_doc = csv.reader(csv_file, delimiter=';')
                line_count = 0
                for row in csv_doc:
                    self.__registros.append(row)
                    line_count += 1
                    
                print(f'Procesadas {line_count} lineas.')
            self.pausa(True)
        elif(opcion=='6'):
            espera = input('\n\tUSAC - SS2\n\tPractica 1\n\tDesarrollado por Oscar Leon 201709144 (Teitan67)...')
            self.mostrar(False,True)
        elif(opcion=='1'):
            print("Eliminando modelo...")
            for query in borrarModelo:
                res = runQuery(query)
            self.pausa(True)     
        elif(opcion=='2'):
            print("Creando modelo...")
            for  query in crearModelo :
                runQuery(query)
            self.pausa(True)
        elif(opcion=='5'):
            self.mostrar(True,False)
        
        else:
            self.mostrar(True,True)

    def ejecutarSubOpcion(self,opcion:str) -> None:
        if(opcion=='1'):
            resultado =  runQuery(consulta1)
            
            print ("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15} ".format("Registros", "Clientes", "Direcciones", "Productos","Fechas","Empleados","EstadosEntregas","Entregas"))
            if(len(resultado)>0):
                print ("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15} ".format(resultado[0][0], resultado[0][1],resultado[0][2], resultado[0][3],resultado[0][4],resultado[0][5],resultado[0][6],resultado[0][7]))
                

            espera = input('Presiona cualquier tecla para continuar...\n')     
            self.mostrar(True,False)
        elif(opcion=='2'):
            resultado =  runQuery(consulta2)
            print ("{:<15} {:<15} ".format("Año", "Cantidad de Tsunamis"))
            if(len(resultado)>0):
                for row in resultado:
                    print ("{:<15} {:<15} ".format(row[0], row[1]))
                
            espera = input('Presiona cualquier tecla para continuar...\n')     
            self.mostrar(True,False)
        elif(opcion=='4'):
            resultado =  runQuery(consulta4)
            print ("{:<15} {:<15} ".format("Pais", "Total damage"))
            if(len(resultado)>0):
                for row in resultado:
                    print ("{:<15} {:<15} ".format(row[0], row[1]))
                
            espera = input('Presiona cualquier tecla para continuar...\n')     
            self.mostrar(True,False)
        elif(opcion=='5'):
            resultado =  runQuery(consulta5)
            print ("{:<15} {:<15} ".format("Pais", "Total muertes"))
            if(len(resultado)>0):
                for row in resultado:
                    print ("{:<15} {:<15} ".format(row[0], row[1]))
                
            espera = input('Presiona cualquier tecla para continuar...\n')     
            self.mostrar(True,False)
        elif(opcion=='6'):
            resultado =  runQuery(consulta6)
            print ("{:<15} {:<15} ".format("Anios", "Total muertes"))
            if(len(resultado)>0):
                for row in resultado:
                    print ("{:<15} {:<15} ".format(row[0], row[1]))
                
            espera = input('Presiona cualquier tecla para continuar...\n')     
            self.mostrar(True,False)
        elif(opcion=='7'):
            resultado =  runQuery(consulta7)
            print ("{:<15} {:<15} ".format("Anio", "Tsunamis"))
            if(len(resultado)>0):
                for row in resultado:
                    print ("{:<15} {:<15} ".format(row[0], row[1]))
                
            espera = input('Presiona cualquier tecla para continuar...\n')     
            self.mostrar(True,False)
        elif(opcion=='8'):
            resultado =  runQuery(consulta8)
            print ("{:<15} {:<15} ".format("Casas", "Total Casas destruidas"))
            if(len(resultado)>0):
                for row in resultado:
                    print ("{:<15} {:<15} ".format(row[0], row[1]))
                
            espera = input('Presiona cualquier tecla para continuar...\n')     
            self.mostrar(True,False)
        elif(opcion=='9'):
            resultado =  runQuery(consulta9)
            print ("{:<15} {:<15} ".format("Pais", "Total Casas dañadas"))
            if(len(resultado)>0):
                for row in resultado:
                    print ("{:<15} {:<15} ".format(row[0], row[1]))
                
            espera = input('Presiona cualquier tecla para continuar...\n')     
            self.mostrar(True,False)
        elif(opcion=='10'):
            resultado =  runQuery(consulta10)
            print ("{:<25} {:<25} ".format("Pais", "Promedio max de holas"))
            if(len(resultado)>0):
                for row in resultado:
                    print ("{:<25} {:<25} ".format(row[0], row[1]))
                
            espera = input('Presiona cualquier tecla para continuar...\n')     
            self.mostrar(True,False)
        elif(opcion=='11'):
            self.mostrar(False,True)
        else:
            self.mostrar(True,False)


