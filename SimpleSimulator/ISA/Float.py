from . import Constants as Const

MOVF=10010
ADDF=10000
SUBF=10001

def movf(instruction):    
    list = [instruction[5:8]]+[instruction[8:]]
    list[0]=Const.decode_register(list[0])
    exp=list[1][:3]
    man=list[1][3:]
    ans1=0
    ans2=0
    for i in range(3):
            ans1=ans1+(2**(2-i)*int(exp[i]))
    ans3=2**(ans1-3)
    for i in range(len(man)):
            ans2=ans2+(2**(-1-i)*int(man[i]))
    ans2=ans2+1
    ans4=ans2*ans3
    list[0].value=ans4

def addf(instruction):
        list = [instruction[7:10]]+[instruction[10:13]]+[instruction[13:]]
        for i in range(3):
            list[i]=Const.decode_register(list[i])
        list[0].value=list[1].value+list[2].value
            
        if list[0].value >= 0b0000000010000000:
            list[0].value = 0b0000000000000000
            Const.FLAGS.overflow()

def subf(instruction):
        list = [instruction[7:10]]+[instruction[10:13]]+[instruction[13:]]
        for i in range(len(list)):
            list[i]=Const.decode_register(list[i])
        list[0].value=list[1].value-list[2].value
            
        if list[0].value < 0b0000000000000000:
            list[0].value = 0b0000000000000000
            Const.FLAGS.overflow()
