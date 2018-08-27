'''
TODO
'''
import time
from luac.appifc.displayabs import DisplayAbs
from asciimatics.screen import Screen

class SimDisplay(DisplayAbs):
    def __init__(self):
        self.screen = Screen.open(200, False, 'UTF-8')

    def __del__(self):
        self.screen.close()

    def displayDateTime(self):
        self.screen.print_at(time.strftime("%H:%M:%S", time.gmtime()),0,0)
        self.screen.refresh()
        #print(time.strftime("%H:%M:%S", time.gmtime()))