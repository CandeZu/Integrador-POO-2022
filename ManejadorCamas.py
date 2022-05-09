from Camas import Cama
import csv

class ManejadorCama:
    __camas = []

    def __init__(self):
        self.__camas = []
    
    def GenerarLista(self):
        archivo = open("camas.csv")
        reader = csv.reader(archivo, delimiter=";")
        bandera=True
        for fila in reader:
            if bandera:
                bandera = not bandera
            else:
                id = int(fila[0])
                habitacion = int(fila[1])
                estado = fila[2]
                nyapaciente = fila[3]
                diagnostico = fila[4]
                fechainter = fila[5]
                fechadealta = fila[6]
                cama = Cama(id, habitacion, estado, nyapaciente, diagnostico, fechainter, fechadealta)
                self.__camas.append(cama)
        archivo.close()
    
    def ListarCamas(self):
        for cama in self.__camas:
            print(cama)
            print("\n".center(20,"-"))
