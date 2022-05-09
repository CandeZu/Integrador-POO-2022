class Medicamento:
    __idcama = 0
    __idMedicamento = 0
    __nombre = ""
    __monodroga = ""
    __presentacion = ""
    __cantAplicada = 0
    __precioTotal = 0

    def __init__(self, idcama, idMedicamento, nombre, monodroga, presentacion, cantAplicada, precioTotal):
        self.__idcama = idcama
        self.__idMedicamento = idMedicamento
        self.__nombre = nombre
        self.__monodroga = monodroga
        self.__presentacion = presentacion
        self.__cantAplicada = cantAplicada
        self.__precioTotal = precioTotal
    
    def getIdcama(self):
        return self.__idcama
    
    def getIdMedicamento(self):
        return self.__idMedicamento
    
    def getNombre(self):
        return self.__nombre
    
    def getMonodroga(self):
        return self.__monodroga
    
    def getPresentacion(self):
        return self.__presentacion
    
    def getCantAplicada(self):
        return self.__cantAplicada
    
    def getPrecioTotal(self):
        return self.__precioTotal
    
    