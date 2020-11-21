from Particulas import Particula
import json
#
class AlmacenDeParticulas:
    def __init__(self):
        self.__particulas = []
    
    def agregar_final(self, Particulas:Particula):
        self.__particulas.append(Particulas)

    def agregar_inicio(self, Particulas:Particula):
        self.__particulas.insert(0, Particulas)

    def mostrar(self):
        for Particulas in self.__particulas:
            print(Particulas)

    def __str__(self):
        return "".join(
            str(Particulas) + '\n'for Particulas in self.__particulas
            
        )

    def __len__(self):
        return len(self.__particulas)
    
    def __iter__(self):
        self.cont = 0
        return self

    def __next__(self):
        if self.cont < len(self.__particulas):
            Particulas = self.__particulas[self.cont]
            self.cont += 1
            return Particulas
        else:
            raise StopIteration

    def guardar(self, ubication):
        try:
            with open(ubication, 'w') as archivo:
                lista = [Particulas.to_dict() for Particulas in self.__particulas]
                print(lista)
                json.dump(lista, archivo, indent=5)
            return 1
        except:
            return 
            
    def abrir(self, ubication):
        try:
            with open(ubication, 'r') as archivo:
                lista = json.load(archivo)
                self.__particulas = [Particula(**Particulas) for Particulas in lista]
            return 1
        except:
            return 0

    def ordenar(self):
        self.__particulas.sort()

    def ordenarD(self):
        part = Particula
        self.__particulas.sort(key=lambda part: part.Distancia, reverse=True)

    def ordenarV(self):
        part = Particula
        self.__particulas.sort(key=lambda part: part.Velocidad)