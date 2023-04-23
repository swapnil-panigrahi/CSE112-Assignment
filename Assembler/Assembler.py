from ISA import Constants as Const
from ISA import A
from ISA import B
from ISA import C
from ISA import D
from ISA import E
from ISA import F

for i in Const.Register:
    print(i.__repr__())

Const.R1.value=0b0000_0000_0000_0111
Const.R2.value=0b0000_0000_0000_0011

print(A.add("add R0 R1 R2"))

print(Const.R0)