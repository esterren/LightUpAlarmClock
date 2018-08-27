'''
TODO
'''
import time
from luac.appifc.displayabs import DisplayAbs

class SimDisplay(DisplayAbs):
    def displayDateTime(self):
        print(time.strftime("%H:%M:%S", time.gmtime()))