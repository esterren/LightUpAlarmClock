'''
TODO

@author: rest
'''

import abc


class DisplayAbs(object):
    __metaclass__ = abc.ABCMeta
    '''
    TODO classdocs
    '''

#    def __init__(self):
        # self.glcd = st7565.Glcd(rgb=[22, 27, 17])
        # self.glcd.init()

    @abc.abstractmethod
    def displayDateTime(self):
        '''
        displays the current Date and Time
        '''
        return
