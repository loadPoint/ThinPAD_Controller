from enum import unique, Enum
from time import sleep

from thinpad_controller import ThinPadController


def R(index):
    if 0 <= index < 32:
        return '{:05b}'.format(index)
    else:
        raise Exception(f"Register #{index} is not exists")

@unique
class InstrOp(Enum):
    ADD = "0001"
    SUB = "0010"
    AND = "0011"
    OR  = "0100"
    XOR = "0101"
    NOT = "0110"
    SLL = "0111"
    SRL = "1000"
    SRA = "1001"
    ROL = "1010"

def Binary_Instr(TYPE: InstrOp, RD: str, RS1: str, RS2: str) -> str:
    return "0000000" + RS2 + RS1 + "000" + RD + TYPE.value+"001"

def POKE_Instr(imm: int, RD: str) -> str:
    immstr = '{:016b}'.format(imm)
    if len(immstr) == 16:
        return immstr + "0000" + RD + "0001" + "010"
    else:
        raise Exception("Imm number is too long")

def PEEK_Instr(imm: int, RD: str) -> str:
    immstr = '{:016b}'.format(imm)
    if len(immstr) == 16:
        return immstr + "0000" + RD + "0010" + "010"
    else:
        raise Exception("Imm number is too long")

if __name__ == "__main__":
    print("你不该调用这个的")
