#script que genere lanzamiento de dados al azar (1-6)
#y escribir mensaje GANADOR cuando saque par de 6

#importar biblioteca para numeros aleatorios enteros
from random import randint



def lanzar (reg):
    d1 = randint(1,6)
    d2 = randint(1,6)
    si = False 
    
    if 0<reg<7:
            if (d1+d2)==reg*2:
                si=True

    elif d1==d2:
         si=True

    return d1, d2, si, reg
        

print(" Digite un numero entre 1 y 6 para asignar el numero del par ganador")      
reg=input(" Digite 0 para asignar, cualquier numero par gana \n")

d=lanzar(int(reg))

regla=d[3]

if 0<regla<7:
    print("Regla: par de "+ str(regla)+" GANA")
else: 
    print("Regla: cualquier numero par gana")

print("El dado uno vale ",d[0]," y el dado dos vale: ", d[1])

if d[2]: print("GANASTE")
else: print("SIGUE INTENTANDO")