class Pow_Object:
    def __init__(self, base, pot):
        self.base = base
        self.pot = pot
        

if __name__ == "__main__":
    obj1 = Pow_Object(1,1)
    obj2 = Pow_Object(2,2)
    obj3 = Pow_Object(3,3)
    pow_obj_list = []
    pow_obj_list.append(obj1)
    pow_obj_list.append(obj2)
    pow_obj_list.append(obj3)
    a=(2,1)
    pow_list = list(map(lambda x: pow(x.base, x.pot), pow_obj_list))
    print(pow_list)
    
    
