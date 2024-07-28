from  abc import ABC, abstractmethod 
 
class Transporte(ABC): 
    @abstractmethod 
    def transportar(self): 
        pass 
     
      
class Camion(Transporte): 
    def transportar(self): 
        print("Transportando en camión") 
         
          
class Barco(Transporte): 
    def transportar(self): 
        print("Transportando en barco") 
         
          
class TransporteFactory: 
    def get_transporte(self, tipo_transporte): 
        if tipo_transporte == "camion": 
            return Camion()  
        elif tipo_transporte == "barco": 
            return Barco() 
        else: 
            raise ValueError("Transporte no válido") 
          
def main(): 
    factory = TransporteFactory()  
     
    transporte1 = factory.get_transporte("camion") 
    print(transporte1.transportar()) 
     
    transporte2 = factory.get_transporte("barco") 
    print(transporte2.transportar()) 
     
      
if __name__ == "__main__": 
    main()
         