using System;
using System.Collections.Generic;

// Definición de la clase Sensor
public class Sensor
{
    public string Id { get; set; }
    public string Ubicacion { get; set; }
    public double Temperatura { get; set; }
}

// Definición de la clase GraphSQL para almacenar los sensores
public static class GraphSQL
{
    // Ahora el campo database es público
    public static Dictionary<string, Sensor> database = new Dictionary<string, Sensor>();

    // Método para agregar un nuevo sensor a la base de datos
    public static void AddSensor(Sensor sensor)
    {
        database[sensor.Id] = sensor;
    }

    // Método para eliminar un sensor de la base de datos
    public static void RemoveSensor(string id)
    {
        if (database.ContainsKey(id))
        {
            database.Remove(id);
        }
    }

    // Método para actualizar la temperatura de un sensor existente
    public static void UpdateTemperature(string id, double temperature)
    {
        if (database.ContainsKey(id))
        {
            database[id].Temperatura = temperature;
        }
    }

    // Método para obtener la temperatura de un sensor específico
    public static double GetTemperature(string id)
    {
        if (database.ContainsKey(id))
        {
            return database[id].Temperatura;
        }
        return -1; // Valor de temperatura inválido si el sensor no existe
    }

    // Método para simular la actualización de temperaturas de los sensores
    public static void SimulateTemperatureUpdates()
    {
        Random random = new Random();
        foreach (var sensor in database.Values)
        {
            // Simulación de la actualización de la temperatura con un valor aleatorio
            double nuevaTemperatura = sensor.Temperatura + random.NextDouble() * 0.5; // Aumento de temperatura aleatorio entre 0 y 0.5
            UpdateTemperature(sensor.Id, nuevaTemperatura);
        }
    }
}

// Clase principal para simular el sistema de tiempo real
class Program
{
    static void Main(string[] args)
    {
        // Agregamos algunos sensores a la base de datos
        GraphSQL.AddSensor(new Sensor { Id = "1", Ubicacion = "Sala de estar", Temperatura = 25.5 });
        GraphSQL.AddSensor(new Sensor { Id = "2", Ubicacion = "Cocina", Temperatura = 22.0 });
        GraphSQL.AddSensor(new Sensor { Id = "3", Ubicacion = "Dormitorio", Temperatura = 20.8 });

        bool salir = false;

        // Menú interactivo
        while (!salir)
        {
            Console.WriteLine("Seleccione una opción:");
            Console.WriteLine("1. Visualizar sensores y temperaturas");
            Console.WriteLine("2. Agregar sensor");
            Console.WriteLine("3. Eliminar sensor");
            Console.WriteLine("4. Consultar temperatura de un sensor");
            Console.WriteLine("5. Salir");

            string opcion = Console.ReadLine();

            switch (opcion)
            {
                case "1":
                    VisualizarSensoresYTemperaturas();
                    break;
                case "2":
                    AgregarSensor();
                    break;
                case "3":
                    EliminarSensor();
                    break;
                case "4":
                    ConsultarTemperatura();
                    break;
                case "5":
                    salir = true;
                    break;
                default:
                    Console.WriteLine("Opción inválida. Por favor, seleccione una opción válida.");
                    break;
            }
        }
    }

    static void VisualizarSensoresYTemperaturas()
    {
        Console.WriteLine("Sensores y temperaturas:");
        foreach (var sensor in GraphSQL.database.Values)
        {
            Console.WriteLine($"Sensor: {sensor.Id}, Ubicación: {sensor.Ubicacion}, Temperatura: {sensor.Temperatura} °C");
        }
    }

    static void AgregarSensor()
    {
        Console.WriteLine("Ingrese el ID del nuevo sensor:");
        string id = Console.ReadLine();

        Console.WriteLine("Ingrese la ubicación del nuevo sensor:");
        string ubicacion = Console.ReadLine();

        // Verificar si el sensor ya existe
        if (GraphSQL.database.ContainsKey(id))
        {
            Console.WriteLine("Error: El sensor ya existe en la base de datos.");
        }
        else
        {
            // Agregar el nuevo sensor con temperatura predeterminada de 0 °C
            GraphSQL.AddSensor(new Sensor { Id = id, Ubicacion = ubicacion, Temperatura = 0 });
            Console.WriteLine("Sensor agregado correctamente.");
        }
    }

    static void EliminarSensor()
    {
        Console.WriteLine("Ingrese el ID del sensor que desea eliminar:");
        string id = Console.ReadLine();

        // Verificar si el sensor existe
        if (GraphSQL.database.ContainsKey(id))
        {
            // Eliminar el sensor
            GraphSQL.RemoveSensor(id);
            Console.WriteLine("Sensor eliminado correctamente.");
        }
        else
        {
            Console.WriteLine("Error: El sensor no existe en la base de datos.");
        }
    }

    static void ConsultarTemperatura()
    {
        Console.WriteLine("Ingrese el ID del sensor del cual desea consultar la temperatura:");
        string id = Console.ReadLine();

        // Verificar si el sensor existe
        if (GraphSQL.database.ContainsKey(id))
        {
            // Obtener la temperatura del sensor
            double temperatura = GraphSQL.GetTemperature(id);

            // Aumentar ligeramente la temperatura del sensor
            temperatura += 0.1;

            // Actualizar la temperatura en la base de datos
            GraphSQL.UpdateTemperature(id, temperatura);

            Console.WriteLine($"La temperatura del sensor {id} ({GraphSQL.database[id].Ubicacion}) es: {temperatura} °C");
        }
        else
        {
            Console.WriteLine("Error: El sensor no existe en la base de datos.");
        }
    }
}
