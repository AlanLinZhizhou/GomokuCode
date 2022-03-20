import time

from PyQt5.QtWidgets import QLabel
from game import Gomoku


class myLabel2(QLabel):


    def __init__(self,par):
        super().__init__(par)
        self.setText(str(7200))
        self.d=par

    def timerEvent(self, evt):
        temp=self.text().split(':')
        a = int(temp[-1])-1
        # a = int(self.text()) - 1
        if a == 0:
            # self.killTimer(self.d.id)
            time.sleep(0.5)
            self.killTimer(self.d.id)

        self.setText('防沉迷:'+str(a))


    def getText(self):
        # Gomoku().ai_play_1step()
        return self.text()

    def reset(self):
        self.setText('防沉迷：','120')