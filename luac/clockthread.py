'''
TODO
@author: esterren
'''
import threading
import time


class ClockThread(threading.Thread):
    '''
    TODO classdocs
    '''

    def __init__(self, lock):
        '''
        Constructor
        '''
        threading.Thread.__init__(self)
        self.lock = lock
        # self.layout = ForcedSquareLayout()

    def run(self):
        while 1:
            self.lock.acquire()
            #self.layout.displayTime()
            print(time.strftime("%H:%M:%S",time.gmtime()))
            self.lock.release()
            time.sleep(1)
