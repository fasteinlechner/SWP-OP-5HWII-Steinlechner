public class main {
    public static void main(String[] args){

        Pizzeria hamburg = new HamburgPizzeria();
        IPizza hamSalami = hamburg.producePizza(Sorte.SALAMI);

        Pizzeria rostock = new RostockPizzeria();
        IPizza rosMargherita = rostock.producePizza(Sorte.MARGHERITA);
        


    }
}
