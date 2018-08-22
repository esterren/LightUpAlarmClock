'''
Light Up Alarm Clock

TODO

@author: esterren
'''
import threading

from UserInterruptThread import UserInterruptThread
from ClockThread import ClockThread

if __name__ == '__main__':
    #     l = ForcedSquareLayout();
    #     print(l.displayTime())
    lock = threading.Lock()
    threads = []

    # create Threads
    t1 = ClockThread(lock)
    t2 = UserInterruptThread(lock)

    # execute Threads
    t1.start()
    t2.start()

    # threads.append(t1)
    # threads.append(t2)
    #
    # for t in threads:
    #     t.join()

    print("exiting main")