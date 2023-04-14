public abstract class Pizzeria {
    protected abstract IPizza generatePizza(Sorte pizza);

    public IPizza producePizza(Sorte pizza){
        IPizza p = generatePizza(pizza);
        p.backen();
        p.schneiden();
        p.verpacken();

        return p;
    }
}

//===================//
// Hamburg Pizzeria  //
//===================//

class HamburgPizzeria extends Pizzeria {

    @Override
    protected IPizza generatePizza(Sorte pizza) {
        IPizza p = null;

        switch(pizza){
            case MARGHERITA:
                p = new HamMargherita(); break;
            case SALAMI:
                p = new HamSalami(); break;
            default:
                p = new HamMargherita(); break;
        }

        return p;
    }

}

//===================//
// Rostock Pizzeria  //
//===================//

class RostockPizzeria extends Pizzeria {

    @Override
    protected IPizza generatePizza(Sorte pizza) {
        IPizza p = null;

        switch(pizza){
            case MARGHERITA:
                p = new RosMargherita(); break;
            case SALAMI:
                p = new RosSalami(); break;
            default:
                p = new RosMargherita(); break;
        }

        return p;
    }

}
