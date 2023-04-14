public class DruckerProxy implements IDrucker{
    private IDrucker d;

    public DruckerProxy (){
        this.d = new SWDrucker();
    }
    @Override
    public void drucken(String serverhost) {
        this.d.drucken(serverhost);
    }

    public void switchDrucker(IDrucker d){
        this.d = d;
    }
}
