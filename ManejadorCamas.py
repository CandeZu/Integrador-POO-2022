from Camas import Cama
from Medicamentos import Medicamento
import csv
import numpy as np
from datetime import date
import os

class ManejadorCama():
    __incremento = 5
    __cantidad = 0
    __dimension = 30
    __camas = None

    def __init__(self,dimension = 30, incremento = 5):
        self.__incremento = incremento
        self.__camas = np.empty(dimension,dtype = Cama)
    
    def agregarCamas(self,Cama):

        if (self.__cantidad == self.__dimension):
            self.__dimension += self.__incremento
            self.__camas.resize(self.__dimension)
        self.__camas[self.__cantidad] = Cama
        self.__cantidad += 1
    
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
                self.agregarCamas(cama)
        archivo.close()
    
    def ListarCamas(self):
        for cama in self.__camas:
            if cama == None:
                continue
            print(cama)
            print("\n".center(20,"-"))
    
    def BuscarPaciente(self, nombrePaciente):
        i = 0
        while i < self.__cantidad and self.__camas[i].getNyapaciente().lower() != nombrePaciente.lower():
            i += 1
        if i == self.__cantidad:
            i = -1
        return i

    def DarAlta(self, unManejadorMedicamentos):
        print("Ingrese paciente que desea dar de alta: ")
        nyapaciente = input()

        i = self.BuscarPaciente(nyapaciente)
        if( i != -1)and (self.__camas[i].getEstado()):
            print("PACIENTE ENCONTRADO".center(20,"-"))
            fecha = date.today()
            fecha = ("{}/{}/{}".format(fecha.day,fecha.month,fecha.year))
            self.__camas[i].setFechadealta(fecha)
            print("".center(20,"-"))
            print("Paciente:{}     Cama:{}     Habitacion:{}\nDiagnostico:{}       Fecha de internacion:{}\nFecha de Alta:{}".format(self.__camas[i].getNyapaciente(),self.__camas[i].getId(),self.__camas[i].getHabitacion(),self.__camas[i].getDiagnostico(),self.__camas[i].getFechainter(),self.__camas[i].getFechadealta()))
            print("".center(20,"-"))
            print("Medicamento/monodroga                Presentacion                    Cantidad              Precio")
            unManejadorMedicamentos.listarMedicamentosPorIdCama(self.__camas[i].getId())
        else:
            print("Paciente no existente")



    def ListaPacientesInternados(self):
        diagnostico = input("Ingrese el diagnostico: ")
        print("{0:<25}{1:<5}{2:<15}{3:<20}{4:<12}".format("Nombre", "Cama", "Habitacion", "Diagnostico", "Fecha de internacion"))
        for unaCama in self.__camas:
            if isinstance(unaCama, Cama):
                if unaCama.getEstado() and unaCama.getDiagnostico().lower() == diagnostico.lower():
                    print("{0:<25}{1:<5}{2:<15}{3:<20}{4:<12}".format(unaCama.getNyapaciente(), unaCama.getId(), unaCama.getHabitacion(), unaCama.getDiagnostico(), unaCama.getFechainter()))