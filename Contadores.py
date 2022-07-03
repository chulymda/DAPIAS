import os
from conexion import conexionContadores
from tabulate import tabulate


def menuContadores():
    os.system("cls")
    print("\n")
    print("*****************************************************************************************")
    print("")
    print("=================")
    print("MODULO CONTADORES:")
    print("=================")
    print("")
    print("Seleccione una opcion:")
    print("\t0 - SALIR")
    print("\t1 - EDITAR REGISTRO")
    print("\t2 - ELIMINAR REGISTRO")


def existeElRegistro(fdp,maquina,FechaHoraRegistro):

    try:
        with conexionContadores.cursor() as cursor:
            consulta = "select count(maquina_id) FROM [CONTADORES].[dbo].[contadores_maquinas] " \
                       "where fdp = ? and maquina_id = ? and fecha = ?"
            print()
            print(consulta)
            print()

            cursor.execute(consulta, (fdp, maquina, FechaHoraRegistro))
            rows = cursor.fetchone()

            cantRegistristros = rows[0]

    except Exception as e:
        print("Ocurrió un error: ", e)
    finally:
        return cantRegistristros


def eliminarRegistro():

    fdp = input("FDP: ")
    maquina= input("Maquina: ")
    FechaHoraRegistro = input("Fecha hora: ")

    imprimeRegistro(fdp, maquina, FechaHoraRegistro)

    print("")
    print("Desea eliminar el registro?")
    elimina = input("SI=s, NO=n: ")

    if  elimina =="s":
        try:
            with conexionContadores.cursor() as cursor:
                consulta = "delete FROM [CONTADORES].[dbo].[contadores_maquinas] where fdp = ? and maquina_id = ? and fecha = ?"
                cursor.execute(consulta, (fdp, maquina, FechaHoraRegistro))


        except Exception as e:
            print("Ocurrió un error: ", e)
        finally:
            0


def imprimeRegistro(fdp,maquina, FechaHoraRegistro):
    try:
        with conexionContadores.cursor() as cursor:
            consulta = "select [sala_id], [fdp], [fecha], [cerrado], [coin_in], [coin_out], [coin_drop], [jackpot], [played], [won], [cancelled], [aft], [current_cred], [ajuste], [maquina_id] FROM [CONTADORES].[dbo].[contadores_maquinas] " \
                       "where fdp = ? and maquina_id = ? and fecha = ?"
            print(consulta)
            cursor.execute(consulta, (fdp, maquina, FechaHoraRegistro))
            rows = [cursor.fetchall()]
            headers = ["sala_id", "fdp", "fecha", "cerrado", "coin_in", "coin_out", "coin_drop", "jackpot", "played",
                       "won", "cancelled", "aft", "current_cred", "ajuste", "maquina_id"]
            for rows in rows:
                print(tabulate(rows, headers=headers, tablefmt="fancy_grid", stralign="left"))
    except Exception as e:
        print("Ocurrió un error: ", e)
    finally:
        0


def ingresaRegistro(fdp, maquina,FechaHoraRegistro):
    print("")
    print("")
    print("FDP: ", fdp)
    print("Maquina: ", maquina)
    print("Fecha Hora: ", FechaHoraRegistro)
    print("")
    maq = str(maquina)
    sala = maq[0:2]
    coin_in = input("Coin IN: ")
    coin_out = input("Coin OUT: ")
    coin_drop = input("Coin DROP: ")
    jackpot = input("Jackpot: ")
    played = input("Juegos jugados: ")
    won = input("Juegos ganaods: ")
    cancelled = input("Cancelados: ")
    aft = input("AFT: ")
    current_cred = input("Current credit: ")
    ajuste = 5
    try:
        with conexionContadores.cursor() as cursor:
            consulta = "insert into [CONTADORES].[dbo].[contadores_maquinas]"\
                       "(sala_id, fdp, fecha, coin_in, coin_out, coin_drop, jackpot, played, won, cancelled, aft," \
                       "current_cred, ajuste, maquina_id)"\
                       "values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
            cursor.execute(consulta, (sala, fdp, FechaHoraRegistro, coin_in, coin_out, coin_drop, jackpot, played, won, cancelled, aft, current_cred, ajuste, maquina))


    except Exception as e:
        print("Ocurrió un error: ", e)
    finally:
        0


