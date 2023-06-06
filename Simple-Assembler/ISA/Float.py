from . import Constants as Const

MOVF=10010
ADDF=10000
SUBF=10001

def float_bin(number):
    whole, dec =str(number).split(".")
    whole=int(whole)
    dec=int(dec)
    if whole==0:
        res="0"+"."
    else:
        res=bin(whole)[2:] + "."
    for i in range(5):
        if decimal_converter(dec)==0:
            res=res+'0'
        else:
            whole, dec = str((decimal_converter(dec)) * 2).split(".")
            dec = int(dec)
            res += whole
    return res

def decimal_converter(num):
    while num > 1:
        num /= 10
    return num

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
            list[2]=float(list[2][1:])
            
            if list[2]>16 or list[2]<0:
                return "ERROR: GIVEN VALUE CAN'T BE REPRESENTED IN FLOATING POINT REPRESENTATION"
        except:
            return "ERROR: INVALID REGISTER CODE OR IMMEDIATE VALUE IS NOT AN INTEGER"
        
        c=float_bin(list[2])
        d=len(c)
        count=0
        no_1=0
        no_0=0
        for i in c:
            if i=='0':
                no_0+=1
            if i=='1':
                no_1+=1
            if i=='.':
                break
            count+=1
        if no_1==0:
            new_count=1
            for i in range(count+1,d):
                if c[i]=='1':
                    break
                new_count+=1
            man=c[count+new_count+1:]
            if len(man)>5:
                man=man[:5]
            elif len(man)<5:
                f=5-len(man)
                for i in range(f):
                    man=man+'0'
            exp=3-new_count
            exp=bin(exp)[2:].zfill(3)
        else:
            i=0
            new_count=1
            while(i<count):
                if c[i]=='1':
                    break
                new_count+=1
                i+=1
            g,h=str(c).split('.')
            k=g+h
            man=k[new_count:]
            if len(man)>5:
                man=man[:5]
            elif len(man)<5:
                f=5-len(man)
                for i in range(f):
                    man=man+'0'
            exp=3+(count-new_count)
            exp=bin(exp)[2:].zfill(3)
        return f'{MOVF}{list[1].__repr__()}{exp}{man}'
    
def addf(instruction):    
    list=instruction.split()
    if "FLAGS" in list:
        return "ERROR: FLAGS CANNOT BE AN OPERAND HERE"
    if len(list) > 4:
        return "ERROR: MORE THAN TWO OPERANDS GIVEN"
    if len(list) < 4:
        return "ERROR: INCOMPLETE INSTRUCTION"
    if list[0] != "addf":
        return "ERROR: ILLEGAL ARGUMENT"
    else:
        try:
            list=[eval("Const."+i) for i in list[1:]]
            if list[1].value+list[2].value>=16:
                return "ERROR: GIVEN VALUE CAN'T BE REPRESENTED IN FLOATING POINT REPRESENTATION"
        except:
            return "ERROR: INVALID REGISTER CODE"
        list[0].value=list[1].value+list[2].value
        if list[0].value >= 16:
            list[0].value = 0b0000000000000000
            Const.FLAGS.overflow()
        return f'{ADDF}00{list[0].__repr__()}{list[1].__repr__()}{list[2].__repr__()}'
    
def subf(instruction):    
    list=instruction.split()
    if "FLAGS" in list:
        return "ERROR: FLAGS CANNOT BE AN OPERAND HERE"
    if len(list) > 4:
        return "ERROR: MORE THAN TWO OPERANDS GIVEN"
    if len(list) < 4:
        return "ERROR: INCOMPLETE INSTRUCTION"
    if list[0] != "addf":
        return "ERROR: ILLEGAL ARGUMENT"
    else:
        try:
            list=[eval("Const."+i) for i in list[1:]]
            if list[1].value-list[2].value>16:
                return "ERROR: GIVEN VALUE CAN'T BE REPRESENTED IN FLOATING POINT REPRESENTATION"
        except:
            return "ERROR: INVALID REGISTER CODE"
        list[0].value=list[1].value-list[2].value
        if list[0].value < 0:
            list[0].value = 0b0000000000000000
            Const.FLAGS.overflow()
        return f'{SUBF}00{list[0].__repr__()}{list[1].__repr__()}{list[2].__repr__()}'