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

def split_list(lst:list, chunk_size:int)->list:
	'''
	https://www.altcademy.com/blog/how-to-split-a-list-in-python/
	'''
	return list(zip(*[iter(lst)] * chunk_size))

def parseInputData(filename:str)->dict:
	almanac = {
		'seeds': [],
		'seeds2': [],
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
			# ~ now for part 2 ..
			almanac['seeds2'] = split_list(almanac['seeds'], 2)
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

def traverse_seed2location(almanac:dict, seed:int, printMsg:bool=True)->int:
	soil = applyMap(almanac['seed2soil'], seed)
	fert = applyMap(almanac['soil2fert'], soil)
	watr = applyMap(almanac['fert2watr'], fert)
	lght = applyMap(almanac['watr2lght'], watr)
	temp = applyMap(almanac['lght2temp'], lght)
	humi = applyMap(almanac['temp2humi'], temp)
	locn = applyMap(almanac['humi2locn'], humi)
	if printMsg:
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
	PART 2
'''


def createInterval(count:int, inBase:int, outBase:int = None)->dict:
	return {
		'count': count,
		'inBase': inBase,
		'outBase': outBase,
	}

def interval2str(interval:dict)->str:
	if interval['outBase']:
		return "([{}->{}]+{})".format(interval['inBase'], interval['outBase'], interval['count'])
	else:
		return "({}+{})".format(interval['inBase'], interval['count'])

def dumpInterval(interval:dict, prepend:str = None):
	if prepend:
		print(prepend, interval2str(interval))
	else:
		print(interval2str(interval))

def dumpIntervals(intervals:list, prepend:str = None):
	if prepend: print(prepend)
	for interval in intervals: dumpInterval(interval, '  ')

def splitInterval(interval:dict, targetIntervals:list)->list:
	'''
	'''
	intervals = []
	for tInt in targetIntervals:
		tIntBeg = tInt['inBase'];
		tIntEnd = tInt['inBase'] + tInt['count']
		sIntBeg = interval['inBase']
		sIntEnd = interval['inBase'] + interval['count']

		if sIntBeg >= tIntBeg and sIntBeg < tIntEnd:
			print('begin of interval', interval2str(interval), 'matches into', interval2str(tInt))
			if sIntEnd <= tIntEnd:
				print('end of interval', interval2str(interval), 'matches into', interval2str(tInt))
				intervals.append(interval)
				interval = None
				break # matches completely, leave it alone and break
			else:
				print({sIntBeg, sIntEnd, tIntBeg, tIntEnd})
				print('!!! end of interval', interval2str(interval), 'does not matches into', interval2str(tInt))
				lenMatch = tIntEnd - sIntBeg
				intervalMatch = createInterval(lenMatch, sIntBeg)
				intervalOver = createInterval(interval['count']-lenMatch, tIntEnd)
				# ~ dumpInterval(intervalMatch, 'intervalMatch')
				# ~ dumpInterval(intervalOver, 'intervalOver')
				intervals.append(intervalMatch)
				interval = None
				# call splitInterval(intervalOver, targetIntervals) and merge with current list of intervals
				xints = splitInterval(intervalOver, targetIntervals)
				dumpIntervals(xints, 'intervalOver')
				intervals = intervals+xints
				break
		pass
	if interval is not None:
		# does not match anywhere, leave it as, is
		intervals.append(interval)
	return intervals

def translateInterval(interval:dict, targetIntervals:list)->list:
	'''
	interval should not be overlapping, run trough splitInterval(..)
	'''
	for tInt in targetIntervals:
		tIntBeg = tInt['inBase'];
		tIntEnd = tInt['inBase'] + tInt['count']
		sIntBeg = interval['inBase']
		sIntEnd = interval['inBase'] + interval['count']
		if sIntBeg >= tIntBeg and sIntEnd <= tIntEnd:
			# match into, translate
			sNewStart = tInt['outBase'] + (sIntBeg - tIntBeg)
			return createInterval(interval['count'], sNewStart)
	return createInterval(interval['count'], interval['inBase']) # pro jistotu nový objekt

def translateIntervals(intervals:list, targetIntervals:list)->list:
	'''
	intervals should be output from splitInterval(..) to ensure no overlapping
	'''
	tIntervals = []
	for interval in intervals:
		tInterval = translateInterval(interval, targetIntervals)
		tIntervals.append(tInterval)
	return tIntervals

def parseInputDataIntervals(filename:str)->dict:
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
			seeds = [*map(int, data.split(' '))]
			# ~ now for part 2 ..
			almanac['seeds'] = [*map(lambda x:createInterval(x[1], x[0]), split_list(seeds, 2))]
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
				xmap = createInterval(cnt, src, dst)
				almanac[mapSect].append(xmap)
	return almanac


'''
	SOLVE PART 2
'''
def solve_part_2(demo:bool) -> str:

	fn = utils.get_input_file(1 if demo else 0, DAY, YEAR)
	print(fn)
	fl = cur_dir + '/' + fn
	"""Do something here >>>"""

	'''
	To solve it effectively, do not loop trough numbers, use intervals.
	Take interval and try to match it on MAP. If only part of interval matches, split it and call recursively..
	Traverse to the bottom
	'''

	almanac = parseInputDataIntervals(fn)
	dumpData(almanac)
	# ~ return None

	locations = []

	if 0: # begin

		for seedMin,seedCount in almanac['seeds2']:
			# ~ loc = traverse_seed2location(almanac, seed)
			# ~ locations.append(loc)
			# ~ print(seedMin,seedCount)
			seedlocs = []
			for offset in range(seedCount):
				seed = seedMin + offset
				loc = traverse_seed2location(almanac, seed, False)
				print('seed {} in loc {}'.format(seed,loc))
				seedlocs.append(loc)
			locations.append(min(seedlocs))

		# ~ print('locations:', locations)
		pass # end

	seedIntervals = almanac['seeds']
	seedIntervalsSplit = []

	soilIntervals = []
	soilIntervalsSplit = []

	fertIntervals = []

	watrIntervals = []

	lghtIntervals = []

	tempIntervals = []

	humiIntervals = []

	print('===seedIntervals===')
	for seedInterval in seedIntervals:
		dumpInterval(seedInterval, 'seedInterval')
		xint = splitInterval(seedInterval, almanac['seed2soil'])
		dumpIntervals(xint, 'xint')
		seedIntervalsSplit = seedIntervalsSplit + xint
		print('---/seedInterval---')
	print('seedIntervals', len(seedIntervals), '-> seedIntervalsSplit', len(seedIntervalsSplit))
	dumpIntervals(seedIntervalsSplit, 'seedIntervalsSplit')

	soilIntervals = translateIntervals(seedIntervalsSplit, almanac['seed2soil'])
	dumpIntervals(soilIntervals, 'soilIntervals')

	print('===soilIntervals===')
	for soilInterval in soilIntervals:
		soilIntervalsSplit = soilIntervalsSplit + splitInterval(soilInterval, almanac['soil2fert'])
		# ~ print('---/soilInterval---')
	print('soilInterval', len(soilInterval), '-> soilIntervalsSplit', len(soilIntervalsSplit))
	dumpIntervals(soilIntervalsSplit, 'soilIntervalsSplit')

	fertIntervals = translateIntervals(soilIntervalsSplit, almanac['soil2fert'])
	dumpIntervals(fertIntervals, 'fertIntervals')

	answer = min(locations) if len(locations)>0 else None

	"""<<< Do something here"""
	utils.print_answer(2, demo, answer)
	return answer

def main():

	# ~ solve_part_1(0)
	# ~ Answer_1 = 35 (demo)
	# ~ Answer_1 = 806029445 is right

	solve_part_2(0)
	# ~ Answer_2 = 46 (demo)
	# ~ non-demo answer is too slow. didn't wait


	pass

if __name__ == '__main__':
	sys.exit(main())
