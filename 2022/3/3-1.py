from __future__ import annotations

from typing import TYPE_CHECKING
import math

if TYPE_CHECKING:
  from typing import Tuple

with open("3/input.txt") as f:
  data = f.read()

def priority(char: str) -> int:
  return char.isupper() and ord(char)-38 or ord(char)-96

def removeAll(l: list, element):
  finished = False
  while not finished:
    try:
      l.remove(element)
    except ValueError:
      finished = True

def findSame(a: str, b: str) -> str:
  one = [*a]
  two = [*b]
  for letter in one.copy():
    if not two.count(letter):
      removeAll(one,letter)
  for letter in two.copy():
    if not one.count(letter):
      removeAll(two,letter)
  return one[0]

def splitLine(line: str) -> Tuple[str,str]:
  length = len(line)
  return line[0:math.floor(length/2)],line[math.floor(length/2):length]

totalPriority = 0

for line in data.splitlines():
  a,b = splitLine(line)
  same = findSame(a,b)
  totalPriority += priority(same)

with open("3/output.txt","w") as f:
  f.write(str(totalPriority))