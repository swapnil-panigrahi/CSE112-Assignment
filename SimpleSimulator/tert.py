import sys
from ISA import Constants as Const
from ISA import A
from ISA import B
from ISA import C
from ISA import D
from ISA import E
from ISA import F

temp_r=Const.decode_register('000')

print(temp_r.__repr__())
print(temp_r.__str__())