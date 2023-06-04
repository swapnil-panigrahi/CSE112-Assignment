from . import Constants as Const

UNCON_JUMP = Const.Opcode(0b01111)
JUMP_LESS = Const.Opcode(0b11100)
JUMP_GREAT = Const.Opcode(0b11101)
JUMP_EQUAL = Const.Opcode(0b11111)

br_var = []

#Jump to branch still to be implemented     
def uncon_jmp(instruction):
    label=eval('0b'+instruction[9:])
    return label
  
def less_jmp(instruction):
    label=eval('0b'+instruction[9:])
    if Const.FLAGS & 4:
        return label
    
    return
    
def greater_jmp(instruction):
    label=eval('0b'+instruction[9:])
    if Const.FLAGS & 2:
        return label
    
    return
    
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