from ejercicio_numpy_pandas import *
import menu
import helpers



def inicio():
    
    finalizar= False
    helpers.clear() #Limpia la terminal

    while (not finalizar):
        opcion = menu.menu()
        if opcion==1:
            print(Fore.BLUE + "=====EJERCICIOS MATRICES=======" + Fore.WHITE)
            print()
            matrices()
        elif opcion==2:
            print(Fore.BLUE + "=====EJERCICIOS DATAFRAME=======" + Fore.WHITE)
            print()
            Dataframe()

    print(Fore.GREEN  + "Nos vemos otro dia :)")
    print(Fore.WHITE)

