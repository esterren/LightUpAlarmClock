from asciimatics.widgets import Frame, Layout, Label, Button
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.exceptions import ResizeScreenError, NextScene, StopApplication
from threading import Thread
import time
import sys

class MainView(Frame):
    def __init__(self, screen: Screen):
        super(MainView, self).__init__(screen, screen.height, screen.width)
        layout_top = Layout([1], fill_frame=True)
        self._screen = screen
        self.add_layout(layout_top)
        self._date_label = Label(label="")
        self._time_label = Label(label="")
        layout_top.add_widget(self._date_label)
        layout_top.add_widget(self._time_label)

        layout_bottom = Layout([1])
        self.add_layout(layout_bottom)
        layout_bottom.add_widget(Button("Snooze", self._snooze),0)

        self.fix()


    def _snooze(self):
        self.palette["background"] = (Screen.COLOUR_BLUE, Screen.A_NORMAL, Screen.COLOUR_WHITE)
        self._screen.force_update()

    def tick(self):
        self._date_label.text = time.strftime("%d.%m.%y")
        self._time_label.text = time.strftime("%H:%M:%S")
        self._screen.force_update()


class Clock(Thread):
    def __init__(self, view: MainView, interval=0.5):
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
    clock_view = MainView(screen)
    ct = Clock(view=clock_view)
    ct.start()
    scene = Scene([clock_view], -1, name="Main")
    screen.play([scene], stop_on_resize=True)

if __name__ == '__main__':
    screen = Screen.open()
    #Screen.wrapper(demo, catch_interrupt=False)
    restore = True
    try:
        try:
            demo(screen)
        except ResizeScreenError:
            restore = False
            raise
    finally:
        screen.close(restore)

    sys.exit(0)
