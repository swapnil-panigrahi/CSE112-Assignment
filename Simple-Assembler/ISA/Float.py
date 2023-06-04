from . import Constants as Const
MOVF=10000

def movf(instruction):    
    list=instruction.split()
    if "FLAGS" in list:
        return "ERROR: FLAGS CANNOT BE AN OPERAND HERE"
    if len(list) > 3:
        return "ERROR: MORE THAN TWO OPERANDS GIVEN"
    if len(list) < 3:
        return "ERROR: INCOMPLETE INSTRUCTION"
    if list[0] != "movf":
        return "ERROR: ILLEGAL ARGUMENT"
    else:
        try:
            list[1]=eval("Const."+list[1])
            list[2]=int(list[2][1:])
            
            if list[2]>127 or list[2]<0:
                return "ERROR: GIVEN VALUE HAS MORE THAN 7 BITS OR IS NEGATIVE"
        except:
            return "ERROR: INVALID REGISTER CODE OR IMMEDIATE VALUE IS NOT AN INTEGER"
    
        return f'{MOVF}0{list[1].__repr__()}{bin(list[2])[2:].zfill(7)}'
    return