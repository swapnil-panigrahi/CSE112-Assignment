from . import Constants as Const

MOVI=Const.Opcode(0b00010)
RS=Const.Opcode(0b01000)
LS=Const.Opcode(0b01001)

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
        
def rs(instruction):
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
            reg=eval("Const."+list[1])
        except:
            return "ERROR: INVALID REGISTER CODE"
    
        reg.value=reg.value<<int(list[2][1:].value)
        return f'{RS}_0_{reg.__repr__()}_'+str(bin(list[2][1:])[2:].zfill(7))

def ls(instruction):
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
            reg=eval("Const."+list[1])
        except:
            return "ERROR: INVALID REGISTER CODE"
    
        reg.value=reg.value>>int(list[2][1:].value)
        return f'{LS}_0_{list[0].__repr__()}_'+str(bin(list[1])[2:].zfill(7))
    