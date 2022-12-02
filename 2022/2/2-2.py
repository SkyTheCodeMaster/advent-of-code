from __future__ import annotations

from enum import Enum

with open("2/input.txt") as f:
  data = f.read()

RPSChoice = Enum("RPSChoice","ROCK PAPER SCISSORS")
Result = Enum("Result","LOSE DRAW WIN")


trans = {
  "A":"ROCK",
  "B":"PAPER",
  "C":"SCISSORS",
  "X":"LOSE",
  "Y":"DRAW",
  "Z":"WIN"
}

ROCK = RPSChoice.ROCK
PAPER = RPSChoice.PAPER
SCISSORS = RPSChoice.SCISSORS
LOSE = Result.LOSE
DRAW = Result.DRAW
WIN = Result.WIN

def rps(me: str,opponent: str) -> int:
  plrChoice = Result[trans[me]]
  compChoice = RPSChoice[trans[opponent]]
  if plrChoice == LOSE:
    if compChoice == ROCK: # Choose scissors and lose
      return 3
    elif compChoice == PAPER: # Choose rock and lose
      return 1
    elif compChoice == SCISSORS: # Choose paper and lose
      return 2
  elif plrChoice == DRAW:
    if compChoice == ROCK: # Choose rock and draw
      return 4
    elif compChoice == PAPER: # Choose paper and draw
      return 5
    elif compChoice == SCISSORS: # Choose scissors and draw
      return 6
  elif plrChoice == WIN:
    if compChoice == ROCK: # Choose paper and win
      return 8
    elif compChoice == PAPER: # Choose scissors and win
      return 9
    elif compChoice == SCISSORS: # Choose rock and win
      return 7

score = 0

for line in data.splitlines():
  op,me = line.split()
  score += rps(me,op)

with open("2/output.txt","w") as f:
  f.write(str(score))