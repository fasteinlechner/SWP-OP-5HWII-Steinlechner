//===================//
// Hamburg Pizza     //
//===================//
class HamMargherita implements IPizza {

    @Override
    public void backen() {
        System.out.println("Pizza Margherita wird in Hamburg gebacken!");
    }

    @Override
    public void schneiden() {
        System.out.println("Pizza Margherita wird in Hamburg geschnitten!");
    }

    @Override
    public void verpacken() {
        System.out.println("Pizza Margherita wird in Hamburg verpackt!");
    }
    
}

class HamSalami implements IPizza {

    @Override
    public void backen() {
        System.out.println("Pizza Salami wird in Hamburg gebacken!");
    }

    @Override
    public void schneiden() {
        System.out.println("Pizza Salami wird in Hamburg geschnitten!");
    }

    @Override
    public void verpacken() {
        System.out.println("Pizza Salami wird in Hamburg verpackt!");
    }
    
}


//===================//
// Rostock Pizza     //
//===================//

class RosMargherita implements IPizza {

    @Override
    public void backen() {
        System.out.println("Pizza Margherita wird in Rostock gebacken!");
    }

    @Override
    public void schneiden() {
        System.out.println("Pizza Margherita wird in Rostock geschnitten!");
    }

    @Override
    public void verpacken() {
        System.out.println("Pizza Margherita wird in Rostock verpackt!");
    }
    
}

class RosSalami implements IPizza {

    @Override
    public void backen() {
        System.out.println("Pizza Salami wird in Rostock gebacken!");
    }

    @Override
    public void schneiden() {
        System.out.println("Pizza Salami wird in Rostock geschnitten!");
    }

    @Override
    public void verpacken() {
        System.out.println("Pizza Salami wird in Rostock verpackt!");
    }
    
}