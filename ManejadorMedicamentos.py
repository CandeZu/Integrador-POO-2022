from Medicamentos import Medicamento
import csv

class ManejadorMedicamento:
    __listaMedicamentos = []

    def __init__(self):
        self.__listaMedicamentos = []
    
    def GenerarLista(self):
        archivo = open("medicamentos.csv")
        reader = csv.reader(archivo, delimiter=";")
        bandera=True
        for fila in reader:
            if bandera:
                bandera = not bandera
            else:
                idcama = int(fila[0])
                idMedicamento = int(fila[1])
                nombre = fila[2]
                monodroga = fila[3]
                presentacion = fila[4]
                cantAplicada = int(fila[5])
                precioTotal = int(fila[6])
                medicamento = Medicamento(idcama, idMedicamento, nombre, monodroga, presentacion, cantAplicada, precioTotal)
                self.__listaMedicamentos.append(medicamento)
        archivo.close()
    
    def ListarMedicamentos(self):
        for medicamento in self.__listaMedicamentos:
            print(medicamento)
            print("\n".center(20,"-"))
