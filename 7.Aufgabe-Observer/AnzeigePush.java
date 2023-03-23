public class AnzeigePush implements IObserver {
    private MessstationPush messstation;
    private Data data;

    public AnzeigePush(MessstationPush m){
        messstation = m;
        messstation.addObserver(this);
    }
    // wird nicht benötigt
    @Override
    public void updatePull() {
        data = messstation.getData();
    }
    
    @Override
    public void updatePush(Data d) {
        data = d;
    }

    public void print(){
        System.out.println("Temperature: " + data.getTemperature() + " Humidity: " + data.getHumidity());
    }
    
}
