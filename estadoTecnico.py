import datetime
import re

repuestos = ["Placa CPU", "Placa video", "Control rodillos", "Monitor", "Memoria", "Memoria juego"]

def listaRepuestos():

    print('=' * 30)
    j = 0
    for i in repuestos:
        j = j + 1
        print(j, i)
    print('=' * 30)



fdp = input("Fecha: ")
anio = int(fdp[0:4])
mes = int(fdp[5:7])
dia = int(fdp[8:10])
hora = int(input("Hora: "))

fecha = datetime.datetime(anio, mes, dia, hora)
fechaSQL = fecha.strftime("%Y-%m-%dT%H:%M:%S")

maquina = input("Maquina: ")
motivo = input("Motivo: ")
faltaRepuesto = input("Falta repuesto: ")
print()
asd = "a"
if faltaRepuesto in('S', 's', '1'):
    listaRepuestos()
    print()
    repuestosFaltates = input("Ingrese los repuestos faltantes: ").split('-')


    repuestosFaltatesSQL = '|'
    x = 0
for i in repuestosFaltates:
    print(repuestos[int(i)-1])
    print(i)

    repuestosFaltatesSQL = repuestosFaltatesSQL + repuestos[int(i)-1] + '|'
    x = x + 1

print(maquina, fechaSQL, 'Fuera de servicio', motivo, repuestosFaltatesSQL)