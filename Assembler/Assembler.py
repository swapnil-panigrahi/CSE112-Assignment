from ISA import Constants as Const
from ISA import A
from ISA import B
from ISA import C
from ISA import D
from ISA import E
from ISA import F

class Branch:
    def __init__(self,label):
        self.label=label
        
        if not Const.Mem:
            self.address=Const.Mem[-1]+0b1
        else:
            self.address=0b000_0000
    
    def __repr__(self):
        return self.address
    
    def __str__(self):
        return self.label
    
    def function(self,instruction):
        for i in instruction:
            if i.split()[0]=='add':
                A.add(i)
            elif i.split()[0]=='sub':
                A.sub(i)
            elif i.split()[0]=='mul':
                A.mul(i)
            elif i.split()[0]=='xor':
                A.xor(i)
            elif i.split()[0]=='or':
                A._or_(i)
            elif i.split()[0]=='and':
                A._and_(i)
            

for i in Const.Reg:
    print(i.__repr__())

Const.R0.value=0b0000_0000_0000_0000
Const.R1.value=0b0000_0000_0000_0111
Const.R2.value=0b0000_0000_0000_0011

print(B.right_shift("rs R0 $10"))
print(Const.R0)
print(D.var("var xyz"))

B1=Branch("label1")
B1.function(["add R0 R1 R2"])

print(Const.R0)