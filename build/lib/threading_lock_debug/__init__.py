#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 zenbook <zenbook@zenbook-XPS>
#
# Distributed under terms of the MIT license.

"""

"""

import threading
import traceback
import logging

class Lock(object):
    def __init__(self):
        self.lock = threading.Lock()
        trace = traceback.extract_stack()
        logging.debug("Create Lock from:%s"%(trace[-2], ))
        self.lock_created_trace = trace[-2]
    
    def __enter__(self, *args, **kwargs):
        trace = traceback.extract_stack()
        logging.debug("Entering Lock from:%s created:%s"%(trace[-2], self.lock_created_trace))
        self.lock.acquire()
        logging.debug("Entered Lock from:%s created:%s"%(trace[-2], self.lock_created_trace))
        
    def __exit__(self, *args, **kwargs):
        trace = traceback.extract_stack()
        logging.debug("Exiting Lock from:%s created:%s"%(trace[-2], self.lock_created_trace))
        self.lock.release()
        
