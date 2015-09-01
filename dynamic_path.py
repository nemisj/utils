#!/usr/bin/env python

# This file will generate new PATH variable based on the given path and taking
# into the account old PATH variable. Also will it remove all the old values
# from the PATH.

import os
import sys
import re

old_path=os.getenv("PATH")

if len(sys.argv) == 1:
	print old_path
	sys.exit(1)

bin_folder = os.path.abspath(sys.argv[1])

paths = [ bin_folder ]


def clean_path(path):
	cleaned = []
	for name in path.split(':'):
		if not re.search(bin_folder, name):
			cleaned.append(name)
	
	return cleaned

cleaned = clean_path(old_path)

for name in os.listdir(bin_folder): 

	full_path = os.path.join(bin_folder, name)
	if os.path.isdir(full_path):
		paths.append(full_path)	

if (len(sys.argv) == 3) and (sys.argv[2] == "clean"):
	# this might be clean
	print ':'.join(cleaned)
else:
	print ':'.join(paths + cleaned)
