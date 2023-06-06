from . import Constants as Const

MOVI=Const.Opcode(0b00010)
RIGHT_S=Const.Opcode(0b01000)
LEFT_S=Const.Opcode(0b01001)

def movi(instruction):
    list = [instruction[6:9]]+[instruction[9:]]
    list[0]=Const.decode_register(list[0])
    list[1]=eval('0b'+list[1])
    
    list[0].value=list[1]
        
def right_shift(instruction):
    list = [instruction[6:9]]+[instruction[9:]]
    list[0]=Const.decode_register(list[0])
    list[1]=eval('0b'+list[1])
    
    list[0].value=list[0].value >> list[1]
    
def left_shift(instruction):
    list = [instruction[6:9]]+[instruction[9:]]
    list[0]=Const.decode_register(list[0])
    list[1]=eval('0b'+list[1])
    
    list[0].value=list[0].value << list[1]