import help
from help import imprimeEmpresas
from conexion import conexionPBI






def FDPCerrada():


    help.inicioLinea()

    help.imprimeEmpresas()

    id_empresa = input("id Empresa: ")
    FDP = input("ultima FDP cerrada: ")



    print("\n")
    print("Confirma?\n SI=s | NO=n:")


    confirma = input()

    if confirma == "s":
        try:
            with conexionPBI.cursor() as cursor:
                consulta = """update[PBI].[dbo].[estadoFDP]
                            set
                            ultimaFDPCerrada = ?
                            where
                            id_empresa = ?"""


                cursor.execute(consulta, (FDP, id_empresa))

        except Exception as e:
            print("*****************************************************************************************")
            print("HA OCURRIDO UN ERROR:\n")
            print("Ocurrió un error al insertar: ", e)
            input()
        finally:
            0
    else:
        print("cancelado")

