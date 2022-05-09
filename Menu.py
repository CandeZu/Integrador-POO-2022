from Camas import Cama
import os

from Medicamentos import Medicamento
from ManejadorMedicamentos import ManejadorMedicamento
from ManejadorCamas import ManejadorCama
from Camas import Cama
import os

class Menu:
    __listaCamas = ManejadorCama()
    __listaMedicamentos = ManejadorMedicamento()
    __op = 0

    def __init__(self, op= 0):
        self.__op = op

    def opciones(self):
            self.__listaCamas.GenerarLista()
            self.__listaMedicamentos.GenerarLista()
            os.system("cls")
            continuar = True


            while continuar:
                print("[1] Leer los datos de cada cama.")
                print("[2] Leer los datos de los medicamentos utilizados en cada cama.")
                print("[3] Dado un nombre y apellido de un paciente al que se le da el alta, listar datos del paciente y medicamentos a devolver.")
                print("[4] Listar los datos de pacientes internados (cama ocupada), que tienen un diagnóstico leído desde teclado.")
                print("[0] Para salir del menu")
                self.__op = int(input("INGRESE OPCION\n"))
                os.system("cls")

                if(self.__op == 1):
                    self.__listaCamas.ListarCamas()

                elif(self.__op ==2):
                    self.__listaMedicamentos.ListarMedicamentos()
        
                elif(self.__op ==3):
                    self.__listaCamas.DarAlta(self.__listaMedicamentos)

                elif (self.__op ==4):
                    self.__listaCamas.ListaPacientesInternados()


                elif(self.__op == 0):
                    continuar = not continuar
                    print("PROGRAMA FINALIZADO")
                else: 
                    print("Opcion incorrecta, ingrese nuevamente")