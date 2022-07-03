import datetime
from conexion import conexionPBI
import os


def Publico():
    Empresa = input("Empresa: ")
    FDP = input("FDP: ")
    anio = int(FDP[0:4])
    mes = int(FDP[5:7])
    dia = int(FDP[8:10])

    fecha = datetime.datetime(anio, mes, dia, 7)

    FechaHora = []
    FechaHoraServidor = []
    Ingreso = []
    #Egreso = []
    SumaIngreso = 0

    for i in range(24):
        print("")
        list.insert(FechaHora, i, fecha - datetime.timedelta(hours=-i))
        list.insert(FechaHoraServidor, i, FechaHora[i].strftime("%Y-%m-%dT%H:%M:%S"))


        print(FechaHora[i], ": ")
        list.insert(Ingreso, i,  input("Ingreso: "))
        SumaIngreso = SumaIngreso + int(Ingreso[i])

        #list.insert(Egreso, i, input("Egreso: "))
        #SumaEgreso = SumaEgreso + int(Egreso[i])

        print("")

    print("Ingreso: ", SumaIngreso )
    #print("Egreso: ", SumaEgreso)

    Confirma= input("Confirma? \n SI=s, NO=n")

    if Confirma == "s":

        for i in range(24):
            try:
                with conexionPBI.cursor() as cursor:
                    consulta = "INSERT INTO [dbo].[publico] ([id_empresa], [fecha hora], [ingreso])" \
                               "VALUES (? , ? , ?)"
                    print(consulta)

                    cursor.execute(consulta, (Empresa, FechaHoraServidor[i], Ingreso[i]))

            except Exception as e:
                print("*****************************************************************************************")
                print("HA OCURRIDO UN ERROR:\n")
                print("Ocurrió un error al insertar: ", e)
                input()
            finally:
                0

    else:
        input("Cancelado. Cualquier tecla para continuar.")

def menuPublico():
    os.system("cls")
    print("\n")
    print("*****************************************************************************************")
    print("")
    print("=================")
    print("MODULO PUBLICO:")
    print("=================")
    print("")
    print("Seleccione una opcion:")
    print("\t0 - SALIR")
    print("\t1 - INGRESAR REGISTRO")



def moduloPublico():
    while True:
        # Mostramos el menu
        menuPublico()

        # solicituamos una opción al usuario
        opcionMenu = input("inserta un numero valor >> ")

        if opcionMenu == "0":
            os.system("cls")
            break

        elif opcionMenu == "1":

            os.system("cls")
            Publico()

        else:
            print("")
            input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")

