from PyQt5.QtWidgets import QLabel


class mybtn(QLabel):
    status=0
    def __init__(self, parent=None):
        super(mybtn, self).__init__(parent)

    def mouseDoubleClickEvent(self, e):
        print
        ('mouse double clicked')

    def mousePressEvent(self, e):
        self.status=1
        print('mousePressEvent')













