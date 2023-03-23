public class Data {
    private float temperature;
    private float humidity;

    public Data (float temp, float hum){
        temperature = temp;
        humidity = hum;
    }
    public void setTemperature(float temp){
        temperature = temp;
    }
    public void setHumidity(float hum){
        humidity = hum;
    }
    public float getTemperature(){
        return temperature;
    }
    public float getHumidity(){
        return humidity;
    }
}
