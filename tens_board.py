# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 19:47:12 2020
for some reason empty file
and one more comment for testing branching on github
terveisia ketulle/ja minulle
@author: Anton ja Kettu
"""

import tensorflow as tf
from datetime import datetime

class GraphBoad:
    def __init__(self, logdir):
        now = datetime.now()
        self.logdir = logdir
        self.timestr = now.strftime("%Y%m%d-%H%M%S")
    
    def write_value()
