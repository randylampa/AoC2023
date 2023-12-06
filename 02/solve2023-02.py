#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# randylampa/AoC2023
# Advent of Code 2023 - 2
# @link https://adventofcode.com/2023/day/2

import sys
import os
cur_dir = os.path.dirname(os.path.realpath(__file__))
par_dir = os.path.dirname(cur_dir)
sys.path.append(par_dir)
import utils
import re

YEAR = 2023
DAY = 2
ISSUE = '02'


def parse_game_line(line:str)->dict:
	'''
	'''
	game = {
		'id': None,
		'red': 0,
		'green': 0,
		'blue': 0,
		'toss': [],
	}
	sgameid,sgametosses = line.split(':')
	game['id'] = int(re.sub(r'\D+', '', sgameid))
	gametosses = sgametosses.split(';')
	# ~ print(game['id'],gametosses)
	for toss in gametosses:
		gametoss = {
			'red': 0,
			'green': 0,
			'blue': 0,
		}
		for clr in gametoss.keys():
			# ~ mtch = re.findall(r'(?P<n>\d+) '+clr, toss)
			# ~ if len(mtch)>1:
				# ~ print('THIS TOSS IS FAULTY!!!', line, toss)
				# ~ exit()
			mtch = re.search(r'(?P<n>\d+) '+clr, toss)
			n = int(mtch.groupdict()['n']) if mtch else 0
			gametoss[clr] = n
			game[clr] = max(game[clr], n)
		game['toss'].append(gametoss)
	return game

def parse_game_line2(line:str)->dict:
	game = {
		'id': None,
		'red': 0,
		'green': 0,
		'blue': 0,
		'toss': [],
	}
	gametoss = {
		'red': 0,
		'green': 0,
		'blue': 0,
	}
	mtch = re.search(r'Game (?P<id>\d+):', line)
	game['id'] = int(mtch.groupdict()['id']) if mtch else 0

	for clr in gametoss.keys():
		mtch = [*map(int, re.findall(r'(?P<n>\d+) '+clr, line))]
		# ~ print(clr, mtch)
		game[clr] = max(mtch)

	return game

def print_game(game:dict):
	print('GameID', game['id'])
	print('  red', game['red'])
	print('  green', game['green'])
	print('  blue', game['blue'])
	print('tosses')
	for toss in game['toss']:
		print(' ', toss)

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

	possible_game = {
		'red': 12,
		'green': 13,
		'blue': 14,
	}

	impossibleIds = []

	for line in lines:
		# ~ print(line)
		# ~ game = parse_game_line(line)
		game = parse_game_line2(line)
		# ~ print_game(game)
		# ~ continue
		is_possible = True
		for k in possible_game.keys():
			if game[k] > possible_game[k]:
				is_possible = False
				impossibleIds.append(game['id'])
				print('Game {} is impossible because {} > {} {}'.format(game['id'], game[k], possible_game[k], k))
				# ~ print(line)
				# ~ print_game(game)
				# ~ exit()
				break
		# ~ print(is_possible)
	print('count:', len(impossibleIds))
	print('list:', impossibleIds)

	answer = sum(impossibleIds)

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
	# ~ demo is 7 instead of 8, but 3+4 EQUALS 7
	# ~ 3197 is too high

	# ~ solve_part_2(1)

	pass

if __name__ == '__main__':
	sys.exit(main())
