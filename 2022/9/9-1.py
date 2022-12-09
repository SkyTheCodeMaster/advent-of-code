from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
  pass

with open("9/input.txt") as f:
  data = f.read()

def adjacent(head: tuple[int,int], tail: tuple[int,int]) -> bool:
  # Check if it's directly next to
  return \
    0 <= abs(head[0] - tail[0]) <= 1 and \
    0 <= abs(head[1] - tail[1]) <= 1

def directlyAdjacent(head: tuple[int,int], tail: tuple[int,int]) -> bool:
  if head[0] == tail[0] and head[1] == tail[1]+1:
    return True
  if head[0] == tail[0] and head[1] == tail[1]-1:
    return True
  if head[0] == tail[0]+1 and head[1] == tail[1]:
    return True
  if head[0] == tail[0]-1 and head[1] == tail[1]:
    return True
  return False

class Head:
  pos: tuple[int,int]
  lastPos: tuple[int,int]
  tail: Tail

  def __init__(self,pos:tuple[int,int]=(0,0)) -> None:
    self.pos = pos
    self.pos = pos

  def move(self, direction: str, units: str):
    units = int(units)
    for _ in range(units):
      self.lastPos = self.pos
      match direction:
        case "U":
          self.pos = (self.pos[0], self.pos[1]+1)
        case "D":
          self.pos = (self.pos[0], self.pos[1]-1)
        case "R":
          self.pos = (self.pos[0]+1, self.pos[1])
        case "L":
          self.pos = (self.pos[0]-1, self.pos[1])

      self.tail.move(direction)

class Tail:
  pos: tuple[int,int]
  head: Head
  tail: Tail
  visited: set[tuple[int,int]]

  def __init__(self,head: Head,pos:tuple[int,int]=(0,0)) -> None:
    self.head = head
    self.head.tail = self
    self.pos = pos
    self.visited = set()
    self.tail = None

  def move(self, direction: str):
    if not adjacent(self.head.pos,self.pos):
      #self.pos = (
      #  self.pos[0] + min(max((self.head.pos[0]-self.pos[0]),1),-1),
      #  self.pos[1] + min(max((self.head.pos[1]-self.pos[1]),1),-1)
      #)
      match direction:
        case "U":
          self.pos = (self.pos[0], self.pos[1]+1)
        case "D":
          self.pos = (self.pos[0], self.pos[1]-1)
        case "R":
          self.pos = (self.pos[0]+1, self.pos[1])
        case "L":
          self.pos = (self.pos[0]-1, self.pos[1])
      if not directlyAdjacent(self.head.pos,self.pos):
        self.pos = self.head.lastPos

    self.visited.add(self.pos)
    if self.tail:
      self.tail.move(direction)

head = Head()
tail = Tail(head)

for line in data.splitlines():
  head.move(*line.split())

print(len(tail.visited))