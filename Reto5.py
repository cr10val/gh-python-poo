#Reto 5 - Herencia Python

class Entregable():
    def entregar():
        pass

    def devolver():
        pass

    def isEntregado():
        pass

    def comparteTo(self, objeto):
        pass

class Serie(Entregable):
    
    #Propiedades
    __Titulo = ""
    __Num_temp = 3
    __Entregado = False
    __Genero = ""
    __Creador = ""

    #Constructor
    def __init__(self,titulo,num_temp,entregado,genero,creador):
        self.__Titulo = titulo
        self.__Num_temp = num_temp
        self.__Entregado = entregado
        self.__Genero = genero
        self.__Creador = creador
        

    #get/set
    @property
    def titulo(self):
        return self.__Titulo 

    @titulo.setter
    def titulo(self, titulo):
        self.__Titulo = titulo

    @property
    def num_temp(self):
        return self.__Num_temp

    @num_temp.setter
    def num_temp(self, num_temp):
        self.__Num_temp = num_temp
    
    @property
    def genero(self):
        return self.__Genero

    @genero.setter
    def genero(self, genero):
        self.__Genero = genero

    @property
    def creador(self):
        return self.__Creador

    @creador.setter
    def creador(self, creador):
        self.__Creador = creador

    #Metodos
    #sobreescribimos el metodo str
    def __str__(self):
        sr ="Titulo: " +  self.__Titulo + "\nNum. Temp.: "+ str(self.__Num_temp)
        sr = sr + "\nEntregado: " + str(self.__Entregado) + "\nGenero: " + self.__Genero
        sr += "\nCreador: " + self.__Creador
        return sr

    #Entregar
    def entregar(self):
        self.__Entregado = True

    #Devolver
    def devolver(self):
        self.__Entregado = False

    #Esta entregado?
    def isEntregado(self):
        return self.__Entregado
        
    #Comparado a 
    #Devuelve 1 si es mayor, 2 si es menor y 0 si son iguales
    
    def compareTo(self, objeto):
        if(self.__Num_temp>objeto.num_temp):
            return 1
        elif(self.__Num_temp<objeto.num_temp):
            return 2
        else:
            return 0


class Videojuego(Entregable):
    #Propiedades
    __Titulo = ""
    __Horas_Est = 10
    __Entregado = False
    __Genero = ""
    __Compania = ""

    #Constructor
    def __init__(self,titulo,horas_est,entregado,genero,compania):
        self.__Titulo = titulo
        self.__Horas_Est = horas_est
        self.__Entregado = entregado
        self.__Genero = genero
        self.__Compania = compania

    #get/set
    @property
    def titulo(self):
        return self.__Titulo 

    @titulo.setter
    def titulo(self, titulo):
        self.__Titulo = titulo

    @property
    def horas_est(self):
        return self.__Horas_Est

    @horas_est.setter
    def horas_est(self, horas_est):
        self.__Horas_Est = horas_est
    
    @property
    def genero(self):
        return self.__Genero

    @genero.setter
    def genero(self, genero):
        self.__Genero = genero

    @property
    def compania(self):
        return self.__Compania

    @compania.setter
    def compania(self, compania):
        self.__Compania = compania

    #Metodos
    def __str__(self):
        sr ="Titulo: " +  self.__Titulo + "\nHoras Est.: "+ str(self.__Horas_Est)
        sr += "\nEntregado: " + str(self.__Entregado) + "\nGenero: " + self.__Genero
        sr += "\nCompañía: " + self.__Compania
        return sr

    #Entregar
    def entregar(self):
        self.__Entregado = True

    #Devolver
    def devolver(self):
        self.__Entregado = False

    #Esta entregado?
    def isEntregado(self):
        return self.__Entregado
        
    #Comparado a 
    #Devuelve 1 si es mayor, 2 si es menor y 0 si son iguales
    
    def compareTo(self, objeto):
        if(self.__Horas_Est >objeto.Horas_Est):
            return 1
        elif(self.__Horas_Est<objeto.Horas_Est):
            return 2
        else:
            return 0

# 1 - Creamos dos arrays
Series = []
Videoj = []


#2 - Rellenamos las series
Series.append(Serie("V",3,False,"Ciencia Ficcion","John Gray"))
Series.append(Serie("The 100",5,False,"Ciencia Ficcion","Martin Man"))
Series.append(Serie("The Simpsons",50,False,"Animacion","John Groenin"))
Series.append(Serie("El cuento de la criada",4,False,"Drama","John Doe"))
Series.append(Serie("Juego de Tronos",8,False,"Ciencia Ficcion","Mark Due"))
#2 - Rellenamos los videojuegos
Videoj.append(Videojuego("Monkey Island",50,False,"Aventura Grafica","Lucas Art"))
Videoj.append(Videojuego("Minecraft",100,False,"Construccion","Mojang"))
Videoj.append(Videojuego("Tetris",60,False,"2D","EA"))
Videoj.append(Videojuego("Super Mario Bros",10,False,"Plataforma","Nintendo"))
Videoj.append(Videojuego("Grand Theft Auto",80,False,"Accion-Aventura","Rockstar"))
#3 - Entregamos algunas series y videojuegos
Series[3].entregar()
Series[4].entregar()
Videoj[1].entregar()
Videoj[2].entregar()
Videoj[3].entregar()

#4 - Contamos cuantas series y video juegos hay entregados y los devolvemos
#0 series entregadas
entr = 0
#Recorremos la lista de series
for ser in Series:
    #Si esta entregada la devolvemos y sumamos 1
    if ser.isEntregado():
        ser.devolver()
        entr += 1

print(f"Había {entr} series entregadas")

#0 videojuegos entregados
entr = 0
#Recorremos la lista de videojuegos
for vj in Videoj:
    #Si esta entregado lo devolvemos y sumamos 1
    if vj.isEntregado():
        vj.devolver()
        entr += 1

print(f"Había {entr} videojuegos entregados")

"""
5 - Por último, indica el Videojuego tiene más horas estimadas y la serie
con mas temporadas. Muéstralos en pantalla con toda su
información (usa el método __ str
"""
#Ponemos que el que tiene mas horas es el primero
mashoras = Videoj[0]
#Recorremos la lista hasta el penultimo
for i in range(len(Videoj)-1):    
    #Si el actual tiene menos horas que el siguiente, decimos que el que tiene mas horas es el siguiente
    if mashoras.horas_est < Videoj[i+1].horas_est:
        mashoras = Videoj[i+1]
    
print("El videojuego con mas horas Estimadas es: \n", mashoras)

#Ponemos la primera serie como la que tiene mas temporadas
mastemp = Series[0]
#Recorremos la lista hasta el penultimo
for i in range(len(Series)-1):
    #Si el siguiente, tiene mas que el actual, cambiamos la variable y seguimos
    if mastemp.num_temp < Series[i+1].num_temp:
        mastemp = Series[i+1]

print("La serie con mas temporadas es: \n", mastemp)

