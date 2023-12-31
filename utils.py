#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# randylampa/AoC2023
#

import sys

def get_input_file(demo:int, day:int, year:int) -> str:
	syear = str(year)
	sday = str(day).rjust(2,'0')
	sdemo = '-demo{}-'.format(str(demo) if demo>0 else '')
	f = 'data{}{}-{}'.format(sdemo if demo>0 else '', syear, sday)
	return f

def get_output_file(demo:int, day:int, year:int) -> str:
	syear = str(year)
	sday = str(day).rjust(2,'0')
	sdemo = '-demo{}-'.format(str(demo) if demo>0 else '')
	f = 'outdata{}{}-{}'.format(sdemo if demo>0 else '', syear, sday)
	return f

def read_file_into_list(name = 'input', mapfnc = lambda x:x.strip()) -> list:
	"""
	Reads all lines into list and map mapfnc on each.
	"""
	f = open(name, 'r')
	lines = f.readlines()
	f.close()
	return [*map(mapfnc, lines)]

def read_file_into_list_bin(name = 'input', mapfnc = None) -> list:
	"""
	Reads all lines into list and map mapfnc on each.
	"""
	f = open(name, 'rb')
	lines = f.readlines()
	f.close()
	if mapfnc is not None:
		return [*map(mapfnc, lines)]
	else:
		return lines

def read_file_into_list_of_ints(name = 'input') -> list:
	"""
	Reads all lines into list and map int(x.strip()) on each.
	"""
	return read_file_into_list(name, lambda x: int(x.strip()))

def read_file_into_lists_of_ints(name = 'input', mapfnc = lambda x:x.strip())->list:
	"""
	Read
	"""
	return read_file_into_list(name, lambda x: [*map(int, x.strip().split(','))])

def print_answer(part:int, demo, answer) -> None:
	print("Answer_{} = {}{}".format(part, answer, ' (demo)' if demo else ''))
