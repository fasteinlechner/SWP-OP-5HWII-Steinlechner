public class main {

    public static void main(String[] args){
        MessstationPull mpull = new MessstationPull();
        AnzeigePull apull = new AnzeigePull(mpull);

        MessstationPush mpush = new MessstationPush();
        AnzeigePush apush = new AnzeigePush(mpush);

        System.out.println("Observer - PULL");
        mpull.setData(15,40);
        apull.print();
        mpull.setData(20, 50);
        apull.print();

        System.out.println("Observer- PUSH");
        mpush.setData(10,10);
        apush.print();
        mpush.setData(30, 60);
        apush.print();



    }
    
}
