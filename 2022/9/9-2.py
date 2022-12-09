from __future__ import annotations
import math
with open("9/input.txt") as f:
  data = f.read()

def adjacent(head: tuple[int,int], tail: tuple[int,int]) -> bool:
  # Check if it's directly next to
  return \
    math.sqrt(math.pow(head[0] - tail[0], 2) + math.pow(head[1] - tail[1], 2)) <= 1.42

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
    self.lastPos = pos

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
      #board = [['.' for __ in range(40)] for _ in range(40)]
      #last = lastTail
      #i = 9
      #while getattr(last,"head",None) is not None:
      #  pos = last.pos
      #  board[pos[1]][pos[0]] = str(i)
      #  i-=1
      #  last = last.head
      #board[head.pos[1]][head.pos[0]] = "H"
      #print("\n".join(["".join(x) for x in board]))
      #print("-"*40)
    
  def __len__(self) -> int:
    return 1

class Tail:
  pos: tuple[int,int]
  lastPos: tuple[int,int]
  head: Head
  tail: Tail
  visited: set[tuple[int,int]]

  def __init__(self,head: Head,pos:tuple[int,int]=(0,0)) -> None:
    self.head = head
    self.head.tail = self
    self.pos = pos
    self.visited = set()
    self.tail = None
    self.lastPos = pos

  def move(self, direction: str):
    if not adjacent(self.head.pos,self.pos):
      self.lastPos = self.pos
      diffX = self.head.pos[0]-self.pos[0]
      diffY = self.head.pos[1]-self.pos[1]

      #if diffX > 0:
      #  self.pos = (self.pos[0]+1,self.pos[1])
      #elif diffX < 0:
      #  self.pos = (self.pos[0]-1,self.pos[1])

      #if diffY > 0:
      #  self.pos = (self.pos[0],self.pos[1]+1)
      #elif diffX < 0:
      #  self.pos = (self.pos[0],self.pos[1]-1)

      self.pos = (self.pos[0]+max(min(self.head.pos[0]-self.pos[0],1),-1),self.pos[1]+max(min(self.head.pos[1]-self.pos[1],1),-1))

      self.visited.add(self.pos)
    if self.tail:
      self.tail.move(direction)

  def __len__(self) -> int:
    return len(self.head) + 1

# We now have 9 rope segments, so we need more Tails
head = Head()
lastTail = Tail(head)
for _ in range(8):
  lastTail = Tail(lastTail)

for line in data.splitlines():
  head.move(*line.split())

print(len(lastTail.visited))