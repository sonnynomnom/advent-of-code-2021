# Advent of Code 2021 - Day 1
# https://adventofcode.com/2021/day/1

# Move each number from depths.txt into a list called depth

with open('/Users/sonny/Desktop/advent-of-code-2021/day1/depths.txt', 'r') as file:
  depths = [int(line.strip()) for line in file]
  # print(depth)

# ========== Part 1 ==========

increased = 0

for i in range(len(depths)):
  if (depths[i] - depths[i-1]) > 0:
    increased += 1

print(increased) # Output: 1557

# ========== Part 2 ==========

sliding_window = []
sum = 0

for i in range(len(depths)):
  sum = depths[i] + depths[i-1] + depths[i-2]
  sliding_window.append(sum)

# print(sliding_window)

increased = 0

for i in range(len(sliding_window)):
  if (sliding_window[i] - sliding_window[i-1]) > 0:
    increased += 1

print(increased) # Output: 1608
