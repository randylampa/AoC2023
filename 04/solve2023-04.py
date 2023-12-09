#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# randylampa/AoC2023
# Advent of Code 2023 - 4
# @link https://adventofcode.com/2023/day/4

import sys
import os
cur_dir = os.path.dirname(os.path.realpath(__file__))
par_dir = os.path.dirname(cur_dir)
sys.path.append(par_dir)
import utils
import re

YEAR = 2023
DAY = 4
ISSUE = '04'


def parse_card(line:str)->dict:
	name, snumsAll = line.split(':')

	snwin, snums = snumsAll.split('|')

	numsWin = [*map(int, re.findall(r'\d+', snwin))]
	nums = [*map(int, re.findall(r'\d+', snums))]

	return {
		'name': name,
		'numsWin': numsWin,
		'nums': nums
	}


'''
	SOLVE PART 1
'''
def solve_part_1(demo:bool) -> str:

	fn = utils.get_input_file(1 if demo else 0, DAY, YEAR)
	print(fn)
	fl = cur_dir + '/' + fn
	"""Do something here >>>"""

	lines = utils.read_file_into_list(fl)
	# ~ print(lines)

	cards_values = []

	for line in lines:
		card = parse_card(line)
		# ~ print(card)
		value = None
		for n in card['nums']:
			try :
				card['numsWin'].index(n)
				value = value*2 if value is not None else 1
			except ValueError:
				# ~ print('number {} is not in winning'.format(n))
				pass
		if value is not None:
			cards_values.append(value)

	answer = sum(cards_values)

	"""<<< Do something here"""
	utils.print_answer(1, demo, answer)
	return answer


'''
	SOLVE PART 2
'''
def solve_part_2(demo:bool) -> str:

	fn = utils.get_input_file(1 if demo else 0, DAY, YEAR)
	print(fn)
	fl = cur_dir + '/' + fn
	"""Do something here >>>"""

	answer = None

	"""<<< Do something here"""
	utils.print_answer(2, demo, answer)
	return answer

def main():

	solve_part_1(0)
	# ~ Answer_1 = 13 (demo)
	# ~ Answer_1 = 22193 is right

	# ~ solve_part_2(1)

	pass

if __name__ == '__main__':
	sys.exit(main())
