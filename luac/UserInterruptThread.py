'''
TODO
@author: esterren
'''
import threading
import time

class UserInterruptThread(threading.Thread):
    '''
    TODO classdocs
    '''

    def __init__(self, lock):
        '''
        Constructor
        '''
        threading.Thread.__init__(self)
        self.lock = lock
        self.t = 5

    def run(self):
        while 1:
            uin = input()
            self.lock.acquire()
            print("input: " + uin)
            print("sleep " + str(self.t) + " sec.")
            time.sleep(self.t)
            self.lock.release()
