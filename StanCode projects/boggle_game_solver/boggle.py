"""
File: boggle.py
Name: Che-Hsien, Chiu
----------------------------------------
TODO: find words in boggle game from user input
"""

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'
dict_list = []

class Node:
	def __init__(self, key):
		self.key = key
		self.next = None
		self.location = 0


class List:
	def __init__(self):
		self.head = None
		self.tail = None
		self.size = 0

	def enqueue(self, key, location):
		"""
		:param key: (char) char of node
		:param location: (int) location in boggle
		"""
		new_node = Node(key)
		if self.size == 0:    # empty list, enqueue directly
			self.head = self.tail = new_node
		else:    # non-empty list, enqueue at tail
			self.tail.next = new_node
			self.tail = new_node
		new_node.location = location    # update location of node
		self.size += 1


class Boggle:
	def __init__(self, n):
		self.size = n**2    # boggle size
		self.lst = []    # linked list in each location
		self.visit = []    # have visited list
		self.word_list = []    # list of word found in dictionary
		for i in range(self.size):    # initial linked list and visited list
			self.lst.append(List())    # all empty at each location
			self.visit.append(False)    # all have not visited

	def show(self):
		for i in range(self.size):
			temp = self.lst[i].head
			while temp is not None:
				print(f'{temp.key}  ', end='')
				print(self.visit[i])
				temp = temp.next
			print()

	def set_lst(self, row_list, n):
		"""
		connect each element in boggle
		row1 -->  0   1   2   3
		row2 -->  4   5   6   7
		row3 -->  8   9  10  11
		row4 --> 12  13  14  15
		"""
		for i in range(self.size):
			# upper left corner, location 0
			if i == 0:
				self.lst[i].enqueue(row_list[i+1], i+1)    # connect right node
				self.lst[i].enqueue(row_list[i+n+1], i+n+1)    # connect lower right node
				self.lst[i].enqueue(row_list[i+n], i+n)    # connect lower node
			# lower left corner, location 12
			elif i == n*(n-1):
				self.lst[i].enqueue(row_list[i-n], i-n)    # connect upper node
				self.lst[i].enqueue(row_list[i-n+1], i-n+1)    # connect upper right node
				self.lst[i].enqueue(row_list[i+1], i+1)    # connect right node
			# upper right corner, location 3
			elif i == n-1:
				self.lst[i].enqueue(row_list[i-1], i-1)    # connect left node
				self.lst[i].enqueue(row_list[i+n-1], i+n-1)    # connect lower left node
				self.lst[i].enqueue(row_list[i+n], i+n)     # connect lower node
			# lower right corner, location 15
			elif i == n**2 - 1:
				self.lst[i].enqueue(row_list[i-n], i-n)  # connect upper node
				self.lst[i].enqueue(row_list[i-n-1], i-n-1)  # connect upper left node
				self.lst[i].enqueue(row_list[i-1], i-1)  # connect left node
			# upper line, location 1, 2
			elif 0 < i < n-1:
				self.lst[i].enqueue(row_list[i-1], i-1)  # connect left node
				self.lst[i].enqueue(row_list[i+n-1], i+n-1)  # connect lower left node
				self.lst[i].enqueue(row_list[i+n], i+n)  # connect lower node
				self.lst[i].enqueue(row_list[i+n+1], i+n+1)  # connect lower right node
				self.lst[i].enqueue(row_list[i+1], i+1)  # connect right node
			# left line, location 4, 8
			elif i%n == 0:
				self.lst[i].enqueue(row_list[i-n], i-n)  # connect upper node
				self.lst[i].enqueue(row_list[i-n+1], i-n+1)  # connect upper right node
				self.lst[i].enqueue(row_list[i+1], i+1)  # connect right node
				self.lst[i].enqueue(row_list[i+n+1], i+n+1)  # connect lower right node
				self.lst[i].enqueue(row_list[i+n], i+n)  # connect lower node
			# right line, location 7, 11
			elif i%n == n-1:
				self.lst[i].enqueue(row_list[i-n], i-n)  # connect upper node
				self.lst[i].enqueue(row_list[i-n-1], i-n-1)  # connect upper left node
				self.lst[i].enqueue(row_list[i-1], i-1)  # connect left node
				self.lst[i].enqueue(row_list[i+n-1], i+n-1)  # connect lower left node
				self.lst[i].enqueue(row_list[i+n], i+n)  # connect lower node
			# lower line, location 13, 14
			elif n*(n-1) < i < n*n:
				self.lst[i].enqueue(row_list[i-1], i-1)  # connect left node
				self.lst[i].enqueue(row_list[i-n-1], i-n-1)  # connect upper left node
				self.lst[i].enqueue(row_list[i-n], i-n)  # connect upper node
				self.lst[i].enqueue(row_list[i-n+1], i-n+1)  # connect upper right node
				self.lst[i].enqueue(row_list[i+1], i+1)  # connect right node
			# others with 8 neighbor
			else:
				self.lst[i].enqueue(row_list[i-1], i-1)  # connect left node
				self.lst[i].enqueue(row_list[i-n-1], i-n-1)  # connect upper left node
				self.lst[i].enqueue(row_list[i-n], i-n)  # connect upper node
				self.lst[i].enqueue(row_list[i-n+1], i-n+1)  # connect upper right node
				self.lst[i].enqueue(row_list[i+1], i+1)  # connect right node
				self.lst[i].enqueue(row_list[i+n+1], i+n+1)  # connect lower right node
				self.lst[i].enqueue(row_list[i+n], i+n)  # connect lower node
				self.lst[i].enqueue(row_list[i+n-1], i+n-1)  # connect lower left node

	def dfs(self, r, ch, row_list):
		"""
		:param r: (int) starting location
		:param ch: (char) char in the location
		:param row_list:  (list) char list from user input
		"""
		if self.has_prefix(ch):
			# length of word in dictionary > 4 and haven't been found, add to boggle word list and print word
			if len(ch) >= 4 and ch in dict_list and ch not in self.word_list:
				self.word_list.append(ch)
				print(f'Found \"{ch}\"')

			self.visit[r] = True    # set location visited
			temp = self.lst[r].head     # choose

			while temp is not None:    # explore all neighbor node, stop when all have visited
				# check if have visited
				if self.visit[temp.location] is False:    # have not visited, explore
					self.dfs(temp.location, ch + temp.key, row_list)
					self.visit[temp.location] = False    # un-choose
					temp = temp.next    # update temp to next node
				else:    # have visited, next neighbor node
					temp = temp.next    # update temp to next node

	def reset_boggle(self):
		"""
		reset visited condition for next location dfs used
		"""
		for i in range(self.size):
			self.visit[i] = False

	def get_word_count(self):
		"""
		get number of words count
		"""
		return len(self.word_list)

	@staticmethod
	def has_prefix(sub_s):
		"""
		:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
		:return: (bool) If there is any words with prefix stored in sub_s
		"""
		global dict_list
		for i in dict_list:
			if i.startswith(sub_s):
				return True
		return False

	@staticmethod
	def read_dictionary(file):
		"""
		:param file: (string) file name
		"""
		global dict_list
		with open(file, 'r') as f:
			for line in f:
				dict_list.append(line.split('\n')[0])  # remove '\n'


def main():
	"""
	find all word in boggle
	"""
	boggle = Boggle(4)
	boggle.read_dictionary(FILE)
	row_list = []
	# user input, and create row list
	for i in range(4):
		row = input(f'{i+1} row of letters: ')
		if is_legal_input(row):
			for char in row.split():
				row_list.append(char.lower())    # case insensitive

	boggle.set_lst(row_list, 4)

	# dfs in each location
	for i in range(boggle.size):
		boggle.dfs(i, row_list[i], row_list)
		boggle.reset_boggle()
	print(f'There are {boggle.get_word_count()} words in total.')


def is_legal_input(row):
	"""
	:param row: (string) input string from user
	:return: (boolean) if legal input
	"""
	# check if over 4 char
	if len(row.split()) != 4:
		print('Illegal input')
		return False
	# check if each element only one character
	else:
		for char in row.split():
			if len(char) != 1:
				print('Illegal input')
				return False
		return True


if __name__ == '__main__':
	main()
