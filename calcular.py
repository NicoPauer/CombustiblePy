#!/usr/bin/python3

# Script de terminal para calcular el consumo y gasto en nafta de un auto

# Importo modulo con las caracteristicas de medidor de consumos de viaje
import medidor
# Importo modulo para poder obtener parametros del comando si los hay
import sys
# Import modulo para ejecutar comandos del systema operativo
import os

# Inicializo los objetos
viaje = medidor.Consumo()

vehiculo = medidor.Auto()
# Programa principal
if (__name__ == '__main__'):
    # Ejecuto un algoritmo u otro dependiendo si hay o no parametros en el comando de terminal
    if (sys.argv.__len__() > 1):
        # Caso mas raro: hay uno o mas parametros, recorro cada uno y hago accion correspondiente
        for parametro in sys.argv:
            if ((parametro == '-h') or (parametro == '-a') or (parametro == '--ayuda') or (parametro == '--help')):
                print('\nCALCULA COSTO DE UN VIAJE SEGUN PRECIO Y DISTANCIAS\n')
                print('\n[Parametros]\n\n\t--precio <numero> <divisa>, -p <numero> <divisa>: ingresa precio numero mayor a cero del combustible por litro\n\n\t--distancia <numero> <unidad>, -d <numero> <unidad>: ingresa distancia numero mayor a cero\n\n\t--rend <numero> <unidad>: ingresa la autonomia, cuanta distancia hace por unidad de combustible\n\n\t-t <numero> <divisa>: ingresa cuanto se agrega en tarifas')
            elif ((parametro == '--precio') or (parametro == '-p')):
                # Ingreso valor a atributo
                viaje.precio.append(float(sys.argv[sys.argv.index(parametro) + 1]))
                # Ingreso unidad en la que se mide
                viaje.precio.append(sys.argv[sys.argv.index(parametro) + 2])
            elif ((parametro == '--distancia') or (parametro == '-d')):
                # Ingreso valor a atributo
                viaje.distancia.append(float(sys.argv[sys.argv.index(parametro) + 1]))
                # Ingreso unidad en la que se mide
                viaje.distancia.append(sys.argv[sys.argv.index(parametro) + 2])
            elif (parametro == '-t'):
                # Ingreso valor a atributo
                viaje.tarifas.append(float(sys.argv[sys.argv.index(parametro) + 1]))
                # Ingreso unidad en la que se mide
                viaje.tarifas.append(sys.argv[sys.argv.index(parametro) + 2])
            elif (parametro == '--rend'):
                # Ingreso valor a atributo
                viaje.rendimiento.append(float(sys.argv[sys.argv.index(parametro) + 1]))
                # Ingreso unidad en la que se mide
                viaje.rendimiento.append(sys.argv[sys.argv.index(parametro) + 2])

        # Muestro el resultado
        divisas = {'ARS':'Pesos Argentinos', 'USD' : 'Dólares Estadounidenses', 'MXN' : 'Pesos Mexicanos', 'EUR':'Euros', 'COB' : 'Pesos Colombianos', 'BTC' : 'Bitcoins', 'SAT' : 'Satoshis'}
        simbolo = viaje.precio[1]
        nombre = divisas[simbolo.upper()]
        print(f'<p style = "border-radius: 0.5em; padding: 2em; width: 48em; background: rgb(70, 70, 70); color: rgb(245, 245, 245);">El auto recorrera <span style = "color: rgb(250, 250, 45);">{viaje.distancia[0]} {viaje.distancia[1]}</span> con autonomía de <span style = "color: rgb(250, 250, 45);">{viaje.rendimiento[0]} {viaje.rendimiento[1]}</span> a <span style = "color: rgb(250, 250, 45);">{viaje.precio[0]} {viaje.precio[1].replace(simbolo, nombre)}</span> el precio del litro de combustible, por lo tanto, tu viaje costará <span style = "color: rgb(250, 250, 45);">{viaje.costo()[0]} {viaje.costo()[1].replace(simbolo, nombre)}</span>.</p>')

    else:
        print('\nCALCULA COSTO DE UN VIAJE SEGUN PRECIO Y DISTANCIAS\n')
        print('\n[Parametros]\n\n\t--precio <numero> <divisa>, -p <numero> <divisa>: ingresa precio numero mayor a cero del combustible por litro\n\n\t--distancia <numero> <unidad>, -d <numero> <unidad>: ingresa distancia numero mayor a cero\n\n\t--rend <numero> <unidad>: ingresa la autonomia, cuanta distancia hace por unidad de combustible\n\n\t-t <numero> <divisa>: ingresa cuanto se agrega en tarifas')
