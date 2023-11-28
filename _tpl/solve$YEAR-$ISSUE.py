#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# randylampa/AoC$YEAR
# Advent of Code $YEAR - $DAY

import sys
import re
sys.path.append('..')
import utils

YEAR = $YEAR
DAY = $DAY
ISSUE = $ISSUE



'''
	SOLVE PART 1
'''
def solve_part_1(demo:bool) -> str:

	fn = utils.get_input_file(demo, ISSUE, True)
	print(fn)
	"""Do something here >>>"""

	"""<<< Do something here"""
	utils.print_answer(1, demo, answer)
	return answer


'''
	SOLVE PART 2
'''
def solve_part_2(demo:bool) -> str:
	fn = utils.get_input_file(demo, ISSUE, True)
	print(fn)
	"""Do something here >>>"""

	"""<<< Do something here"""
	utils.print_answer(2, demo, answer)
	return answer

def main(args):

	solve_part_1(1)

	solve_part_2(1)

	pass

if __name__ == '__main__':
	sys.exit(main())
