from asciimatics.widgets import Frame, Layout, Label
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.exceptions import ResizeScreenError, NextScene, StopApplication
from threading import Thread
import time
import sys

class ClockView(Frame):
    def __init__(self, screen: Screen):
        super(ClockView, self).__init__(screen, screen.height, screen.width)
        layout = Layout([1], fill_frame=True)
        self._screen = screen
        self.add_layout(layout)
        self._date_label = Label(label="")
        self._time_label = Label(label="00:00:00")
        layout.add_widget(self._date_label)
        layout.add_widget(self._time_label)
        self.fix()

    def tick(self):
        self._date_label.text = time.strftime("%d.%m.%y")
        self._time_label.text = time.strftime("%H:%M:%S")
        self._screen.force_update()


class Clock(Thread):
    def __init__(self, view: ClockView, interval=0.5):
        Thread.__init__(self)
        self.view = view
        self.setDaemon(True)
        self.interval = interval

    def run(self):
        time.sleep(1)
        while True:
            self.view.tick()
            time.sleep(self.interval)

def demo(screen:Screen):
    clock_view = ClockView(screen)
    ct = Clock(view=clock_view)
    ct.start()
    scene = Scene([clock_view], -1, name="Main")
    screen.play([scene], stop_on_resize=True)

if __name__ == '__main__':
    #try:
    #screen = Screen.open()
    Screen.wrapper(demo, catch_interrupt=False)
    #try:
    #    demo(screen)
    #finally:
    #    Screen.close()
    #    sys.exit(0)
    #except ResizeScreenError as e:
    #Screen.close()
    sys.exit(0)