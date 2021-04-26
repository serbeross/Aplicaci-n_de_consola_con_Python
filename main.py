from usuarios import acciones

hazEl = acciones.Acciones()


hazEl.primetaAcciones()

accion = input("Que quiere hacer?: ")
    
if accion == "registro" or accion == "r":
    hazEl.registro()
            

elif accion == "login" or accion == "l":
    hazEl.login()
        