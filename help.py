from conexion import conexionPBI
from tabulate import tabulate
import os




def imprimeEmpresas():
    try:
        with conexionPBI.cursor() as cursor:
            consulta = """SELECT [id_empresa]
                        ,[nombreCorto]
                        ,[ultimaFDPCerrada]
                        FROM [PBI].[dbo].[view_empresas]"""
            #print(consulta)
            cursor.execute(consulta)
            rows = [cursor.fetchall()]
            headers = ["id_empresa", "Empresa", "Ultima FDP cerrada"]
            for rows in rows:
                print(tabulate(rows, headers=headers, tablefmt="fancy_grid", stralign="left"))
                print()
    except Exception as e:
        print("Ocurrió un error: ", e)
    finally:
        0

def inicioLinea():
    os.system("cls")
    print("===================================================================================")
