from ISA import Constants as Const
from ISA import A
from ISA import B
from ISA import C
from ISA import D
from ISA import E
from ISA import F        

def instruction_decode(instruction):
        instr=instruction.strip().split()[0].strip(':')

        if instr=="add":
            return A.add(instruction.strip())
        elif instr=='sub':
            return A.sub(instruction.strip())
        elif instr=='mul':
            return A.mul(instruction.strip())
        elif instr=='xor':
            return A.xor(instruction.strip())
        elif instr=='or':
            return A._or_(instruction.strip())
        elif instr=='and':
            return A._and_(instruction.strip())
        elif instr=='mov':
            if "$" in instruction:
                return B.movi(instruction.strip())
            else:
                return C.movr(instruction.strip())
        elif instr=='rs':
            return B.right_shift(instruction.strip())
        elif instr=='ls':
            return B.left_shift(instruction.strip())
        elif instr=='div':
            return C.div(instruction.strip())
        elif instr=='not':
            return C.inv(instruction.strip())
        elif instr=='comp':
            return C.comp(instruction.strip())
        elif instr=='var':
            return D.var(instruction.strip())
        elif instr=='load':
            return D.load(instruction.strip())
        elif instr=='store':
            return D.store(instruction.strip())
        elif instr=='jmp':
            return E.uncon_jmp(instruction.strip())
        elif instr=='jlt':
            return E.less_jmp(instruction.strip())
        elif instr=='jgt':
            return E.greater_jmp(instruction.strip())
        elif instr=='je':
            return E.equal_jmp(instruction.strip())
        elif instr=='hlt':
            return F.hlt(instruction.strip())
        else:
            if instr not in E.br_var:
                return f'INVALID INSTRUCTION OR BRANCH PASSED'
            else:
                for j in instruction.split(': ')[1:]:
                    return instruction_decode(j.strip())

test_file = open(r'Assembler/tests/errorGen/test1', "r")
instr_list=test_file.readlines()
for i in instr_list:
    print(instruction_decode(i.strip()))