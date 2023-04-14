public class Farbdrucker implements IDrucker {

    @Override
    public void drucken(String serverhost) {
        System.out.println("Nachricht von: " + serverhost + " wird in FARBE gedruckt!");
    }
    
}
