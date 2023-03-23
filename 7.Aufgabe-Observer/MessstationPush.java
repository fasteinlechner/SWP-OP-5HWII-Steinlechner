import java.util.ArrayList;

public class MessstationPush extends Messstation{
    private Data data;
    private ArrayList <IObserver> observers = new ArrayList<IObserver>(); 

    @Override
    public void addObserver(IObserver observer) {
        observers.add(observer);
    }

    @Override
    public void removeObserver(IObserver observer) {
        observers.remove(observer);
    }

    // wird hier nicht gebraucht
    @Override
    public void notifyObserversPull() {
        for(IObserver obs : observers){
            obs.updatePull();
        }
    }

    @Override
    public void notifyObserversPush(Data d) {
        for(IObserver obs : observers){
            obs.updatePush(d);
        }
    }

    public Data getData(){
        return data;
    }

    public void setData(float temp, float hum){
        data = new Data (temp, hum);
        notifyObserversPush(data);
    }
    
}
