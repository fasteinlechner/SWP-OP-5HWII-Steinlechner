public class AnzeigePull implements IObserver{
    private MessstationPull messstation;
    private Data data;

    public AnzeigePull(MessstationPull m){
        messstation = m;
        messstation.addObserver(this);
    }
    @Override
    public void updatePull(){
        data = messstation.getData();
    }

    public void print(){
        System.out.println("Temperature: " + data.getTemperature() + " Humidity: " + data.getHumidity());
    }


    //---------------------------------------------------------------
    // wird hier nicht gebraucht
    //---------------------------------------------------------------

    @Override
    public void updatePush(Data d) {
        data = d;
    }
}
