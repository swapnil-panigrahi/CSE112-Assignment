from . import Constants as Const

MOVI=Const.Opcode(0b00010)
RIGHT_S=Const.Opcode(0b01000)
LEFT_S=Const.Opcode(0b01001)

def movi(instruction):
    list = instruction.split()
    if "FLAGS" in list:
        return "ERROR: FLAGS CANNOT BE AN OPERAND HERE"
    if len(list) > 3:
        return "ERROR: MORE THAN TWO OPERANDS GIVEN"
    if len(list) < 3:
        return "ERROR: INCOMPLETE INSTRUCTION"
    
    if list[0] != "mov":
        return "ERROR: ILLEGAL ARGUMENT"
    else:
        try:
            reg=eval("Const."+list[1])
        except:
            return "ERROR: INVALID REGISTER CODE"
    
        reg.value=list[2][1:].value
        return f'{MOVI}_0_{reg.__repr__()}_'+str(bin(list[2][1:])[2:].zfill(7))
        
def right_shift(instruction):
    list = instruction.split()
    if "FLAGS" in list:
        return "ERROR: FLAGS CANNOT BE AN OPERAND HERE"
    if len(list) > 3:
        return "ERROR: MORE THAN TWO OPERANDS GIVEN"
    if len(list) < 3:
        return "ERROR: INCOMPLETE INSTRUCTION"
    
    if list[0] != "rs":
        return "ERROR: ILLEGAL ARGUMENT"
    else:
        try:
            list[1]=eval("Const."+list[1])
            list[2]=int(list[2][1:])
        except:
            return "ERROR: INVALID REGISTER CODE"
    
        list[1].value=list[1].value << list[2]
        return f'{RIGHT_S}_0_{list[1].__repr__()}_{bin(list[2])[2:].zfill(7)}'

def left_shift(instruction):
    list = instruction.split()
    if "FLAGS" in list:
        return "ERROR: FLAGS CANNOT BE AN OPERAND HERE"
    if len(list) > 3:
        return "ERROR: MORE THAN TWO OPERANDS GIVEN"
    if len(list) < 3:
        return "ERROR: INCOMPLETE INSTRUCTION"
    
    if list[0] != "rs":
        return "ERROR: ILLEGAL ARGUMENT"
    else:
        try:
            list[1]=eval("Const."+list[1])
            list[2]=int(list[2][1:])
        except:
            return "ERROR: INVALID REGISTER CODE"
    
        list[1].value=list[1].value >> list[2]
        return f'{RIGHT_S}_0_{list[1].__repr__()}_{bin(list[2])[2:].zfill(7)}'
    