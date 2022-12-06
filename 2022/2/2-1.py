from __future__ import annotations

from enum import Enum

with open("2/input.txt") as f:
  data = f.read()

RPSChoice = Enum("RPSChoice","ROCK PAPER SCISSORS")

trans = {
  "A":"ROCK",
  "B":"PAPER",
  "C":"SCISSORS",
  "X":"ROCK",
  "Y":"PAPER",
  "Z":"SCISSORS"
}

ROCK = RPSChoice.ROCK
PAPER = RPSChoice.PAPER
SCISSORS = RPSChoice.SCISSORS

shapePoints = {
  ROCK: 1,
  PAPER: 2,
  SCISSORS: 3,
}

def rps(me: str,opponent: str) -> int:
  plrChoice = RPSChoice[trans[me]]
  compChoice = RPSChoice[trans[opponent]]
  # Check for player win.
  if (compChoice == ROCK and plrChoice == PAPER) or (compChoice == PAPER and plrChoice == SCISSORS) or (compChoice == SCISSORS and plrChoice == ROCK):
    return 6+shapePoints[plrChoice]
  # Check for computer win.
  elif (compChoice == PAPER and plrChoice == ROCK) or (compChoice == ROCK and plrChoice == SCISSORS) or (compChoice == SCISSORS and plrChoice == PAPER):
    return 0+shapePoints[plrChoice]
  else:
    return 3+shapePoints[plrChoice]

score = 0

for line in data.splitlines():
  op,me = line.split()
  score += rps(me,op)

print(score)