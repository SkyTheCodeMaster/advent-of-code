from __future__ import annotations

from typing import TYPE_CHECKING
import re

if TYPE_CHECKING:
  from typing import Tuple,List

with open("4/input.txt") as f:
  data = f.read()

sections = re.compile("(\d+)\-(\d+)")

def splitPairs(pair: str) -> Tuple[List[int],List[int]]:
  one,two = pair.split(",")
  reOne = sections.split(one)
  reTwo = sections.split(two)
  rangeOne = list(range(int(reOne[1]),int(reOne[2])+1))
  rangeTwo = list(range(int(reTwo[1]),int(reTwo[2])+1))
  return rangeOne,rangeTwo

def contains(l1: list,l2: list) -> bool:
  if (l1[0] <= l2[0] and l1[-1] >= l2[-1]) or (l1[0] >= l2[0] and l1[-1] <= l2[-1]):
    return True
  return False

total = 0
for pair in data.splitlines():
  one,two = splitPairs(pair)
  print(one,two,end=" | ")
  contained = contains(one,two)
  print(contained,end=" | ")
  if contained:
    total += 1
  print(total)

print(total)