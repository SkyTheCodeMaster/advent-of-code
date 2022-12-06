elves = []

with open("1/input.txt") as f:
  data = f.read()

elf = 0
for x in data.splitlines():
  if x == "":
    elves.append(elf)
    elf = 0
  else:
    elf += int(x)

elves.sort(reverse=True)

print(elves)

print(elves[0])