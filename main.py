#!/usr/bin/python
# Copyright 2017 Babakolo Usman Suleiman
# This program is distributed under the terms of the GNU
# General Public License (GPL).
"""
App main entry point
"""
import sys
sys.path.insert(0,'lib')
from View import *

print 'Starting program...'
## <----------------   START GUI -------------->
view = View("EEEN599-AI Optimization (BA)")
view.start()
