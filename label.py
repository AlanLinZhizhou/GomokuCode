import time

from PyQt5.QtWidgets import QLabel
from game import Gomoku


class myLabel(QLabel):
    flag = None
    notice = None

    def __init__(self, par):
        super().__init__(par)
        self.setText(str(120))
        self.d = par

    def timerEvent(self, evt):
        temp = self.text().split(':')
        a = int(temp[-1]) - 1
        if a == 0:
            # self.killTimer(self.d.id)
            time.sleep(0.5)
            a = 120
        self.setText('落子倒计时:' + str(a))

    def getText(self):
        return self.text()

    def reset(self):
        self.setText('落子倒计时:' + '120')
