import os
import Tesoreria
import Contadores
import Publico
import cerrarFDP


def menuPrincipal():
    os.system("cls")
    print("")
    print("=====================")
    print("MENU PRINCIPAL")
    print("=====================\n \n")
    print("Selecciona una opción\n")
    print("\t0 - Salir")
    print("\t1 - Modulo tesoreria")
    print("\t2 - Contadores")
    print("\t3 - Publico")
    print("\t4 - FDP Cerradas\n")



while True:
    # Mostramos el menu
    menuPrincipal()

    # solicituamos una opción al usuario
    opcionMenu = input("inserta una opcion: >> ")

    if opcionMenu == "0":
        exit()

    elif opcionMenu == "1":
        os.system("cls")
        Tesoreria.moduloTesoreria()

    elif opcionMenu == "2":
        os.system("cls")
        Contadores.moduloContadores()

    elif opcionMenu == "3":
        os.system("cls")
        Publico.moduloPublico()

    elif opcionMenu == "4":
        os.system("cls")
        cerrarFDP.FDPCerrada()

    else:
        print("")
        input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")



