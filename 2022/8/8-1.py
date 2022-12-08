from __future__ import annotations

with open("8/input.txt") as f:
  data = f.read()

# Parse data into a 2D list of characters for easy indexing.
def parse(data: str) -> list[list[int]]:
  l = []
  for line in data.splitlines():
    l.append([int(char) for char in line])
  return l

# Figure out if a tree is visible from the edge of the grid
def isVisible(l:list[list[int]], x: int, y: int) -> bool:
  # Check if the tree is on the border, if true, then it is visible.
  if x==0 or y==0: return True
  if x==len(l[y]) or y==len(l): return True
  height = l[y][x]
  visible = True
  
  # Check if the tree is visible from the top
  for i in range(y-1,-1,-1):
    if l[i][x] >= height:
      visible = False
  if visible: return True

  # Check if the tree is visible from the bottom
  visible = True
  for i in range(y+1,len(l)):
    if l[i][x] >= height:
      visible = False
  if visible: return True

  # Check if the tree is visible from the left.
  visible = True
  for i in range(x-1,-1,-1):
    if l[y][i] >= height:
      visible = False
  if visible: return True

  # Check if the tree is visible from the right.
  visible = True
  for i in range(x+1,len(l[y])):
    if l[y][i] >= height:
      visible = False
  if visible: return True

  return False
def process(l:list[list[int]]) -> int:
  # get the number of trees
  total = 0
  for y in range(len(l)):
    for x in range(len(l[y])):
      if isVisible(l,x,y):
        total += 1
  return total

l = parse(data)
total = process(l)
print(total)