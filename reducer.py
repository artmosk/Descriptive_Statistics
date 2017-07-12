#!/usr/bin/env python
#-*- coding: utf-8 -*-

import sys


def main():

	cash_key = 0
	cnt = 0
	for line in sys.stdin:
		key, value = line.split('\t')
		value = int(value)
		if cash_key == 0:
			cash_key = key
			cash_value = value
		elif cash_key == key:
			cash_value += value
		else:
			sys.stdout.write(cash_key + '\t' + str(cash_value)+'\n')
			cash_key = key
			cash_value = value
	sys.stdout.write(cash_key + '\t' + str(cash_value)+'\n')

if __name__ == "__main__":
     main()
