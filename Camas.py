class Cama:
    __id = 0
    __habitacion = 0
    __estado = None
    __nyapaciente = ""
    __diagnostico = ""
    __fechainter = None
    __fechadealta = None

    def __init__(self, id, habitacion, estado, nyapaciente, diagnostico, fechainter, fechadealta):
        self.__id = id
        self.__habitacion = habitacion
        self.__estado = estado
        self.__nyapaciente = nyapaciente
        self.__diagnostico = diagnostico
        self.__fechainter = fechainter
        self.__fechadealta = fechadealta
    
    def getId(self):
        return self.__id
    
    def getHabitacion(self):
        return self.__habitacion
    
    def getEstado(self):
        return self.__estado
    
    def getNyapaciente(self):
        return self.__nyapaciente
    
    def getDiagnostico(self):
        return self.__diagnostico
    
    def getFechainter(self):
        return self.__fechainter
    
    def getFechadealta(self):
        return self.__fechadealta
    
    def __str__(self):
        return "Id cama: {}\nHabitacion: {}\nEstado: {}\nNombre del paciente: {}\nDiagnostico: {}\nFecha de internación: {}\nFecha de alta: {}".format(self.__id, self.__habitacion, self.__estado, self.__nyapaciente, self.__diagnostico, self.__fechainter, self.__fechadealta)