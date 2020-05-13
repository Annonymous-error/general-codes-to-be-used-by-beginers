

class phone: #base class 
    def __initt__(self, brand,model ,price):
        self.brand = brand
        self.model = model
        self.price=max(price,0) #sso as to reject non negative values
        
        
        
        def full_name(self):    #class fuction
            return f"{self.brand}{self.model}"
        
        
        def make_a_call(self):  #class fuction
            return f"caliing {number}..."
    
    
    
class smartphone: #  carries all properties of phone
    def __initt__(self, brand,model ,price,ram, internal_mem,rear_cam ):
        super().__init__(brand,model,price)
        self.ram= ram
        self.internal_mem = internal_mem
        self.rear_cam =rear_cam 
        def full_name(self):    #class fuction
            return f"{self.brand}{self.model}{ram}"
        
class flagshipphone: #  carries all properties of phone
    def __initt__(self, brand,model ,price,ram, internal_mem,rear_cam,front_cam):
        super().__init__(brand,model ,price,ram, internal_mem,rear_cam)
        self.front_cam =front_cam
        
        
#python searches methods from child to parent = Method resolution order
# print(help(flagshipphone()))
issubclass(smartphone,phone)    # to check given class is subclass ie smartphone is of phone
 