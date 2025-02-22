import grid
import time
import os
import sys

clear = lambda: os.system('cls')

clear()
sys.argv.append(100)
sys.argv.append(100)
map = grid.Map(int(sys.argv[1]), int(sys.argv[2]))
map.setup()
map.display()

i = 0
while i < 100:
	i += 1
	time.sleep(1)
	clear()
	map.range()
	map.update()
	map.display()
