def email(correo, confirmación):
    if confirmación != correo:
         try:
            correo == confirmación
         except:
            print("No coinciden")    
    elif confirmación.find("@gmail.com") == False:
         try:
            correo == confirmación
         except:
            print("No tiene formato @gmail.com")
    else:
        print("bienvendio")
        return correo
