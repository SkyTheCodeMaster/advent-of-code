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
def isVisible(l:list[list[int]], x: int, y: int) -> int:
  # Check if the tree is on the border, if true, then it is visible.
  if x==0 or y==0: return True
  if x==len(l[y]) or y==len(l): return True
  height = l[y][x]
  score = 0
  
  # Check if the tree is visible from the top
  tScore = 0
  for i in range(y-1,-1,-1):
    tScore +=1
    if l[i][x] >= height:
      #tScore -=1
      break

  # Check if the tree is visible from the bottom
  bScore = 0
  for i in range(y+1,len(l)):
    bScore +=1
    if l[i][x] >= height:
      #bScore -=1
      break

  # Check if the tree is visible from the left.
  lScore = 0
  for i in range(x-1,-1,-1):
    lScore +=1
    if l[y][i] >= height:
      #lScore -=1
      break

  # Check if the tree is visible from the right.
  rScore = 0
  for i in range(x+1,len(l[y])):
    rScore +=1
    if l[y][i] >= height:
      #rScore -=1
      break

  return rScore*lScore*tScore*bScore
def process(l:list[list[int]]) -> int:
  # get the number of trees
  scores = []
  for y in range(len(l)):
    for x in range(len(l[y])):
      scores.append(isVisible(l,x,y))
  scores.sort(reverse=True)
  return scores[0]

l = parse(data)
total = process(l)
print(total)