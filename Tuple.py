class tuple:
    def __init__(self,a,b):
        self.x = a
        self.y = b
    
    def get_x(self):
        return self.x

    def get_y(self):
        return self.y
    
    def set_xy(self, a,b):
        self.x = a
        self.y = b
    
    # Addition
    def Addition(self,tup):
        print(tup[0]+tup[1])
    
    # Substarction 
    def Subtraction (self,tup):
        print(tup[0]-tup[1])

    # Multiplication
    def Multiplication(self,tup):
        print(tup[0]*tup[1])

    # Devision
    def Division(self,tup):
        print(tup[0]/tup[1])

    # Power
    def Power(self,tup):
        print(tup[0]**tup[1])
