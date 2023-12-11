#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# randylampa/AoC2023
# Advent of Code 2023 - 5
# @link https://adventofcode.com/2023/day/5

import sys
import os
cur_dir = os.path.dirname(os.path.realpath(__file__))
par_dir = os.path.dirname(cur_dir)
sys.path.append(par_dir)
import utils
import re

YEAR = 2023
DAY = 5
ISSUE = '05'

mapPath = [
	'seed',
	'soil',
	'fert',
	'watr',
	'lght',
	'temp',
	'humi',
	'locn',
]

def parseInputData(filename:str)->dict:
	almanac = {
		'seeds': [],
		'seed2soil': [],
		'soil2fert': [],
		'fert2watr': [],
		'watr2lght': [],
		'lght2temp': [],
		'temp2humi': [],
		'humi2locn': [],
	}

	fh = open(filename, 'r')
	ssections = fh.read()
	# ~ print(ssections)
	asections = ssections.split('\n\n')
	# ~ print(asections)
	for ssec in asections:
		name, data = [*map(str.strip, ssec.split(':'))]
		# ~ print(name)
		# ~ print(data)
		mapSect = None
		if name=='seeds':
			almanac['seeds'] = [*map(int, data.split(' '))]
		elif name=='seed-to-soil map':
			mapSect = 'seed2soil'
		elif name=='soil-to-fertilizer map':
			mapSect = 'soil2fert'
		elif name=='fertilizer-to-water map':
			mapSect = 'fert2watr'
		elif name=='water-to-light map':
			mapSect = 'watr2lght'
		elif name=='light-to-temperature map':
			mapSect = 'lght2temp'
		elif name=='temperature-to-humidity map':
			mapSect = 'temp2humi'
		elif name=='humidity-to-location map':
			mapSect = 'humi2locn'
		if mapSect:
			# ~ map data into section
			# ~ print('parsing:', mapSect)
			lines = data.split('\n')
			for line in lines:
				dst,src,cnt = [*map(int, line.split(' '))]
				# ~ print(src,dst,cnt)
				xmap = {
					'srcMin': src,
					'srcMax': src + cnt-1,
					'dstMin': dst,
				}
				almanac[mapSect].append(xmap)
	return almanac

def dumpData(almanac:dict):
	for k in almanac.keys():
		print(k)
		print(almanac[k])
	# ~ print('seed2soil', seed2soil)
	# ~ print('soil2fert', soil2fert)
	# ~ print('fert2watr', fert2watr)
	# ~ print('watr2lght', watr2lght)
	# ~ print('lght2temp', lght2temp)
	# ~ print('temp2humi', temp2humi)
	# ~ print('humi2locn', humi2locn)

def applyMap(xmaps:list, src:int)->int:
	dst = src
	# ~ print('applyMap to src {}'.format(src))
	for xmap in xmaps:
		# ~ print(xmap)
		if src >= xmap['srcMin'] and src <= xmap['srcMax']:
			# ~ print('  src {} in {} - {}'.format(src, xmap['srcMin'], xmap['srcMax']))
			offset = src - xmap['srcMin']
			dst = xmap['dstMin'] + offset
			# ~ print('  has offset {} resulting in {}'.format(offset, dst))
			# ~ break
	# ~ print(' mapped to {}'.format(dst))
	return dst

def traverse_seed2location(almanac:dict, seed:int)->int:
	soil = applyMap(almanac['seed2soil'], seed)
	fert = applyMap(almanac['soil2fert'], soil)
	watr = applyMap(almanac['fert2watr'], fert)
	lght = applyMap(almanac['watr2lght'], watr)
	temp = applyMap(almanac['lght2temp'], lght)
	humi = applyMap(almanac['temp2humi'], temp)
	locn = applyMap(almanac['humi2locn'], humi)
	print('Seed {}, soil {}, fertilizer {}, water {}, light {}, temperature {}, humidity {}, location {}'.format(seed, soil, fert, watr, lght, temp, humi, locn))
	return locn

'''
	SOLVE PART 1
'''
def solve_part_1(demo:bool) -> str:

	fn = utils.get_input_file(1 if demo else 0, DAY, YEAR)
	print(fn)
	fl = cur_dir + '/' + fn
	"""Do something here >>>"""

	almanac = parseInputData(fn)
	# ~ dumpData(almanac)

	locations = []

	for seed in almanac['seeds']:
		loc = traverse_seed2location(almanac, seed)
		locations.append(loc)
	print('locations:', locations)

	answer = min(locations)

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
	# ~ Answer_1 = 35 (demo)

	# ~ solve_part_2(1)

	pass

if __name__ == '__main__':
	sys.exit(main())
