#u/usr/bin/env python
#-*- coding: utf-8 -*-
    
import sys
def main():

	for line in sys.stdin:	
		x = line.split(",")
		if len(x) < 5:
			del x
		else:
			sys.stdout.write(x[2] + '\t' + x[4])
	
if __name__ == "__main__":
    main()


