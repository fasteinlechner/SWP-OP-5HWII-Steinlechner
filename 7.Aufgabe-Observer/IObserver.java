public interface IObserver{
    public abstract void updatePull();
    public abstract void updatePush(Data d);
}