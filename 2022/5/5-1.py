from __future__ import annotations

from typing import TYPE_CHECKING
import re

if TYPE_CHECKING:
  from typing import List,Tuple

#                [B]     [L]     [S]
#        [Q] [J] [C]     [W]     [F]
#    [F] [T] [B] [D]     [P]     [P]
#    [S] [J] [Z] [T]     [B] [C] [H]
#    [L] [H] [H] [Z] [G] [Z] [G] [R]
#[R] [H] [D] [R] [F] [C] [V] [Q] [T]
#[C] [J] [M] [G] [P] [H] [N] [J] [D]
#[H] [B] [R] [S] [R] [T] [S] [R] [L]
# 1   2   3   4   5   6   7   8   9 

containers = [
  ["H","C","R"],
  ["B","J","H","L","S","F"],
  ["R","M","D","H","J","T","Q"],
  ["S","G","R","H","Z","B","J"],
  ["R","P","F","Z","T","D","C","B"],
  ["T","H","C","G"],
  ["S","N","V","Z","B","P","W","L"],
  ["R","J","Q","G","C"],
  ["L","D","T","R","H","P","F","S"],
]

def grabXfromY(x: int, y: int) -> List[int]:
  # Convert to real container
  y-=1
  out = []
  for i in range(x):
    print(containers[y],len(containers[y])-1)
    out.append(containers[y].pop(len(containers[y])-1))
  return out

def moveXfromYtoZ(x: int, y: int, z: int) -> None:
  grabbed = grabXfromY(x,y)
  containers[z-1].extend(grabbed)

def parseMove(move: str) -> Tuple[int,int,int]:
  match = re.match("move (\d+) from (\d+) to (\d+)",move)
  groups = match.groups()
  x = int(groups[0])
  y = int(groups[1])
  z = int(groups[2])
  return x,y,z

def performMove(move: str) -> None:
  print(move)
  x,y,z = parseMove(move)
  moveXfromYtoZ(x,y,z)

def getTop() -> str:
  out = ""
  for container in containers:
    out += container[-1]
  return out

with open("5/input.txt") as f:
  data = f.read()

for line in data.splitlines():
  performMove(line)

print(getTop())