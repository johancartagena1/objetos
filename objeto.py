print("hola mundo soy el rey del mundo opp poo")

class carro():
    
    def  __init__(self, name):
        self.nombre = name
        
    def saber_modelo(self):
        print("ford rapor price 2021")
        
    
    def su_aceleracion(self, info):
        print("el carro ford acelera a ", info)
        
    
    def puede_transportar(self, info):
        print("el carro ford puede transportar a ",info, "personas ")
        
    
    def su_precio(self):
        print("su valor es de 59,000 dolares Estadonidense")
        
  
    def su_motor(self):
        print("su motor es de  3.5L D35 twin-turbo V6 gasoline")
       
       
    def su_consumo(self):
        print("el carro consume 19,88 l/100km	43.027 km y 8.555 l")
       

ford_raptor = carro("ford raptor")
ford_raptor.saber_modelo()
ford_raptor.su_aceleracion("de 0 a 100 km/h en solo 4.1 segundos")
ford_raptor.puede_transportar("5-7")
ford_raptor.su_precio()
ford_raptor.su_motor()
ford_raptor.su_consumo()
