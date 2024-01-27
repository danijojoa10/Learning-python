#fubcion para detectar la clave de un cajero de banco
#intentos permitidos 3

def cajero(): 
    clave_registrada = '2024'

    cont_attempts=1
    status= True
    intentosf=0

    while status: 

        clave_ingresada = input("digita tu clave")


        if (clave_ingresada==clave_registrada):
           print("Continue con su transaccion")
           cont_attempts += 1 
           status = False
        else : 
            print("contraseña incorrecta, intenta nuevamente")
            print("intentos restantes", 3-(cont_attempts))   
            cont_attempts += 1
            

            if(cont_attempts>3):
             print("tu cuenta a sido bloqueada")  
             break  


cajero()