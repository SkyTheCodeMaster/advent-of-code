from __future__ import annotations

from typing import TYPE_CHECKING
import re

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

def findSame(a: str, b: str, c: str) -> str:
  return list(set(a)&set(b)&set(c))[0]

totalPriority = 0

for match in re.finditer("^(.*)\n(.*)\n(.*)",data,re.MULTILINE):
  a,b,c = match.groups()
  same = findSame(a,b,c)
  totalPriority += priority(same)

print(totalPriority)