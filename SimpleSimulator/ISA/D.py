from . import Constants as Const
from . import E

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
        list[1]=Const.Memory(list[1],0b000_0000)
        Const.Mem[list[1].var]=list[1].address
        
        Const.Mem_block.append(list[1].address)


def load(instruction):
    list = [instruction[6:9]]+[instruction[9:]]
    
    list[0]=Const.decode_register(list[0])
    list[1]=Const.decode_memory(list[1])
    
    list[0].value=list[1]
    
def store(instruction):
    list = [instruction[6:9]]+[instruction[9:]]
        
    list[0]=Const.decode_register(list[0])
    list[1]=Const.decode_memory(list[1])
    
    Const.Mem[list[1]]=list[0].value