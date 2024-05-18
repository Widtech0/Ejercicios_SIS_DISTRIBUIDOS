import java.lang.Thread;

// Creamos una clase Corredor que extiende Thread para representar a cada corredor como un hilo
class Corredor extends Thread {
    private int numeroCorredor; 

    public Corredor(int numeroCorredor) {
        this.numeroCorredor = numeroCorredor;
    }

    public void run() {
        // Cuando se inicia el hilo, se imprime un mensaje indicando que el corredor ha comenzado.
        System.out.println("Comienza el corredor " + numeroCorredor); 
        long tiempoInicio = System.currentTimeMillis(); // Se registra el tiempo de inicio de la carrera.
        double tiempoTotal = 0; 

        try {
            // Simula el avance del corredor en la carrera a través de un bucle.
            for (int i = 1; i <= 20; i++) {
                System.out.println("Corredor " + numeroCorredor + " - Metro " + i);

                // Se simula un tiempo de avance aleatorio entre 0.2 y 0.4 segundos.
                double tiempoAvance = (Math.random() * 0.2) + 0.2; 
                tiempoTotal += tiempoAvance; 
                
                Thread.sleep((long)(tiempoAvance * 1000)); 
            }
        } catch (InterruptedException e) {
            System.out.println("Corredor " + numeroCorredor + " interrumpido."); 
        }

        long tiempoFinal = System.currentTimeMillis(); 
        tiempoTotal += (tiempoFinal - tiempoInicio) / 1000.0; 
        
        System.out.println("El corredor " + numeroCorredor + " terminó la carrera en " + tiempoTotal + " segundos.");
    }
}

public class ejemplojava {
    public static void main(String[] args) {
        System.out.println("¡Comienza la carrera!"); 

        Corredor corredor1 = new Corredor(1);
        Corredor corredor2 = new Corredor(2);
        Corredor corredor3 = new Corredor(3);

        // Se inician los hilos de los corredores utilizando el método start().
        corredor1.start();
        corredor2.start();
        corredor3.start();

        try {
            // Se utiliza el método join() para esperar a que todos los hilos de los corredores terminen antes de continuar.
            corredor1.join();
            corredor2.join();
            corredor3.join();
        } catch (InterruptedException e) {
            System.out.println("La carrera fue interrumpida."); 
        }

        // Una vez que todos los corredores han terminado, se imprime un mensaje indicando que la carrera ha terminado.
        System.out.println("¡La carrera ha terminado!"); 
    }
}
