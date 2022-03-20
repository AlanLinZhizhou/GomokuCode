from PyQt5.QtWidgets import QApplication

from mainframe import MainUi
from mainframe0 import MainUi0
from window import GomokuWindow
# from regAndLogin import registerAndLog
from game import Gomoku
import sys


def main():

    app = QApplication(sys.argv)
    '''注册登录'''
    # ex0=registerAndLog()
    gui0 = MainUi0()
    gui0.show()


    # if gui0.login==1:
    #     # ex = GomokuWindow(ex0.age)
    #     gui = MainUi(gui0.age)
    #     gui.show()
    #     gui0.close()

    print(gui0.login)
    sys.exit(app.exec_())



if __name__ == '__main__':
    main()
