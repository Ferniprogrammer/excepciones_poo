import re

correo_correcto = "fsanchor@myuax.com"
user = "Fernando"

def email(correo):
    if correo == "":
        raise ValueError("'' es una entrada incorrecta. Introduzca una dirección de correo")    
    if re.search(".*@.*\..*", correo) is None:
        raise ValueError("Una dirección de correo electrónico debe tener el formato xxx@xxx.xx")
    if correo != correo_correcto:
        raise SystemError("Cuenta bloqueada a causa de un ataque")

if __name__ == "__main__":
    parar = False
    while not parar:
        correo = input("Introduzca su correo: ")
        
        try:
            email(correo)
            print("Bienvenido {:s}!".format(user))
            parar = True
        except ValueError as error:
            print(error)
        except SystemError as error:
            print(error)
            parar = True

       

    