import copy

def create_rectangle(a, b):
	rectangle = [[1 for num_a in range(a)] for num_b in range(b)]
	return rectangle

def area_calculation(rectangle):
	area = 0
	for row in rectangle:
		for elem in row:
			area += elem
	return area

def printer(rectangle):
	print('****')
	for y in range(len(rectangle)):
		print(rectangle[y])

def line(rectangle, power):
	##printer(rectangle)
	power.append(area_calculation(rectangle))
	for x in range(len(rectangle[0])):
		if (rectangle[0][x] == 1):
			rectangle[0][x] = 0
			##printer(rectangle)
			power.append(area_calculation(rectangle))

def vertical(rectangle, y, x):
	while y >= 0:
		rectangle[y][x] = 0
		y -= 1

def function(rectangle, y, power):
	#line(copy.deepcopy(rectangle))
	if y > 0:
		for x in range(0, len(rectangle[0])):
			if (rectangle[y][x] == 1):
				function(copy.deepcopy(rectangle), y - 1, power)
				vertical(rectangle, y, x)
				line(copy.deepcopy(rectangle), power)
				#function(copy.deepcopy(rectangle), y - 1, power)
				#printer(rectangle)
				#function(copy.deepcopy(rectangle), y - 1, power)
	#else:
	#	line(copy.deepcopy(rectangle))

def calculation_c(a, b, k):
	summa = 0
	power = []
	rectangle = create_rectangle(a, b)
	line(copy.deepcopy(rectangle), power)
	function(copy.deepcopy(rectangle), b - 1, power)
	for i in power:
		summa += k ** i
	print(power)
	return summa

#k = 1
#result = 0
#while k < 8:
#	print('->>' + str(k))
#	result += calculation_c((10 ** k) + k, (10 ** k) + k, k)
#	k += 1
#print(result % 1000000007)

print(calculation_c(3, 3, 1))


#count = 1
#power = []
#rectangle = create_rectangle(10, 10)
#line(copy.deepcopy(rectangle), power)
#while count < 4:
#	function(copy.deepcopy(rectangle), count, power)
#	count += 1

#function(copy.deepcopy(rectangle), 9, power)

##print(power)
##print(len(power))
