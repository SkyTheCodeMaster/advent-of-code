from __future__ import annotations

with open("6/input.txt") as f:
  data = f.read()

def checkDuplicates(s: str) -> bool:
  "Check for duplicate characters in the string, returns True if duplicates found."
  return len(s) != len(set(s))

def iterate(s: str) -> int:
  "Iterate over the string, and return the first character marker of a packet."
  for i in range(len(s)):
    substr = s[i:i+14]
    if not checkDuplicates(substr):
      return i+14

marker = iterate(data)
print(marker)