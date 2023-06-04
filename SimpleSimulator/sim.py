import sys
from ISA import Constants as Const
from ISA import A
from ISA import B
from ISA import C
from ISA import D
from ISA import E
from ISA import F

if __name__ == '__main__':        
            instr_list = str(sys.stdin.readlines())

            i = 0
            while(instr_list[i] != "1101000000000000"):
                    print(bin(i).zfill(7), Const.R0, Const.R1, Const.R2, Const.R3, Const.R4, Const.R5, Const.R6, Const.R7, Const.FLAGS)
                    cmd = str((instr_list[i].strip())[0:6])
                    if(cmd == "00000"):
                            A.add(instr_list[i].strip())
                    elif(cmd == "00001"):
                            A.sub(instr_list[i].strip())
                    elif(cmd == "00010"):
                            B.movi(instr_list[i].strip())
                    elif(cmd == "00011"):
                            C.movr(instr_list[i].strip())
                    elif(cmd == "00100"):
                            D.load(instr_list[i].strip())
                    elif(cmd == "00101"):
                            D.store(instr_list[i].strip())
                    elif(cmd == "00110"):
                            A.mul(instr_list[i].strip())
                    elif(cmd == "00111"):
                            C.div(instr_list[i].strip())
                    elif(cmd == "01000"):
                            B.right_shift(instr_list[i].strip())
                    elif(cmd == "01001"):
                            B.left_shift(instr_list[i].strip())
                    elif(cmd == "01010"):
                            A.xor(instr_list[i].strip())
                    elif(cmd == "01011"):
                            A._or_(instr_list[i].strip())
                    elif(cmd == "01100"):
                            A._and_(instr_list[i].strip())
                    elif(cmd == "01101"):
                            C.inv(instr_list[i].strip())
                    elif(cmd == "01110"):
                            C.comp(instr_list[i].strip())
                    elif(cmd == "01111"):
                            E.uncon_jmp(instr_list[i].strip())
                    elif(cmd == "11100"):
                            E.less_jmp(instr_list[i].strip())
                    elif(cmd == "11101"):
                            E.greater_jmp(instr_list[i].strip())
                    elif(cmd == "11111"):
                            E.equal_jmp(instr_list[i].strip())
                                    
                    if cmd not in ('01111','11100','11101','11111'):
                        i+=1
                    else:
                        if(cmd == "01111"):
                            i=E.uncon_jmp(instr_list[i].strip())
                        elif(cmd == "11100"):
                            i=E.less_jmp(instr_list[i].strip())
                        elif(cmd == "11101"):
                            i=E.greater_jmp(instr_list[i].strip())
                        elif(cmd == "11111"):
                            i=E.equal_jmp(instr_list[i].strip())