from . import Constants as Const

UNCON_JUMP = Const.Opcode(0b01111)
JUMP_LESS = Const.Opcode(0b11100)
JUMP_GREAT = Const.Opcode(0b11101)
JUMP_EQUAL = Const.Opcode(0b11111)

br_var = []

class Branch:
    def __init__(self,label):
        self.label=label
        
        if not Const.Mem:
            self.address=Const.Mem[-1]+0b1
        else:
            self.address=0b000_0000
    
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
        list[1] = Branch(list[1])
        if list[1].label not in br_var:
            br_var.append(list[1].label)
            
        return f'{UNCON_JUMP}_0000_{list[1].__repr__()}'
    
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
        list[1] = Branch(list[1])
        if list[1].label not in br_var:
            br_var.append(list[1].label)

        return f'{JUMP_LESS}_0000_{list[1].__repr__()}'
    
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
        list[1] = Branch(list[1])
        if list[1].label not in br_var:
            br_var.append(list[1].label)

        return f'{JUMP_GREAT}_0000_{list[1].__repr__()}'
    
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
        list[1] = Branch(list[1])
        if list[1].label not in br_var:
            br_var.append(list[1].label)

        return f'{JUMP_EQUAL}_0000_{list[1].__repr__()}'