'''
TODO
@author: esterren
'''
import threading
import time
from luac.appifc.displayabs import DisplayAbs

class UserInterruptThread(threading.Thread):
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
        self.t = 5

    def run(self):
        while True:
            uin = input()
            self.lock.acquire()
            # print("input: " + uin)
            # print("sleep " + str(self.t) + " sec.")
            time.sleep(self.t)
            self.lock.release()
