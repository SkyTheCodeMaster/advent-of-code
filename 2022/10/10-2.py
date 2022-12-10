from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
  from typing import Any

with open("10/input.txt") as f:
  data = f.read()


class Instruction:
  time: int # Amount of clocks instruction takes to execute
  data: list[Any]
  def run(self,reg: int) -> int:
    "Take the current register, and return what it should be set to."
    return reg

  def __str__(self) -> str:
    return f"<{self.__class__.__name__} {getattr(self,'data',None) and f'DATA={self.data}'or''} TIME={self.time}>"

class Noop(Instruction):
  time: int = 1

class Addx(Instruction):
  time: int = 2
  def run(self,reg: int) -> int:
    var = int(self.data[0])
    return reg + var

class CPU:
  instructions: list[Instruction]
  clock: int = 0
  remaining: int = 0 # Remaining time on current instruction
  idx: int = -1
  strengths: list[int]
  register: int = 1
  def __init__(self,instructions: list[Instruction]) -> None:
    self.instructions = instructions
    self.strengths = []

  def tick(self) -> bool:
    self.clock += 1
    # If we're done, run the instruction
    if self.remaining <= 0:
      self.register = self.instructions[self.idx].run(self.register)

    if not self.remaining:
      # fetch next
      self.idx += 1

      # if we're at the end of the instructions, return false
      if len(self.instructions) <= self.idx:
        return False

      # grab the instructions
      inst = self.instructions[self.idx]

      # set the remaining time on the instructions (egg timer lol)
      self.remaining = inst.time

    # Process the instruction, remove 1 from time counter
    self.remaining -= 1

    # See if we're on a 40th tick, if so, add a strength
    if (self.clock % 40) - 1 in (self.register-1,self.register,self.register+1):
      print(" ",end="")
    else:
      print("█",end="")
    if (self.clock) % 40 == 0: print()

    return True

instr: dict[str,Instruction] = {
  "noop": Noop,
  "addx": Addx,
}
l: list[Instruction] = []
for line in data.splitlines():
  info = list(line.split(" "))
  opcode = info.pop(0)
  inst = instr[opcode]()
  if info:
    inst.data = [info.pop(0)]
  l.append(inst)

#for i in l:print(i)

cpu = CPU(l)
while cpu.tick():pass