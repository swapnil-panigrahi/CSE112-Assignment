from . import Constants as Const

MOVR=Const.Opcode(0b00011)
DIV=Const.Opcode(0b00111)
INV=Const.Opcode(0b01101)
COMP=Const.Opcode(0b01110)

def movr(instruction):
    list = instruction.split()
    if "FLAGS" in list:
        return "ERROR: FLAGS CANNOT BE AN OPERAND HERE"
    if len(list) > 3:
        return "ERROR: MORE THAN THREE OPERANDS GIVEN"
    if len(list) < 3:
        return "ERROR: INCOMPLETE INSTRUCTION"
    
    if list[0] != "mov":
        return "ERROR: ILLEGAL ARGUMENT"
    else:
        try:
            list=[eval("Const."+i) for i in list[1:]]
        except:
            return "ERROR: INVALID REGISTER CODE"
    
        list[0].value=list[1].value
        
def div(instruction):
    list = instruction.split()
    if "FLAGS" in list:
        return "ERROR: FLAGS CANNOT BE AN OPERAND HERE"
    if len(list) > 3:
        return "ERROR: MORE THAN THREE OPERANDS GIVEN"
    if len(list) < 3:
        return "ERROR: INCOMPLETE INSTRUCTION"
    
    if list[0] != "div":
        return "ERROR: ILLEGAL ARGUMENT"
    else:
        try:
            list=[eval("Const."+i) for i in list[1:]]
        except:
            return "ERROR: INVALID REGISTER CODE"

        if list[1].value == 0b0000_0000_0000_0000:
            Const.R0.value=0b0000_0000_0000_0000
            Const.R1.value=0b0000_0000_0000_0000
            Const.FLAG.overflow()
        else:
            Const.R0.value=list[0].value//list[1].value
            Const.R1.value=list[0].value%list[1].value
            

            