from . import Constants as Const

MOVR=Const.Opcode(0b00011)
DIV=Const.Opcode(0b00111)
NOT=Const.Opcode(0b01101)
COMP=Const.Opcode(0b01110)

def movr(instruction):
    list = [instruction[10:13]]+[instruction[13:]]
    for i in list:
        i=Const.decode_register(i)
    list = [instruction[10:13]]+[instruction[13:]]
    for i in list:
        i=Const.decode_register(i)
    
    list[0].value=list[1].value
    list[0].value=list[1].value
        
def div(instruction):
    list = [instruction[10:13]]+[instruction[13:]]
    for i in list:
        i=Const.decode_register(i)
        
    if list[1].value==0:
        Const.FLAGS.overflow()
        Const.R0=0
        Const.R1=0
    list = [instruction[10:13]]+[instruction[13:]]
    for i in list:
        i=Const.decode_register(i)
        
    if list[1].value==0:
        Const.FLAGS.overflow()
        Const.R0=0
        Const.R1=0
    else:
        Const.R0=list[0]//list[1]
        Const.R1=list[0]%list[1]
    
        Const.R0=list[0]//list[1]
        Const.R1=list[0]%list[1]
          
def inv(instruction):
    list = [instruction[10:13]]+[instruction[13:]]
    for i in list:
        i=Const.decode_register(i)
        
    list[0] = -(~(list[1].value))
    list = [instruction[10:13]]+[instruction[13:]]
    for i in list:
        i=Const.decode_register(i)
        
    list[0] = -(~(list[1].value))
    
def comp(instruction):
    list = [instruction[10:13]]+[instruction[13:]]
    for i in list:
        i=Const.decode_register(i)
        
    if list[0].value > list[1].value:
        Const.FLAGS.greater_than()
        
    elif list[0].value < list[1].value:
        Const.FLAGS.less_than()
        
    list = [instruction[10:13]]+[instruction[13:]]
    for i in list:
        i=Const.decode_register(i)
        
    if list[0].value > list[1].value:
        Const.FLAGS.greater_than()
        
    elif list[0].value < list[1].value:
        Const.FLAGS.less_than()
        
    else:
        Const.FLAGS.equal()
        Const.FLAGS.equal()