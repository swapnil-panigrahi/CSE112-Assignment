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
    label=eval('0b'+instruction[9:])
    if Const.FLAGS & 1:
        return label

    return