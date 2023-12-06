#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# randylampa/AoC2023
# Advent of Code 2023 - 3
# @link https://adventofcode.com/2023/day/3

import sys
import os
cur_dir = os.path.dirname(os.path.realpath(__file__))
par_dir = os.path.dirname(cur_dir)
sys.path.append(par_dir)
import utils
import re

YEAR = 2023
DAY = 3
ISSUE = '03'



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

	lineidx = 0
	for line in lines:
		# ~ print(line)
		for m in re.finditer(r'\d+', line):
			# ~ print(m)
			sidx = int(m.start())
			eidx = int(m.end())
			lab = m.group()
			print('LINE {}: PARTNUM {} from {} to {}'.format(lineidx, lab, sidx, eidx))

		lineidx = lineidx+1

	answer = None

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

	solve_part_1(1)

	# ~ solve_part_2(1)

	pass

if __name__ == '__main__':
	sys.exit(main())
