'''
Light Up Alarm Clock

TODO

@author: esterren
'''
import threading
import time
from luac.userinterruptthread import UserInterruptThread
from luac.clockthread import ClockThread
from luac.appifc.displayabs import DisplayAbs
from luac.sim.simdisplay import SimDisplay

if __name__ == '__main__':

    #     l = ForcedSquareLayout();
    lock = threading.Lock()
    display = SimDisplay()
    #threads = []

    while True:
        display.displayDateTime()
        time.sleep(0.5)
    # create Threads
    #t1 = ClockThread(lock, display)
    #t2 = UserInterruptThread(lock, display)

    # execute Threads
    #t1.start()
    #t2.start()

    #print("exiting main")