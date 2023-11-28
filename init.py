#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# randylampa/AoC2023
#

import sys
import getopt

YEAR = 2023

def main():
	try:
		options, arguments = getopt.getopt(sys.argv[1:], "y:d:p:", ["year =", "day =", "part ="])
	except:
		print("Error parsing args")
		return -1
	print(options, arguments)

	year = YEAR
	day = None
	part = 1

	for opt, arg in options:
		if opt in ('-y', '--year'):
			year = arg
		elif opt in ('-d', '--day'):
			day = int(arg)
		elif opt in ('-p', '--part'):
			part = int(arg)

	if len(arguments)>0:
		day = int(arguments[0])

	if day is None:
		print('Day not set!')
		return -2

	issue = str(day).rjust(2, '0')

	url = "https://adventofcode.com/{}/day/{}".format(year, day)
	url_input = "{}/input".format(url)
	url_answer = "{}/answer".format(url)

	trtable = {
		'$YEAR':year,
		'$DAY':day,
		'$ISSUE':issue,
		'$URL':url,
		'$URL_INPUT':url_input,
		'$URL_ANSWER':url,
	}

	print(trtable)

	'''
	TODO
	get all files from dir `_tpl`. copy them into dir `$ISSUE`
	rename & modify according to `trtable`
	'''

	return 0

if __name__ == '__main__':
	sys.exit(main())
