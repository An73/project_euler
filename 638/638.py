import copy

def create_rectangle(a, b):
	rectangle = [[1 for num_a in range(a)] for num_b in range(b)]
	return rectangle

def printer(rectangle):
	print('****')
	for y in range(len(rectangle)):
		print(rectangle[y])

def line(rectangle):
	printer(rectangle)
	for x in range(len(rectangle[0])):
		if (rectangle[0][x] == 1):
			rectangle[0][x] = 0
			printer(rectangle)

def vertical(rectangle, y, x):
	while y >= 0:
		rectangle[y][x] = 0
		y -= 1

def function(rectangle, y):
	#line(copy.deepcopy(rectangle))
	if y > 0:
		for x in range(0, len(rectangle[0])):
			if (rectangle[y][x] == 1):
				vertical(rectangle, y, x)
				line(copy.deepcopy(rectangle))
				#printer(rectangle)
				function(copy.deepcopy(rectangle), y - 1)
	#else:
	#	line(copy.deepcopy(rectangle))


count = 1
rectangle = create_rectangle(3, 3)
line(copy.deepcopy(rectangle))
while count < 3:
	function(copy.deepcopy(rectangle), count)
	count += 1

#def function(rectangle, y, start):
#	rec = copy.deepcopy(rectangle)
#	#line(copy.deepcopy(rectangle))
#	y1 = 1
#	while y1 < y + 1:
#		line(copy.deepcopy(rec))
#		for x in range(0, len(rectangle[0])):
#			if (rec[y1][x] == 1):
#				vertical(rec, y, x)
#			elif x == (len(rectangle[0]) - 1):
#				y1++

				#printer(rectangle)
				#function(copy.deepcopy(rectangle), y + 1, False)

#function(create_rectangle(3, 3), 1, True)

#line(create_rectangle(3, 2))
