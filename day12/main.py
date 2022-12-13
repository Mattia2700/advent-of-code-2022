import heapq

def can_travel(current: chr, next: chr):
	if current == 'S':
		current = 'a'
	elif next == 'E':
		next = 'z'
	# return ord(current)-1 == ord(next) or ord(current) == ord(next)
	return ord(current)+1 == ord(next) or ord(current) >= ord(next)

def get_neighbors(grid: list, current: tuple):
	i, j = current
	neighbors = []
	if i > 0 and can_travel(grid[i][j], grid[i-1][j]):
		neighbors.append((i-1, j))
	if j < len(grid[0])-1 and can_travel(grid[i][j], grid[i][j+1]):
		neighbors.append((i, j+1))
	if i < len(grid)-1 and can_travel(grid[i][j], grid[i+1][j]):
		neighbors.append((i+1, j))
	if j > 0 and can_travel(grid[i][j], grid[i][j-1]):
		neighbors.append((i, j-1))
	return neighbors

def shortest_path(grid: list, start: tuple, end: tuple):
	distances = {}
	for i in range(len(grid)):
		for j in range(len(grid[0])):
			distances[(i, j)] = float('inf')
	distances[start] = 0
	
	visited = set()
	visited.add(start)

	queue = [(0, start)]
	heapq.heapify(queue)
	while queue != []:
		u = heapq.heappop(queue)[1]
		visited.remove(u)
		for v in get_neighbors(grid, u):
			if distances[u] + 1 < distances[v]:
				if v not in visited:
					heapq.heappush(queue, (distances[u]+1, v))
					visited.add(v)
				else:
					queue.remove((distances[v], v))
					heapq.heappush(queue, (distances[u]+1, v))
				distances[v] = distances[u] + 1
	return distances[end]

def try_all(grid: list, start: tuple, end: tuple):
	i, j = start
	grid[i][j] = 'a'
	shortest = float('inf')

	for i in range(len(grid)):
		for j in range(len(grid[0])):
			if grid[i][j] == 'a':
				shortest = min(shortest, shortest_path(grid, (i, j), end))
	
	return shortest

with open("/home/mattiafranzin/Desktop/aoc2022/day12/input.txt") as f:
		lines = f.read().splitlines()

		start = None
		end = None
		grid = []

		for line in lines:
				grid.append(list(line))
				if 'S' in line:
						start = (grid.index(list(line)), line.index('S'))
				if 'E' in line:
						end = (grid.index(list(line)), line.index('E'))
		
		# print(shortest_path(grid, start, end))
		print(try_all(grid, start, end))
		