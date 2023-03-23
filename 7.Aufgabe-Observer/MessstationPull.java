import java.util.ArrayList;

public class MessstationPull extends Messstation{
    private ArrayList <IObserver> observers = new ArrayList<IObserver>(); 
    private Data data;
    @Override
    public void addObserver(IObserver observer) {
        observers.add(observer);
    }

    @Override
    public void removeObserver(IObserver observer) {
        observers.remove(observer);
    }
    @Override
    public void notifyObserversPull(){
        for (IObserver observer : observers){
            observer.updatePull();
        }
    }

    @Override
    public void notifyObserversPush(Data d){
        for (IObserver observer : observers){
            observer.updatePush(d);
        }
    }
   

    public void setData(float temp, float hum){
        data = new Data (temp, hum);
        notifyObserversPull();
    }
    public Data getData(){
        return data;
    }


}