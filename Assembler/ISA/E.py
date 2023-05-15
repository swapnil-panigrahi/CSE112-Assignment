from . import Constants as Const

UNCON_JUMP = Const.Opcode(0b01111)
JUMP_LESS = Const.Opcode(0b11100)
JUMP_GREAT = Const.Opcode(0b11101)
JUMP_EQUAL = Const.Opcode(0b11111)

br_var = []

#Jump to branch still to be implemented     
class Branch():
    def __init__(self,label):
        self.label=label
        
        if Const.Mem_block:
            self.address=Const.Mem_block[-1]+0b1
        else:
            self.address=0b000_0000
        
        Const.Mem_block.append(self.address)
        Const.Mem[self.label]=self.address
        
    def __repr__(self):
        return f'{bin(self.address)[2:].zfill(7)}'
    
    def __str__(self):
        return self.label
    
    def function(self,instruction):
        return self,instruction

def uncon_jmp(instruction):
    list = instruction.split()
    
    if "FLAGS" in list:
        return "ERROR: FLAGS CANNOT BE AN OPERAND HERE"
    if len(list) > 2:
        return "ERROR: MORE THAN ONE OPERAND GIVEN"
    if len(list) < 2:
        return "ERROR: INCOMPLETE INSTRUCTION"
    
    if list[0] != "jmp":
        return "ERROR: ILLEGAL ARGUMENT"
    else:
        if list[1] not in br_var:
            return "ERROR: BRANCH NOT DEFINED"
        
        for i in Const.Mem:
            if i==list[1]: 
                return f'{UNCON_JUMP}0000{bin(Const.Mem[i])[2:].zfill(7)}'
    
def less_jmp(instruction):
    list = instruction.split()
    
    if "FLAGS" in list:
        return "ERROR: FLAGS CANNOT BE AN OPERAND HERE"
    if len(list) > 2:
        return "ERROR: MORE THAN ONE OPERAND GIVEN"
    if len(list) < 2:
        return "ERROR: INCOMPLETE INSTRUCTION"
    
    if list[0] != "jlt":
        return "ERROR: ILLEGAL ARGUMENT"
    else:
        if list[1] not in br_var:
            return "ERROR: BRANCH NOT DEFINED"
        
        for i in Const.Mem:
            if i==list[1]: 
                return f'{JUMP_LESS}0000{bin(Const.Mem[i])[2:].zfill(7)}'
    
def greater_jmp(instruction):
    list = instruction.split()
    
    if "FLAGS" in list:
        return "ERROR: FLAGS CANNOT BE AN OPERAND HERE"
    if len(list) > 2:
        return "ERROR: MORE THAN ONE OPERAND GIVEN"
    if len(list) < 2:
        return "ERROR: INCOMPLETE INSTRUCTION"
    
    if list[0] != "jgt":
        return "ERROR: ILLEGAL ARGUMENT"
    else:
        if list[1] not in br_var:
            return "ERROR: BRANCH NOT DEFINED"

        for i in Const.Mem:
            if i==list[1]: 
                return f'{JUMP_GREAT}0000{bin(Const.Mem[i])[2:].zfill(7)}'
    
def equal_jmp(instruction):
    list = instruction.split()
    
    if "FLAGS" in list:
        return "ERROR: FLAGS CANNOT BE AN OPERAND HERE"
    if len(list) > 2:
        return "ERROR: MORE THAN ONE OPERAND GIVEN"
    if len(list) < 2:
        return "ERROR: INCOMPLETE INSTRUCTION"
    
    if list[0] != "je":
        return "ERROR: ILLEGAL ARGUMENT"
    else:
        if list[1] not in br_var:
            return "ERROR: BRANCH NOT DEFINED"

        for i in Const.Mem:
            if i==list[1]: 
                return f'{JUMP_EQUAL}0000{bin(Const.Mem[i])[2:].zfill(7)}'