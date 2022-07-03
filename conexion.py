import pyodbc


direccion_servidor = '192.168.100.200'
BDTesoreria = 'tesoreria'
BDContadores = 'contadores'
BDPBI = 'PBI'
nombre_usuario = 'chuly'
password = '978645312'


try:
    conexionTesoreria = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
                              direccion_servidor + ';DATABASE=' + BDTesoreria + ';UID=' + nombre_usuario + ';PWD=' + password)
    print("Conexión TESORERIA: OK")

except Exception as e:
    print("Ocurrió un error al conectar a SQL Server: ", e)


try:
    conexionContadores = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
                              direccion_servidor + ';DATABASE=' + BDContadores + ';UID=' + nombre_usuario + ';PWD=' + password)
    print("conexión CONTADORES: OK")

except Exception as e:
    print("Ocurrió un error al conectar a SQL Server: ", e)


try:
    conexionPBI = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
                              direccion_servidor + ';DATABASE=' + BDPBI + ';UID=' + nombre_usuario + ';PWD=' + password)
    print("conexión PBI: OK")

except Exception as e:
    print("Ocurrió un error al conectar a SQL Server: ", e)

