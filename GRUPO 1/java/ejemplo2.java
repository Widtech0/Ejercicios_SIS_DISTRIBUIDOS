class Corredor implements Runnable {
    private int numeroCorredor; 

    public Corredor(int numeroCorredor) {
        this.numeroCorredor = numeroCorredor;
    }

    public void run() {
        System.out.println("Comienza el corredor " + numeroCorredor); 
        long tiempoInicio = System.currentTimeMillis(); 
        double tiempoTotal = 0; 

        try {
            for (int i = 1; i <= 20; i++) {
                System.out.println("Corredor " + numeroCorredor + " - Metro " + i);
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

public class ejemplo2 {
    public static void main(String[] args) {
        System.out.println("¡Comienza la carrera!"); 

        Corredor corredor1 = new Corredor(1);
        Corredor corredor2 = new Corredor(2);
        Corredor corredor3 = new Corredor(3);

        Thread hiloCorredor1 = new Thread(corredor1);
        Thread hiloCorredor2 = new Thread(corredor2);
        Thread hiloCorredor3 = new Thread(corredor3);

        hiloCorredor1.start();
        hiloCorredor2.start();
        hiloCorredor3.start();

        try {
            hiloCorredor1.join();
            hiloCorredor2.join();
            hiloCorredor3.join();
        } catch (InterruptedException e) {
            System.out.println("La carrera fue interrumpida."); 
        }

        System.out.println("¡La carrera ha terminado!"); 
    }
}
