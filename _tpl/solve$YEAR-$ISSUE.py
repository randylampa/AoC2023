#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# randylampa/AoC$YEAR
# Advent of Code $YEAR - $DAY
# @link $URL

import sys
import re
sys.path.append('..')
import utils

YEAR = $YEAR
DAY = $DAY
ISSUE = '$ISSUE'



'''
	SOLVE PART 1
'''
def solve_part_1(demo:bool) -> str:

	fn = utils.get_input_file(1 if demo else 0, DAY, YEAR)
	print(fn)
	"""Do something here >>>"""

	"""<<< Do something here"""
	utils.print_answer(1, demo, answer)
	return answer


'''
	SOLVE PART 2
'''
def solve_part_2(demo:bool) -> str:

	fn = utils.get_input_file(1 if demo else 0, DAY, YEAR)
	print(fn)
	"""Do something here >>>"""

	"""<<< Do something here"""
	utils.print_answer(2, demo, answer)
	return answer

def main():

	solve_part_1(1)

	solve_part_2(1)

	pass

if __name__ == '__main__':
	sys.exit(main())
