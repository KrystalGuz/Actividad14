#
class Particula:
    def __init__(self, Id=0, OrigenX=0, OrigenY=0, DestinoX=0, DestinoY=0, Velocidad=0, Red=0, Green=0, Blue=0, Distancia=0):
        self.__Id = Id
        self.__OrigenX = OrigenX
        self.__OrigenY = OrigenY
        self.__DestinoX = DestinoX
        self.__DestinoY = DestinoY
        self.__Velocidad = Velocidad
        self.__Red = Red
        self.__Green = Green
        self.__Blue = Blue
        self.__Distancia = Distancia
    
    def __str__(self):
        return (
            'Id: ' + str(self.__Id) + '\n' +
            'Origen en X: ' + str(self.__OrigenX) + '\n' +
            'Origen en Y: ' + str(self.__OrigenY) + '\n' +
            'Destino en X: ' + str(self.__DestinoX) + '\n' +
            'Destino en Y: ' + str(self.__DestinoY) + '\n' +
            'Velocidad: ' + str(self.__Velocidad) + '\n' +
            'Red: ' + str(self.__Red) + '\n' +
            'Green: ' + str(self.__Green) + '\n' +
            'Blue: ' + str(self.__Blue) + '\n' +
            'Distancia: ' + str(self.__Distancia) + '\n'
        )
    
    def __lt__(self, other):
        return self.Id < other.Id

    @property
    def Id(self):
        return self.__Id

    @property
    def OrigenX(self):
        return self.__OrigenX

    @property
    def OrigenY(self):
        return self.__OrigenY

    @property
    def DestinoX(self):
        return self.__DestinoX

    @property
    def DestinoY(self):
        return self.__DestinoY

    @property
    def Velocidad(self):
        return self.__Velocidad

    @property
    def Red(self):
        return self.__Red

    @property
    def Green(self):
        return self.__Green

    @property
    def Blue(self):
        return self.__Blue

    @property
    def Distancia(self):
        return self.__Distancia

    def to_dict(self):
        return {
            "Id": self.__Id,
            "OrigenX": self.__OrigenX,
            "OrigenY": self.__OrigenY,
            "DestinoX": self.__DestinoX,
            "DestinoY": self.__DestinoY,
            "Velocidad": self.__Velocidad,
            "Red": self.__Red,
            "Green": self.__Green,
            "Blue": self.__Blue,
            "Distancia": self.__Distancia
        }