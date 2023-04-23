class Register:
    def __init__(self,address):
        self.address=address
        self.value=0b0000_0000_0000_0000
        
    def __repr__(self):
        return f'0b{bin(self.address)[2:].zfill(3)}'
    
    def __str__(self):
        return f'0b{bin(self.value)[2:].zfill(16)}'
    
class Opcode:
    def __init__(self,opcode):
        self.opcode=opcode

class Flag(Register):
    def __init__(self,address):
        super().__init__(address)
        
    def overflow(self):
        self.value |= 0b0000_0000_0000_1000
    
    def less_than(self):
        self.value |= 0b0000_0000_0000_0100
    
    def greater_than(self):
        self.value |= 0b0000_0000_0000_0010
    
    def equal(self):
        self.value |= 0b0000_0000_0000_0001

    
R0=Register(0b000)
R1=Register(0b001)
R2=Register(0b010)
R3=Register(0b011)
R4=Register(0b100)
R5=Register(0b101)
R6=Register(0b110)

FLAG=Flag(0b111)

Register=[R0,R1,R2,R3,R4,R5,R6,FLAG]