def contadores():
    fdp = str(input("Fecha de produccion: "))
    maquina = int(input("Maquina: "))
    FechaHoraRegistro = str(input("Fecha hora del registro: "))

    if existeElRegistro(fdp, maquina, FechaHoraRegistro) >0:
        print("")
        print("Existen registros")
        print("")

        print(fdp)
        print(maquina)
        print(FechaHoraRegistro)

        try:
            with conexionContadores.cursor() as cursor:
                consulta = "select [sala_id], [fdp], [fecha], [cerrado], [coin_in], [coin_out], [coin_drop], [jackpot], [played], [won], [cancelled], [aft], [current_cred], [ajuste], [maquina_id] FROM [CONTADORES].[dbo].[contadores_maquinas] " \
                           "where fdp = ? and maquina_id = ? and fecha = ?"
                print(consulta)
                cursor.execute(consulta, (fdp, maquina, FechaHoraRegistro))
                rows = [cursor.fetchall()]
                headers = ["sala_id", "fdp", "fecha", "cerrado", "coin_in", "coin_out", "coin_drop", "jackpot", "played", "won", "cancelled", "aft", "current_cred", "ajuste", "maquina_id"]
                for rows in rows:
                    print(tabulate(rows, headers=headers, tablefmt="fancy_grid", stralign="left"))
        except Exception as e:
            print("Ocurrió un error: ", e)
        finally:
            0

        edita = input("Desea editar el registro?:\n SI=s NO=n: ")

        if edita == "s":
            edita_IN = input("Coin IN: ")
            edita_OUT = input("Coin OUT: ")
            edita_DROP = input("Coin DROP: ")
            edita_JACK = input("JACKPOT: ")
            edita_PLAYED = input("JUGADOS: ")
            edita_WON = input("GANADOS: ")
            edita_CANCELL = input("CANCELADOS: ")
            edita_AFT = input("AFT: ")
            edita_CURRENT = input("CURRENT CREDIT: ")
            print("")
            ajuste = input("A cual ajuste?:")

            try:
                with conexionContadores.cursor() as cursor:
                    consulta = "update [CONTADORES].[dbo].[contadores_maquinas] set coin_in = ?, coin_out = ?, coin_drop =?, jackpot= ?, played =?, won =?, cancelled = ?, aft=?, current_cred=? " \
                    "where fdp = ? and maquina_id = ? and fecha = ? and ajuste = ?"

                    cursor.execute(consulta, (edita_IN, edita_OUT, edita_DROP, edita_JACK, edita_PLAYED, edita_WON, edita_CANCELL, edita_AFT, edita_CURRENT, fdp, maquina, FechaHoraRegistro, ajuste))
            except Exception as e:
                print("Ocurrió un error: ", e)
            finally:
               0
    else:
        print("NO HAY REGISTRO")
        print("Desea inertar un registro?")
        inserta = input("SI=s, NO=n: ")
        if  inserta =="s":
            ingresaRegistro(fdp, maquina, FechaHoraRegistro)


def moduloContadores():
    while True:
            # Mostramos el menu
            menuContadores()

            # solicituamos una opción al usuario
            opcionMenu = input("inserta un numero valor >> ")

            if opcionMenu == "0":
                os.system("cls")
                break
            elif opcionMenu == "1":

                os.system("cls")
                contadores()

            elif opcionMenu == "2":
                os.system("cls")
                eliminarRegistro()

            else:
                print("")
                input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")
