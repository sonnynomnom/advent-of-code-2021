# https://adventofcode.com/2021/day/2

f = open('/Users/sonny/Desktop/advent-of-code-2021/day2/commands.txt', 'r')
data = f.read()
splat = data.split("\n")

commands = []

for number, command in enumerate(splat, 1):
  commands += [str(command)]

# ========== Part 1 ==========

horizontal = 0
depth = 0

for i in range(len(commands)):
  if commands[i][0] == 'f':
    horizontal += int(commands[i][len(commands[i])-1])
  if commands[i][0] == 'u':
    depth -= int(commands[i][len(commands[i])-1])
  if commands[i][0] == 'd':
    depth += int(commands[i][len(commands[i])-1])

print(horizontal * depth)

# ========== Part 2 ==========

horizontal = 0
depth = 0
aim = 0

for i in range(len(commands)):
  if commands[i][0] == 'f':
    horizontal += int(commands[i][len(commands[i])-1])
    depth += aim * int(commands[i][len(commands[i])-1])
  if commands[i][0] == 'u':
    aim -= int(commands[i][len(commands[i])-1])
  if commands[i][0] == 'd':
    aim += int(commands[i][len(commands[i])-1])

print(horizontal * depth)
