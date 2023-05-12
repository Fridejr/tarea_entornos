from funciones import op_and as bit_and
from funciones import op_or as bit_or
from funciones import op_exOr as bit_exOr
from funciones import op_shiftL as bit_shiftL
from funciones import op_shiftR as bit_shiftR

#tambien se puede hacer mas simple asi pero lo veo mejor como lo tengo arriba
#from tarea21abril import op_and as bit_and, op_or as bit_or, op_exOr as bit_exOr, op_shiftL as bit_shiftL, op_shiftR as bit_shiftR, op_not as bit_not

print(bit_and(234,542))
print(bit_or(76,43))
print(bit_exOr(53575,75457))
print(bit_shiftL(56,87))
print(bit_shiftR(34,56))
