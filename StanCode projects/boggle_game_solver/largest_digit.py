"""
File: largest_digit.py
Name: Che-Hsien Chiu
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n: (int) number n for pick largest digit
	:return: (int) max digit
	"""
	# transfer to positive number then recursive
	if n >= 0:
		ans = helper(n, n%10)
	else:
		n = -n
		ans = helper(n, n%10)
	return ans


def helper(n, max_n):
	"""
	:param n: (int) number n for pick largest digit
	:param max_n: (int) largest digit
	:return: (int) largest digit
	"""
	# Base Case
	if n == 0:    # return largest digit
		return max_n

	# Recursive Case
	else:
		remainder = n % 10    # pick digit
		if remainder > max_n:
			return helper(n//10, remainder)    # replace largest digit then recurs
		else:
			return helper(n//10, max_n)


if __name__ == '__main__':
	main()
