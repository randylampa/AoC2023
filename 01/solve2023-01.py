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

	fn = utils.get_input_file(demo, DAY, YEAR)
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
	SOLVE PART 2
'''
def solve_part_2(demo:bool) -> str:
	fn = utils.get_input_file(demo, DAY, YEAR)
	print(fn)
	"""Do something here >>>"""

	"""<<< Do something here"""
	utils.print_answer(2, demo, answer)
	return answer

def main():

	solve_part_1(0)

	# ~ solve_part_2(1)

	pass

if __name__ == '__main__':
	sys.exit(main())
