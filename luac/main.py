'''
Light Up Alarm Clock

TODO

@author: esterren
'''
import threading

from luac.userinterruptthread import UserInterruptThread
from luac.clockthread import ClockThread
from luac.appifc.displayabs import DisplayAbs
from luac.sim.simdisplay import SimDisplay

if __name__ == '__main__':
    #     l = ForcedSquareLayout();
    #     print(l.displayTime())
    lock = threading.Lock()
    display = SimDisplay()
    threads = []

    # create Threads
    t1 = ClockThread(lock, display)
    t2 = UserInterruptThread(lock, display)

    # execute Threads
    t1.start()
    t2.start()

    # threads.append(t1)
    # threads.append(t2)
    #
    # for t in threads:
    #     t.join()

    print("exiting main")