import os
from ISA import Constants as Const
from ISA import A
from ISA import B
from ISA import C
from ISA import D
from ISA import E
from ISA import F        

def instruction_decode(instruction):
        instr_header=instruction.strip().split()[0].strip(':')

        if instr_header=="add":
            return A.add(instruction.strip())
        elif instr_header=='sub':
            return A.sub(instruction.strip())
        elif instr_header=='mul':
            return A.mul(instruction.strip())
        elif instr_header=='xor':
            return A.xor(instruction.strip())
        elif instr_header=='or':
            return A._or_(instruction.strip())
        elif instr_header=='and':
            return A._and_(instruction.strip())
        elif instr_header=='mov':
            if "$" in instruction:
                return B.movi(instruction.strip())
            else:
                return C.movr(instruction.strip())
        elif instr_header=='rs':
            return B.right_shift(instruction.strip())
        elif instr_header=='ls':
            return B.left_shift(instruction.strip())
        elif instr_header=='div':
            return C.div(instruction.strip())
        elif instr_header=='not':
            return C.inv(instruction.strip())
        elif instr_header=='cmp':
            return C.comp(instruction.strip())
        elif instr_header=='var':
            return D.var(instruction.strip())
        elif instr_header=='ld':
            return D.load(instruction.strip())
        elif instr_header=='st':
            return D.store(instruction.strip())
        elif instr_header=='jmp':
            return E.uncon_jmp(instruction.strip())
        elif instr_header=='jlt':
            return E.less_jmp(instruction.strip())
        elif instr_header=='jgt':
            return E.greater_jmp(instruction.strip())
        elif instr_header=='je':
            return E.equal_jmp(instruction.strip())
        elif instr_header=='hlt':
            return F.hlt(instruction.strip())
        else:
            if instr_header not in E.br_var:
                return 'ERROR: INVALID INSTRUCTION OR BRANCH PASSED'
            else:
                for j in instruction.split(': ')[1:]:
                    return instruction_decode(j.strip())

cwd=os.getcwd()
test_files=os.listdir(f'{cwd}/CSE112-Assignment/Assembler/tests/input_cases')

for i in test_files:
    files=os.listdir(f'{cwd}/CSE112-Assignment/Assembler/tests/input_cases/{i}')
    
    try:
        os.mkdir(f'{cwd}/CSE112-Assignment/Assembler/tests/output_cases')
    except:
        pass
    try:
        os.mkdir(f'{cwd}/CSE112-Assignment/Assembler/tests/output_cases/{i}')
    except:
        pass
    
    for j in files:
        with open(f'{cwd}/CSE112-Assignment/Assembler/tests/input_cases/{i}/{j}') as test_case:
            instr_list=test_case.readlines()
            instr_list=[i for i in instr_list if i.strip()]
            
            Const.Mem_block=[i for i in range(len(instr_list))]
            instr_addr=Const.Mem_block[-1] if Const.Mem else 0
             
            if 'hlt' in instr_list[0]:
                print(f'{cwd}/CSE112-Assignment/Assembler/tests/input_cases/{i}/{j} {bin(0)[2:].zfill(7)}: {instr_list[0].strip()} ERROR: hlt CAN\'T BE THE FIRST INSTRUCTION')
                continue
            
            bin_return=[]
            
            for k in instr_list:
                if k.strip():
                    bin_str=instruction_decode(k)

                    if bin_str!=None and 'ERROR' not in bin_str:
                        bin_return.append(f'{bin(instr_list.index(k))[2:].zfill(7)}: {bin_str}\n')
                    elif bin_str==None:
                        pass
                    else:
                        print(f'{cwd}/CSE112-Assignment/Assembler/tests/input_cases/{i}/{j} {bin(instr_list.index(k))[2:].zfill(7)}: {k.strip()} {bin_str}')
                        break            
            
            else:
                output_case=open(f'{cwd}/CSE112-Assignment/Assembler/tests/output_cases/{i}/{j}.txt',"w")
                
                output_case.writelines(bin_return)
                output_case.close()