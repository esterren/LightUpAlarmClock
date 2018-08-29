'''
TODO
'''
import time
from luac.appifc.displayabs import DisplayAbs
from asciimatics.screen import Screen
from asciimatics.scene import Scene
from asciimatics.widgets import Frame, Label, Layout
from asciimatics.exceptions import ResizeScreenError
import sys

class ClockView(Frame):
    def __init__(self, screen):
        super(ClockView, self).__init__(screen, screen.height, screen.width)
        self.time_label = Label(label="00:00:00")
        layout = Layout([100])
        self.add_layout(layout)
        layout.add_widget(self.time_label)
        self.fix()

    def set_time(self):
        self.time_label.text = time.strftime("%H:%M:%S", time.gmtime())

class SimDisplay(DisplayAbs):
    def __init__(self):
        self._screen = Screen.open(catch_interrupt=True)
        self._clock_view = ClockView(self._screen)
        self._scenes = [
            Scene([self._clock_view], -1, name="Main")
        ]
        self._screen.set_scenes(self._scenes, start_scene=None)
        #last_scene = None
        #while True:
        #    try:
        #        Screen.wrapper(self.demo, arguments=[last_scene])
        #        sys.exit(0)
        #    except ResizeScreenError as e:
        #        last_scene = e.scene

        #self.screen = Screen.open(200, False, 'UTF-8')

    def __del__(self):
        self._screen.close()

    def displayDateTime(self):
        self._clock_view.set_time()
        self._screen.draw_next_frame(repeat=True)
        #self.screen.print_at(time.strftime("%H:%M:%S", time.gmtime()),0,0)
        #self.screen.refresh()
        #print(time.strftime("%H:%M:%S", time.gmtime()))