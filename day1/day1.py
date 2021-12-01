# https://adventofcode.com/2021/day/1

with open('/Users/sonny/Desktop/advent-of-code-2021/day1/depths.txt', 'r') as file:
  depths = [int(line.strip()) for line in file]

# ========== Part 1 ==========

increased = 0

for i in range(len(depths)):
  if (depths[i] - depths[i-1]) > 0:
    increased += 1

print(increased)

# ========== Part 2 ==========

sliding_window = []
sum = 0

for i in range(len(depths)):
  sum = depths[i] + depths[i-1] + depths[i-2]
  sliding_window.append(sum)

increased = 0

for i in range(len(sliding_window)):
  if (sliding_window[i] - sliding_window[i-1]) > 0:
    increased += 1

print(increased)
