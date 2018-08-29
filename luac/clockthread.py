'''
TODO
@author: esterren
'''
import threading
import time
from luac.appifc.displayabs import DisplayAbs

class ClockThread(threading.Thread):
    '''
    TODO classdocs
    '''

    def __init__(self, lock, display:DisplayAbs):
        '''
        Constructor
        '''
        threading.Thread.__init__(self)
        self._lock = lock
        self._display = display
        # self.layout = ForcedSquareLayout()

    def run(self):
        while True:
            self._lock.acquire()
            self._display.displayDateTime()
            #self.layout.displayTime()
            #print(time.strftime("%H:%M:%S",time.gmtime()))
            self._lock.release()
            time.sleep(1)
