from __future__ import annotations

import math
import re
from typing import TYPE_CHECKING

if TYPE_CHECKING:
  from typing import Union

with open("11/input.txt") as f:
  data = f.read()

monkies: list[Monkey] = []
supermodulo = 1

class Monkey:
  id: int
  inv: list[int]
  operation: str
  test: str
  test_t: int # Monkey to throw to
  test_f: int # ^^^

  inspected: int = 0

  def __init__(self,id:int,inv:list[int],operation:str,test:str,test_t:int,test_f:int) -> None:
    self.id = id
    self.inv = inv
    self.operation = operation
    self.test = test
    self.test_t = test_t
    self.test_f = test_f

  def _evaluate(self,math:str) -> Union[float,int]:
    match = re.match("(\d+) ([\+\*]) (\d+)",math)
    groups = match.groups()
    x,y = int(groups[0]),int(groups[2])
    match groups[1]:
      case "+":
        return x+y
      case "*":
        return x*y

  def processTest(self,item:int) -> bool:
    # here we must parse the test string.
    op = self.operation.replace("old",str(item))
    res = self._evaluate(op)
    match = re.match("divisible by (\d+)",self.test)
    div = int(match.group(1))

    return res%div==0,res%supermodulo

  def processInventory(self) -> None:
    for item in self.inv.copy():
      ok,worry = self.processTest(item)
      if ok:
        monkies[self.test_t].inv.append(worry)
        self.inv.remove(item)
        self.inspected += 1
      else:
        monkies[self.test_f].inv.append(worry)
        self.inv.remove(item)
        self.inspected += 1

for match in re.finditer("Monkey (\d+):\n  Starting items: (.+)\n  Operation: new = (.+)\n  Test: (.+)\n    If true: throw to monkey (\d+)\n    If false: throw to monkey (\d+)",data):
  monkey_id = int(match.group(1))
  monkey_inv = match.group(2)
  monkey_operation = match.group(3)
  monkey_test = match.group(4)
  monkey_test_t = int(match.group(5))
  monkey_test_f = int(match.group(6))
  parsed_inv = []
  for match in re.finditer("(\d+),?",monkey_inv):
    parsed_inv.append(int(match.group(1)))

  monkey = Monkey(monkey_id,parsed_inv,monkey_operation,monkey_test,monkey_test_t,monkey_test_f)
  monkies.insert(monkey_id,monkey)

divs = []
for monkey in monkies:
  # calculate supermodulo
  match = re.match("divisible by (\d+)",monkey.test)
  div = int(match.group(1))
  supermodulo *= div

for round in range(10000):
  for monkey in monkies:
    monkey.processInventory()
for monkey in monkies:
  print(f"Monkey {monkey.id} inspected items {monkey.inspected} times.")

inspection = [monkey.inspected for monkey in monkies]
inspection.sort(reverse=True)
print(f"\nThe level of monkey business is {inspection[0]*inspection[1]}.")
