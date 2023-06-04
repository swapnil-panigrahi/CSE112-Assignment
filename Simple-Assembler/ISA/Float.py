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
            list[2]=float(list[2][1:])
            
            if list[2]>127 or list[2]<0:
                return "ERROR: GIVEN VALUE HAS MORE THAN 7 BITS OR IS NEGATIVE"
        except:
            return "ERROR: INVALID REGISTER CODE OR IMMEDIATE VALUE IS NOT AN INTEGER"
        def float_bin(number, places = 3):
            whole, dec = str(number).split(".")
            whole = int(whole)
            dec = int (dec)
            res = bin(whole).lstrip("0b") + "."
            for x in range(places):
                whole, dec = str((decimal_converter(dec)) * 2).split(".")
                dec = int(dec)
                res += whole
            return res
        def decimal_converter(num):
            while num > 1:
                num /= 10
            return num
        list[2]=float_bin(list[2])
        return f'{MOVF}{list[1].__repr__()}{bin(list[2])[2:].zfill(8)}'