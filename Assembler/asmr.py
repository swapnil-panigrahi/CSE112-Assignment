from ISA import Constants as Const
from ISA import A
from ISA import B
from ISA import C
from ISA import D
from ISA import E
from ISA import F        


f = open(r"Assembler/tests/errorGen/test1", "r")
l=f.readlines()
for i in l:
    k=i.strip().split()[0]
    if k not in Const.Instructions:
        k='None'
    if k!='None':
        if k=="add":
            A.add(i.strip())
        elif k=='sub':
            A.sub(i.strip())
        elif k=='mul':
            A.mul(i.strip())
        elif k=='xor':
            A.xor(i.strip())
        elif k=='or':
            A._or_(i.strip())
        elif k=='and':
            A._and_(i.strip())
        elif k=='mov':
            if "$" in i:
                B.movi(i.strip())
            else:
                C.movr(i.strip())
        elif k=='rs':
            B.right_shift(i.strip())
        elif k=='ls':
            B.left_shift(i.strip())
        elif k=='div':
            C.div(i.strip())
        elif k=='not':
            C.inv(i.strip())
        elif k=='comp':
            C.comp(i.strip())
        elif k=='load':
            D.load(i.strip())
        elif k=='store':
            D.store(i.strip())
        elif k=='jmp':
            E.uncon_jmp(i.strip())
        elif k=='jlt':
            E.less_jmp(i.strip())
        elif k=='jgt':
            E.greater_jmp(i.strip())
        elif k=='je':
            E.equal_jmp(i.strip())
        elif k=='hlt':
            F.hlt(i.strip())
        else:
            