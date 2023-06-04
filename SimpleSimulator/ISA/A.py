from . import Constants as Const

ADD=Const.Opcode(0b00000)
SUB=Const.Opcode(0b00001)
MUL=Const.Opcode(0b00110)
XOR=Const.Opcode(0b01010)
OR=Const.Opcode(0b01011)
AND=Const.Opcode(0b01100)

def add(instruction):
    list = instruction.split()
    if "FLAGS" in list:
        return "ERROR: FLAGS CANNOT BE AN OPERAND HERE"
    if len(list) > 4:
        return "ERROR: MORE THAN THREE OPERANDS GIVEN"
    if len(list) < 4:
        return "ERROR: INCOMPLETE INSTRUCTION"
    
    if list[0] != "add":
        return "ERROR: ILLEGAL ARGUMENT"
    else:
        try:
            list=[eval("Const."+i) for i in list[1:]]
        except:
            return "ERROR: INVALID REGISTER CODE"
    
        list[0].value=list[1].value+list[2].value
            
        if list[0].value >= 0b0000000010000000:
            list[0].value = 0b0000000000000000
            Const.FLAGS.overflow()
            
        return f'{ADD}00{list[0].__repr__()}{list[1].__repr__()}{list[2].__repr__()}'
                
def sub(instruction):
    list = instruction.split()
    if "FLAGS" in list:
        return "ERROR: FLAGS CANNOT BE AN OPERAND HERE"
    if len(list) > 4:
        return "ERROR: MORE THAN THREE OPERANDS GIVEN"
    if len(list) < 4:
        return "ERROR: INCOMPLETE INSTRUCTION"
    
    if list[0] != "sub":
        return "ERROR: ILLEGAL ARGUMENT"
    else:
        try:
            list=[eval("Const."+i) for i in list[1:]]
        except:
            return "ERROR: INVALID REGISTER CODE"
        else:
            list[0].value=list[1].value-list[2].value
            
            if list[0].value < 0b0000000000000000:
                list[0].value = 0b0000000000000000
                Const.FLAGS.overflow()
                
        return f'{SUB}00{list[0].__repr__()}{list[1].__repr__()}{list[2].__repr__()}'

def mul(instruction):
    list = instruction.split()
    if "FLAGS" in list:
        return "ERROR: FLAGS CANNOT BE AN OPERAND HERE"
    if len(list) > 4:
        return "ERROR: MORE THAN THREE OPERANDS GIVEN"
    if len(list) < 4:
        return "ERROR: INCOMPLETE INSTRUCTION"
    
    if list[0] != "mul":
        return "ERROR: ILLEGAL ARGUMENT"
    else:
        try:
            list=[eval("Const."+i) for i in list[1:]]
        except:
            return "ERROR: INVALID REGISTER CODE"
        else:
            list[0].value=list[1].value*list[2].value
            
            if list[0].value >= 0b0000000010000000:
                list[0].value = 0b0000000000000000
                Const.FLAGS.overflow()
                
        return f'{MUL}00{list[0].__repr__()}{list[1].__repr__()}{list[2].__repr__()}'

def xor(instruction):
    list = instruction.split()
    if "FLAGS" in list:
        return "ERROR: FLAGS CANNOT BE AN OPERAND HERE"
    if len(list) > 4:
        return "ERROR: MORE THAN THREE OPERANDS GIVEN"
    if len(list) < 4:
        return "ERROR: INCOMPLETE INSTRUCTION"
    
    if list[0] != "xor":
        return "ERROR: ILLEGAL ARGUMENT"
    else:
        try:
            list=[eval("Const."+i) for i in list[1:]]
        except:
            return "ERROR: INVALID REGISTER CODE"
        else:
            list[0].value = list[1].value ^ list[2].value
            
    return f'{XOR}00{list[0].__repr__()}{list[1].__repr__()}{list[2].__repr__()}'
            
def _or_(instruction):
    list = instruction.split()
    if "FLAGS" in list:
        return "ERROR: FLAGS CANNOT BE AN OPERAND HERE"
    if len(list) > 4:
        return "ERROR: MORE THAN THREE OPERANDS GIVEN"
    if len(list) < 4:
        return "ERROR: INCOMPLETE INSTRUCTION"
    
    if list[0] != "or":
        return "ERROR: ILLEGAL ARGUMENT"
    else:
        try:
            list=[eval("Const."+i) for i in list[1:]]
        except:
            return "ERROR: INVALID REGISTER CODE"
        else:
            list[0].value = list[1].value | list[2].value
    
    return f'{OR}00{list[0].__repr__()}{list[1].__repr__()}{list[2].__repr__()}'
            
def _and_(instruction):
    list = instruction.split()
    if "FLAGS" in list:
        return "ERROR: FLAGS CANNOT BE AN OPERAND HERE"
    if len(list) > 4:
        return "ERROR: MORE THAN THREE OPERANDS GIVEN"
    if len(list) < 4:
        return "ERROR: INCOMPLETE INSTRUCTION"
    
    if list[0] != "and":
        return "ERROR: ILLEGAL ARGUMENT"
    else:
        try:
            list=[eval("Const."+i) for i in list[1:]]
        except:
            return "ERROR: INVALID REGISTER CODE"
        else:
            list[0].value = list[1].value & list[2].value
            
    return f'{AND}00{list[0].__repr__()}{list[1].__repr__()}{list[2].__repr__()}'