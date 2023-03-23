import java.util.ArrayList;

public abstract class Messstation{
    private ArrayList <IObserver> observers = new ArrayList<IObserver>(); 
    public void addObserver(IObserver observer){
        observers.add(observer);
    }
    public void removeObserver(IObserver observer){
        observers.remove(observer);
    }
    public void notifyObserversPush(Data d){
        for (IObserver observer : observers){
            observer.updatePush(d);
        }
    }
    public void notifyObserversPull(){
        for (IObserver observer : observers){
            observer.updatePull();
        }
    }
}