from . import Constants as Const

UNCON_JUMP = Const.Opcode(0b01111)
JUMP_LESS = Const.Opcode(0b11100)
JUMP_GREAT = Const.Opcode(0b11101)
JUMP_EQUAL = Const.Opcode(0b11111)

class Branch:
    def __init__(self,label):
        self.label=label
        
        if not Const.Mem:
            self.address=Const.Mem[-1]+0b1
        else:
            self.address=0b000_0000
    
    def __repr__(self):
        return self.address
    
    def __str__(self):
        return self.label
    
    def function(self,instruction):
        return self,instruction

