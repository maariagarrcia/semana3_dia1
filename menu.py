#FUNCIONES PARA EL MENU

import helpers
from colorama import Fore

def aceptar_opcion_menu():
    opcion = -1
    salir = False

    while (not salir):
        inputusuario= input(Fore.GREEN + "Dime que opcion deseas" + Fore.WHITE)
          
        if (inputusuario == "F" or inputusuario == "f"):
            # Finalizar
            opcion= -1
            salir= True
        elif (inputusuario == "P" or inputusuario== "p"):
            # Ver puntuaciones
            opcion=-2
            salir= True
        elif (helpers.input_usuarioOk(inputusuario, 1, 5)):
            #JUGAR CON NIVEL ENTRE 1,4
            opcion= int(inputusuario)
            salir= True
        else:
            # Opcion incorrecta
            print(Fore.RED + "*ATENCION: Seleccione una opcion valida" + Fore.WHITE)
    
    return opcion

def menu():
    print()
    print(Fore.GREEN + "MENU")
    print("----")
    print("1 - EJERCICIOS MATRICES")
    print("2 - EJERCICIOS DATAFRAME")

    print("F - Finalizar")
    print(Fore.WHITE)

    opcion= aceptar_opcion_menu()
    return opcion