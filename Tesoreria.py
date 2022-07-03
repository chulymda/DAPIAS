from conexion import conexionTesoreria, conexionPBI
from tabulate import tabulate
from gastronomia import gastronomiaIngresar, gastronomiaEliminar
import os


def tesoreriaIn():
    print("INGRESO DE REGISTROS TESORERIA:\n")
    fecha = input("Fecha: ")
    id_empresa = input("Bingo: ")
    maquinas = input("Tragamonedas: ")
    bar = input("Bar: ")
    bingoBruto = input("Bingo bruto: ")
    bingoNeto = input("Bigo neto: ")
    billetero = input("Billetero: ")

    print("\n\n")
    print("Confirma?\n SI=s | NO=n:")
    confirma = input()

    if confirma == "s":
        try:
            with conexionTesoreria.cursor() as cursor:
                consulta = "INSERT INTO tesoreria(id_bingo, fecha, maquinas, bingoBruto, bingoNeto, billetero) " \
                           "VALUES (?,?,?,?,?,?); "
                # Podemos llamar muchas veces a .execute con datos distintos
                cursor.execute(consulta, (id_empresa, fecha, maquinas, bingoBruto, bingoNeto, billetero))

                gastronomiaIngresar(id_empresa, fecha, 'General', bar)  # se ingresa el buffet en la sala general

        except Exception as e:
            print("*****************************************************************************************")
            print("HA OCURRIDO UN ERROR:\n")
            print("Ocurrió un error al insertar: ", e)
            input()
        finally:
            0



    else:
        print("cancelado")
        menuTesoreria()


def tesoreriaDel():
    print("Eliminar registro tesoreria:\n")
    fecha = input("Fecha: ")
    id_empresa = input("Bingo: ")

    print("\n\n")

    try:
        with conexionTesoreria.cursor() as cursor:
            consulta = "select id_bingo	,fecha	,maquinas	,bingoBruto	,bingoNeto	,pbi.dbo.gastronomia.Total as [" \
                       "buffet] ,convert(int,[billetero]) from tesoreria left join pbi.dbo.gastronomia on " \
                       "pbi.dbo.gastronomia.id_sala = id_bingo and pbi.dbo.gastronomia.FDP = fecha " \
                       "where fecha = ? and id_bingo = ? "

            # Podemos llamar muchas veces a .execute con datos distintos
            cursor.execute(consulta, (fecha, id_empresa))
            rows = [cursor.fetchall()]
            headers = ["id_Bingo", "Fecha", "Maquinas", "Bingo bruto", "Bingo neto", "Buffet", "Billetero",
                       "id_Tesoreria"]
            for rows in rows:
                print(tabulate(rows, headers=headers, tablefmt="fancy_grid", stralign="left"))



    except Exception as e:
        print("*****************************************************************************************")
        print("HA OCURRIDO UN ERROR:\n")
        print("Ocurrió un error al consultar: ", e)
        input()
    finally:
        0

    elimina = input("Desea eliminar el registro?:\n SI=s NO=n: ")
    if elimina == "s":
        try:
            with conexionTesoreria.cursor() as cursor:
                consulta = "delete from tesoreria where id_bingo =? and fecha = ? "
                # Podemos llamar muchas veces a .execute con datos distintos
                cursor.execute(consulta, (id_empresa, fecha))
                gastronomiaEliminar(id_empresa, fecha)

        except Exception as e:
            print("*****************************************************************************************")
            print("HA OCURRIDO UN ERROR:\n")
            print("Ocurrió un error al insertar: ", e)
            input()
        finally:
            0
    else:
        print("\nREGISTRO CANCELADO")
        print("Vuelva a ingresar los datos:")
        tesoreriaDel()


def tesoreriaImprimir():
    print("")
    FechaIni = input("Fecha desde: ")
    FechaFIN = input("Fecha hasta: ")

    try:
        with conexionTesoreria.cursor() as cursor:

            consulta = "SELECT [id_bingo], [fecha], [maquinas], [bingoBruto], [bingoNeto]," \
                       "pbi.dbo.gastronomia.Total as [buffet]," \
                       "[billetero], [id_tesoreria] FROM [TESORERIA].[dbo].[tesoreria]" \
                       "left join pbi.dbo.gastronomia on pbi.dbo.gastronomia.id_sala = id_bingo and " \
                       "pbi.dbo.gastronomia.FDP = fecha " \
                       "where [TESORERIA].[dbo].[tesoreria].fecha >= ? and [TESORERIA].[dbo].[tesoreria].fecha <= ?"

            print(consulta)
            cursor.execute(consulta, (FechaIni, FechaFIN))
            rows = [cursor.fetchall()]
            headers = ["id_bingo", "fecha", "maquinas", "bingoBruto", "bingoNeto", "buffet", "billetero",
                       "id_tesoreria"]
            for rows in rows:
                print(tabulate(rows, headers=headers, tablefmt="fancy_grid", stralign="left"))
            input("Toque para continuar")
    except Exception as e:
        print("Ocurrió un error: ", e)
    finally:
        0


def menuTesoreria():
    os.system("cls")
    print("\n")
    print("*****************************************************************************************")
    print("")
    print("=================")
    print("MODULO TESORERIA:")
    print("=================")
    print("")
    print("Seleccione una opcion:")
    print("\t0 - SALIR")
    print("\t1 - INGRESAR REGISTRO")
    print("\t2 - ELIMINAR REGISTRO")
    print("\t3 - VER REGISTRO")


def moduloTesoreria():
    while True:
        # Mostramos el menu
        menuTesoreria()

        # solicituamos una opción al usuario
        opcionMenu = input("inserta un numero valor >> ")

        if opcionMenu == "0":
            os.system("cls")
            break

        elif opcionMenu == "1":

            os.system("cls")
            tesoreriaIn()

        elif opcionMenu == "2":
            os.system("cls")
            tesoreriaDel()

        elif opcionMenu == "3":
            os.system("cls")
            tesoreriaImprimir()


        else:
            print("")
            input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")
