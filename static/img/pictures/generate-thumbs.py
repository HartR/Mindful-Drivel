#!/usr/bin/env python
#makes a small thumbnail for all pictures in current directory 
import os
import subprocess

for filename in os.listdir(os.getcwd()):
	minusExtension, extension = os.path.splitext(filename)
	if extension.lower() == '.jpg':
		subprocess.call(["convert", filename, "-resize", "300x300", minusExtension + "-thumb" + extension])
