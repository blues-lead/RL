# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 19:47:12 2020
for some reason empty file
@author: Anton
"""

import tensorflow as tf
from datetime import datetime

class GraphBoad:
    def __init__(self, logdir):
        now = datetime.now()
        self.logdir = logdir
        self.timestr = now.strftime("%Y%m%d-%H%M%S")
    
    def write_value()