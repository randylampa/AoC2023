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

	rgx = re.compile(r'[\d\.]')

	arePartnums = []
	notPartnums = []

	lineidx = 0
	lineidxMax = len(lines)
	for line in lines:
		# ~ print(line)
		for m in re.finditer(r'\d+', line):
			# ~ print(m)
			isPartnum = False
			sidx = int(m.start())
			eidx = int(m.end())
			lab = m.group()
			print('LINE {}: PARTNUM {} from {} to {}'.format(lineidx, lab, sidx, eidx))
			# ~ print(line[sidx])
			# ~ print(line[eidx])
			idxL = sidx-1 if sidx>0 else None
			idxR = eidx if eidx<len(line) else None
			print('  idxL:{}, idxR:{}'.format(idxL,idxR))
			if idxL and line[idxL]!='.':
				print('  has SYMBOL`{}` on the left'.format(line[idxL]))
				isPartnum = True
				# ~ continue
			if idxR and line[idxR]!='.':
				print('  has SYMBOL`{}` on the right'.format(line[idxR]))
				isPartnum = True
				# ~ continue
			idxL = idxL if idxL is not None else sidx
			idxR = idxR if idxR is not None else eidx
			if lineidx>0:
				# ~ has prev line
				strip = lines[lineidx-1][idxL:idxR+1]
				print(' strip Top', strip)
				symbols = rgx.sub('', strip)
				if len(symbols)>0:
					print('  has SYMBOL`{}` on top'.format(symbols))
					isPartnum = True
					# ~ continue
			if lineidx<lineidxMax-1:
				# ~ has next line
				strip = lines[lineidx+1][idxL:idxR+1]
				print(' strip Bottom', strip)
				symbols = rgx.sub('', strip)
				if len(symbols)>0:
					print('  has SYMBOL`{}` on bottom'.format(symbols))
					isPartnum = True
					# ~ continue
				pass
			pn = int(lab)
			if isPartnum:
				arePartnums.append(pn)
			else:
				notPartnums.append(pn)

		lineidx = lineidx+1

	print('arePartnums', arePartnums)
	print('notPartnums', notPartnums)

	answer = sum(arePartnums)

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
	# ~ Answer_1 = 4361 (demo)
	# ~ Answer_1 = 543867 is right

	# ~ solve_part_2(1)

	pass

if __name__ == '__main__':
	sys.exit(main())
