from . import Constants as Const

ADD=Const.Opcode(0b00000)
SUB=Const.Opcode(0b00001)
MUL=Const.Opcode(0b00110)
XOR=Const.Opcode(0b01010)
OR=Const.Opcode(0b01011)
AND=Const.Opcode(0b01100)

def add(instruction):
        list = [instruction[7:10]]+[instruction[10:13]]+[instruction[13:]]
        for i in list:
            i=Const.decode_register(i)
        list[0].value=list[1].value+list[2].value
            
        if list[0].value >= 0b0000000010000000:
            list[0].value = 0b0000000000000000
            Const.FLAGS.overflow()
                
def sub(instruction):
        list = [instruction[7:10]]+[instruction[10:13]]+[instruction[13:]]
        for i in list:
            i=Const.decode_register(i)
        list[0].value=list[1].value-list[2].value
            
        if list[0].value < 0b0000000000000000:
            list[0].value = 0b0000000000000000
            Const.FLAGS.overflow()

def mul(instruction):
        list = [instruction[7:10]]+[instruction[10:13]]+[instruction[13:]]
        for i in list:
            i=Const.decode_register(i)
        list[0].value=list[1].value*list[2].value
            
        if list[0].value >= 0b0000000010000000:
            list[0].value = 0b0000000000000000
            Const.FLAGS.overflow()

def xor(instruction):
        list = [instruction[7:10]]+[instruction[10:13]]+[instruction[13:]]
        for i in list:
            i=Const.decode_register(i)
        list[0].value=list[1].value^list[2].value
            
def _or_(instruction):
        list = [instruction[7:10]]+[instruction[10:13]]+[instruction[13:]]
        for i in list:
            i=Const.decode_register(i)
        list[0].value=list[1].value | list[2].value
            
def _and_(instruction):
        list = [instruction[7:10]]+[instruction[10:13]]+[instruction[13:]]
        for i in list:
            i=Const.decode_register(i)
        list[0].value=list[1].value & list[2].value