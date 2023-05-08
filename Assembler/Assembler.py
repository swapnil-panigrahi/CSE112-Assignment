from ISA import Constants as Const
from ISA import A
from ISA import B
from ISA import C
from ISA import D
from ISA import E
from ISA import F        

for i in Const.Reg:
    print(i.__repr__())

Const.R0.value=0b0000_0000_0000_0000
Const.R1.value=0b0000_0000_0000_0111
Const.R2.value=0b0000_0000_0000_0011

print(B.right_shift("rs R0 $10"))
print(Const.R0)
print(D.var("var xyz"))

B1=E.Branch("label1")
B1.function(["add R0 R1 R2"])

print(Const.R0)