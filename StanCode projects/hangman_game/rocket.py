"""
File: rocket.py
Name: Che-Hsien, Chiu
-----------------------
This program should implement a console program
that draws ASCII art - a rocket.
The size of rocket is determined by a constant
defined as SIZE at top of the file.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

SIZE = 10


def main():
	"""
	Create a rocket.
	"""
	head()
	belt()
	upper()
	lower()
	belt()
	head()


def head():
	"""
	create head part of the rocket
	"""
	for i in range(SIZE):    # row
		for j in range(2*(SIZE+1)):    # column

			# left part
			if j <= SIZE:
				if i+j >= SIZE:
					print('/',end='')
				else:
					print(' ',end='')

			# right part
			else:
				if j <= (i+SIZE+1):
					print ('\\',end='')
				else:
					print(' ',end='')
		print('')



def belt():
	"""
	create belt part of the rocket.
	"""
	print('+',end='')
	for i in range(2*SIZE):
		print('=',end='')
	print('+')


def upper():
	"""
	create upper part of the rocket body.
	"""

	# SIZE is odd
	if SIZE%2 == 1:
		for i in range(SIZE):    # row
			print('|',end='')
			for j in range(1,2*(SIZE)+1):    # column

				# left part
				if j <= SIZE:
					if i+j >= SIZE:
						if (i+j)%2 == 0:
							print('\\',end='')
						else:
							print('/',end='')
					else:
						print('.',end='')

				# right part
				else:
					if j <= (i+SIZE+1):
						if (i+j)%2 == 0:
							print('\\',end='')
						else:
							print('/',end='')
					else:
						print('.',end='')
			print('|')

	# SIZE is even
	else:
		for i in range(SIZE):  # row
			print('|', end='')
			for j in range(1, 2 * (SIZE) + 1):  # column
				# left part
				if j <= SIZE:
					if i + j >= SIZE:
						if (i + j) % 2 == 0:
							print('/', end='')
						else:
							print('\\', end='')
					else:
						print('.', end='')

				# right part
				else:
					if j <= (i + SIZE + 1):
						if (i + j) % 2 == 0:
							print('/', end='')
						else:
							print('\\', end='')
					else:
						print('.', end='')
			print('|')


def lower():
	"""
	create lower part of the rocket body.
	"""
	for i in range(SIZE):    # row
		print('|',end='')
		for j in range(1,2*(SIZE)+1):    # column

			# left part
			if j <= SIZE:
				if j-i > 0:
					if (i+j)%2 == 0:
						print('/',end='')
					else:
						print('\\',end='')
				else:
					print('.',end='')

			# right part
			else:
				if j+i <= 2*SIZE:
					if (i+j)%2 == 0:
						print('/',end='')
					else:
						print('\\',end='')
				else:
					print('.',end='')
		print('|')



###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()