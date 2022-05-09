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

    def DarAlta(self, Medicamento):
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
            Total = 0
            for i in range(len(Medicamento)):
                if(Medicamento[i].getIdcama() == self.__camas[i].getId()):
                    print("{0:^30}{1:^30}{2:^30}{3:^7}".format(Medicamento[i].getMonodroga(),Medicamento[i].getPresentacion(),Medicamento[i].getCantAplicada(),Medicamento[i].getPrecioTotal()))
                    Total += Medicamento[i].getPrecioTotal()
            print("Total Adeudado:{0:82}".format(Total))
        else:
            print("Paciente no existente")

    def ListaPacientesInternados(self):
        diagnostico = input("Ingrese diagnostico que desea solicitar\n")
        os.system("cls")
        print("Pacientes con diagnostico de {}".format(diagnostico).lower())
        for i in range(30):
            if(self.__camas[i] != None):
                if (self.__camas[i].getEstado() == True):
                    if(self.__camas[i].getDiagnostico().lower() == diagnostico):
                        print("".center(20,"-"))
                        print(self.__camas[i])
                        print("".center(20,"-"))
    