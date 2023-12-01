#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# randylampa/AoC2023
# Advent of Code 2023 - 1
# @link https://adventofcode.com/2023/day/1

import sys
import re
sys.path.append('..')
import utils

YEAR = 2023
DAY = 1
ISSUE = '01'



'''
	SOLVE PART 1
'''
def solve_part_1(demo:bool) -> str:

	fn = utils.get_input_file(1 if demo else 0, DAY, YEAR)
	print(fn)
	"""Do something here >>>"""

	lines = utils.read_file_into_list(fn)

	numbers = []
	for line in lines:
		line = re.sub(r'\D', '', line)
		nums = line[0]+line[-1]
		# ~ print(line, nums, int(nums))
		numbers.append(int(nums))

	answer = sum(numbers)

	"""<<< Do something here"""
	utils.print_answer(1, demo, answer)
	return answer

'''
	SOLVE PART 1b
'''
def solve_part_1b(demo:bool) -> str:

	fn = utils.get_input_file(1 if demo else 0, DAY, YEAR)
	print(fn)
	"""Do something here >>>"""

	lines = utils.read_file_into_list(fn)

	numbers = []
	for line in lines:
		nums = ''
		for char in line:
			if char >= '0' and char <= '9':
				nums = nums+char
				break
		rline = list(line)
		rline.reverse()
		for char in rline:
			if char >= '0' and char <= '9':
				nums = nums+char
				break
		# ~ print(line, nums, int(nums))
		numbers.append(int(nums))

	answer = sum(numbers)

	"""<<< Do something here"""
	utils.print_answer(1, demo, answer)
	return answer

strigits = [
	'zero',
	'one',
	'two',
	'three',
	'four',
	'five',
	'six',
	'seven',
	'eight',
	'nine',
]

def transNums(instr:str)->str:
	'''
	naive, replace in order 0,1,2...
	'''
	for digit in strigits:
		index = strigits.index(digit)
		# ~ print(digit, index)
		instr = instr.replace(digit, str(index))
	return instr

def transNums2(instr:str)->str:
	'''
	replaces in order of find
	'''
	finds = {}
	for digit in strigits:
		index = strigits.index(digit)
		pos = None
		try:
			pos = instr.index(digit)
		except ValueError:
			pass
		if pos is not None:
			finds[pos] = digit
		print(digit, index, pos, finds)
	ks = list(finds.keys())
	ks.sort()
	for i in ks:
		digit = finds[i]
		index = strigits.index(digit)
		print(digit, index)
		instr = instr.replace(digit, str(index))
	return instr

'''
	SOLVE PART 2
'''
def solve_part_2(demo:bool) -> str:

	# ~ line = 'xtwone3four'
	# ~ print(transNums2(line))
	# ~ return ''

	fn = utils.get_input_file(2 if demo else 0, DAY, YEAR)
	print(fn)
	"""Do something here >>>"""

	lines = utils.read_file_into_list(fn)

	numbers = []
	for line0 in lines:
		line = transNums(line0)
		line = re.sub(r'\D', '', line)
		nums = line[0]+line[-1]
		# ~ print(line0, line, nums, int(nums))
		numbers.append(int(nums))

	answer = sum(numbers)

	"""<<< Do something here"""
	utils.print_answer(2, demo, answer)
	return answer

def main():

	# ~ solve_part_1(0)
	# ~ 54597 - is right
	solve_part_1b(0)
	# ~ 54597 - is right

	# ~ solve_part_2(0)
	# ~ 54039 - too low
	# ~ 54513 - too high

	pass

if __name__ == '__main__':
	sys.exit(main())
