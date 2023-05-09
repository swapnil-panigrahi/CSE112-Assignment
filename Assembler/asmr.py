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
    print(i.strip().split()[0])