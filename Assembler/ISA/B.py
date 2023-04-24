from . import Constants as Const

def movi(instruction):
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
        
