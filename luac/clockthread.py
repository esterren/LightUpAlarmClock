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
        self.lock = lock
        self.display = display
        # self.layout = ForcedSquareLayout()

    def run(self):
        while 1:
            self.lock.acquire()
            self.display.displayDateTime()
            #self.layout.displayTime()
            #print(time.strftime("%H:%M:%S",time.gmtime()))
            self.lock.release()
            time.sleep(1)
