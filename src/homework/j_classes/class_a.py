#write a class die
import random


class  die:
    
    def  roll():
        roll_value = random.randint(1, 6)
        

    def  get_rolled_value(self):
        return  self._rolled_value
    
    def  __str__  (self):
            return f'The rolled value is $(self._rolled_value:, .2f)' 
