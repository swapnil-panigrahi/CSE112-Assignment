from . import Constants as Const

LOAD=Const.Opcode(0b00100)
STORE = Const.Opcode(0b00101)

def var(instruction):
    list=instruction.split()
    
    if "FLAGS" in list:
        return "ERROR: FLAGS CANNOT BE AN OPERAND HERE"
    if len(list) > 2:
        return "ERROR: MORE THAN ONE OPERAND GIVEN"
    if len(list) < 2:
        return "ERROR: INCOMPLETE INSTRUCTION"
    
    if list[0]!="var":
        return "ERROR: ILLEGAL ARGUMENT"
    else:        
        if not(Const.Mem):
            list[1]=Const.Memory(list[1],0b0000_0000_0000_0000)
            Const.Mem.append(list[1])
        else:
            list[1]=Const.Memory(Const.Mem[-1]+0b1)
            
        #return f'{list[1].__repr__()}' 

def load(instruction):
    list = instruction.split()
    
    if "FLAGS" in list:
        return "ERROR: FLAGS CANNOT BE AN OPERAND HERE"
    if len(list) > 3:
        return "ERROR: MORE THAN ONE OPERAND GIVEN"
    if len(list) < 3:
        return "ERROR: INCOMPLETE INSTRUCTION"
    
    if list[0] != "ld":
        return "ERROR: ILLEGAL ARGUMENT"
    else:
        try:
            t = eval("Const."+list[1])
        except:
            return "ERROR: INVALID REGISTER CODE"
        for i in Const.Mem:
            if i.var == list[2]:
                t.value = i.value
                return f'{LOAD}_0_{t.__repr__()}_{i.__repr__()}'
        return "ERROR: USE OF NOT DECLARED VARIABLE"
    
def store(instruction):
    list = instruction.split()

    if "FLAGS" in list:
        return "ERROR: FLAGS CANNOT BE AN OPERAND HERE"
    if len(list) > 3:
        return "ERROR: MORE THAN ONE OPERAND GIVEN"
    if len(list) < 3:
        return "ERROR: INCOMPLETE INSTRUCTION"
    
    if list[0] != "st":
        return "ERROR: ILLEGAL ARGUMENT"
    else:
        try:
            t = eval("Const."+list[1])
        except:
            return "ERROR: INVALID REGISTER CODE"
        for i in Const.Mem:
            if i.var == list[2]:
                i.value = t.value
                return f'{STORE}_0_{t.__repr__()}_{i.__repr__()}'
        return "ERROR: USE OF NOT DECLARED VARIABLE"