from conexion import conexionPBI


def gastronomiaIngresar(id_sala, fdp, puntoGastronomico, monto):

    try:
        with conexionPBI.cursor() as cursor:
            consulta = "INSERT INTO gastronomia(id_sala, FDP, Gastronomia, Total) "\
                       "VALUES (?,?,?,?); "
            # Podemos llamar muchas veces a .execute con datos distintos
            cursor.execute(consulta, (id_sala, fdp, puntoGastronomico, monto))

    except Exception as e:
        print("*****************************************************************************************")
        print("HA OCURRIDO UN ERROR:\n")
        print("Ocurrió un error al insertar: ", e)
        input()
    finally:
        0


def gastronomiaEliminar(id_sala, fdp):

    try:
        with conexionPBI.cursor() as cursor:
            consulta = "delete FROM [PBI].[dbo].[gastronomia] where id_sala = ? and FDP = ?"
            # Podemos llamar muchas veces a .execute con datos distintos
            cursor.execute(consulta, (id_sala, fdp))

    except Exception as e:
        print("*****************************************************************************************")
        print("HA OCURRIDO UN ERROR:\n")
        print("Ocurrió un error al insertar: ", e)
        input()
    finally:
        0


