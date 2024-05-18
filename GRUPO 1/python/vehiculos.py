import threading
import time

#Funcion que simulara la llegada de los vehiculos al estacionamiento
def llegada_vehiculo(vehiculo_id):
    hora_llegada = time.strftime("%H:%M:%S", time.localtime())
    print(f"Vehiculo {vehiculo_id} llego al estacionamiento a las {hora_llegada}!")
    tiempo_espera = 5
    time.sleep(tiempo_espera)
    hora_registro = time.strftime("%H:%M:%S", time.localtime())
    print(f"Vehiculo {vehiculo_id} registrado a las {hora_registro}!")

#Simulacion de llegada
def simulacion_llegada(cantidad_vehiculos):
    for vehiculo_id in range(1, cantidad_vehiculos + 1):
        threading.Thread(target=llegada_vehiculo, args=(vehiculo_id,)).start()
        time.sleep(2)

#Simula la llegada de X cantidad de vehiculos
simulacion_llegada(5)
