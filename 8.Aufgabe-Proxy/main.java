public class main {
    public static void main(String[] args){

        DruckerProxy drucker = new DruckerProxy();
        drucker.drucken("Fabian Steinlechner");

        drucker.switchDrucker(new Farbdrucker());
        drucker.drucken("Max Verstappen");
    }
}
