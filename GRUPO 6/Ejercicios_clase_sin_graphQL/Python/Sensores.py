import random

# Definición de la clase Sensor
class Sensor:
    def __init__(self, id, ubicacion, temperatura):
        self.id = id
        self.ubicacion = ubicacion
        self.temperatura = temperatura

# Definición de la clase GraphSQL para almacenar los sensores
class GraphSQL:
    # Ahora el campo database es un diccionario público
    database = {}

    # Método para agregar un nuevo sensor a la base de datos
    @staticmethod
    def add_sensor(sensor):
        GraphSQL.database[sensor.id] = sensor

    # Método para eliminar un sensor de la base de datos
    @staticmethod
    def remove_sensor(id):
        if id in GraphSQL.database:
            del GraphSQL.database[id]

    # Método para actualizar la temperatura de un sensor existente
    @staticmethod
    def update_temperature(id, temperatura):
        if id in GraphSQL.database:
            GraphSQL.database[id].temperatura = temperatura

    # Método para obtener la temperatura de un sensor específico
    @staticmethod
    def get_temperature(id):
        if id in GraphSQL.database:
            return GraphSQL.database[id].temperatura
        return -1  # Valor de temperatura inválido si el sensor no existe

    # Método para simular la actualización de temperaturas de los sensores
    @staticmethod
    def simulate_temperature_updates():
        for sensor in GraphSQL.database.values():
            # Simulación de la actualización de la temperatura con un valor aleatorio
            nueva_temperatura = sensor.temperatura + random.random() * 0.5  # Aumento de temperatura aleatorio entre 0 y 0.5
            GraphSQL.update_temperature(sensor.id, nueva_temperatura)

# Clase principal para simular el sistema de tiempo real
class Program:
    @staticmethod
    def main():
        # Agregamos algunos sensores a la base de datos
        GraphSQL.add_sensor(Sensor("1", "Sala de estar", 25.5))
        GraphSQL.add_sensor(Sensor("2", "Cocina", 22.0))
        GraphSQL.add_sensor(Sensor("3", "Dormitorio", 20.8))

        salir = False

        # Menú interactivo
        while not salir:
            print("Seleccione una opción:")
            print("1. Visualizar sensores y temperaturas")
            print("2. Agregar sensor")
            print("3. Eliminar sensor")
            print("4. Consultar temperatura de un sensor")
            print("5. Salir")

            opcion = input()

            if opcion == "1":
                Program.visualizar_sensores_y_temperaturas()
            elif opcion == "2":
                Program.agregar_sensor()
            elif opcion == "3":
                Program.eliminar_sensor()
            elif opcion == "4":
                Program.consultar_temperatura()
            elif opcion == "5":
                salir = True
            else:
                print("Opción inválida. Por favor, seleccione una opción válida.")

    @staticmethod
    def visualizar_sensores_y_temperaturas():
        print("Sensores y temperaturas:")
        for sensor in GraphSQL.database.values():
            print(f"Sensor: {sensor.id}, Ubicación: {sensor.ubicacion}, Temperatura: {sensor.temperatura} °C")

    @staticmethod
    def agregar_sensor():
        id = input("Ingrese el ID del nuevo sensor: ")
        ubicacion = input("Ingrese la ubicación del nuevo sensor: ")

        # Verificar si el sensor ya existe
        if id in GraphSQL.database:
            print("Error: El sensor ya existe en la base de datos.")
        else:
            # Agregar el nuevo sensor con temperatura predeterminada de 0 °C
            GraphSQL.add_sensor(Sensor(id, ubicacion, 0))
            print("Sensor agregado correctamente.")

    @staticmethod
    def eliminar_sensor():
        id = input("Ingrese el ID del sensor que desea eliminar: ")

        # Verificar si el sensor existe
        if id in GraphSQL.database:
            # Eliminar el sensor
            GraphSQL.remove_sensor(id)
            print("Sensor eliminado correctamente.")
        else:
            print("Error: El sensor no existe en la base de datos.")

    @staticmethod
    def consultar_temperatura():
        id = input("Ingrese el ID del sensor del cual desea consultar la temperatura: ")

        # Verificar si el sensor existe
        if id in GraphSQL.database:
            # Obtener la temperatura del sensor
            temperatura = GraphSQL.get_temperature(id)

            # Aumentar ligeramente la temperatura del sensor
            temperatura += 0.1

            # Actualizar la temperatura en la base de datos
            GraphSQL.update_temperature(id, temperatura)

            print(f"La temperatura del sensor {id} ({GraphSQL.database[id].ubicacion}) es: {temperatura} °C")
        else:
            print("Error: El sensor no existe en la base de datos.")

# Ejecutar el programa principal
if __name__ == "__main__":
    Program.main()
