from PyQt5.QtWidgets import QMainWindow, QMessageBox, QLabel, QWidget
from PyQt5.QtGui import QPainter, QPen, QColor, QPalette, QBrush, QPixmap, QRadialGradient
from PyQt5.QtCore import Qt, QPoint, QTimer
import traceback
from time import strftime, localtime
from btn import mybtn
from game2 import Gomoku
from corner_widget import CornerWidget
# import time
from label import myLabel
from label2 import myLabel2
from tkinter import *

def run_with_exc(f):
    """游戏运行出现错误时，用messagebox把错误信息显示出来"""

    def call(window, *args, **kwargs):
        try:
            return f(window, *args, **kwargs)
        except Exception:
            exc_info = traceback.format_exc()
            QMessageBox.about(window, '错误信息', exc_info)
    return call


class GomokuWindow2(QMainWindow,QWidget):


    timer = None
    lable1 = None
    rec_age = None
    label_addicted = None
    last_place_x = 7
    last_place_y = 7
    last_pc_x = 7
    last_pc_y = 7
    regret=None
    btn = None
    mycolor = 0 # 0代表黑色，1代表白色
    recheck='{[C5][玩家][超级强的电脑][后手胜][2021-04-16 00:00 Love][2021 CCGC];'
    new_x={'0':'A','1':'B','2':'C','3':'D','4':'E','5':'F','6':'G','7':'H','8':'I','9':'J','10':'K','11':'L','12':'M','13':'N','14':'O'}
    new_y = {'0': '15', '1': '14', '2': '13', '3': '12', '4': '11', '5': '10', '6': '9', '7': '8', '8': '7', '9': '6',
             '10': '5', '11': '4', '12': '3', '13': '2', '14': '1'}
    def __init__(self,age,fall_check):
        super().__init__()
        self.rec_age = age
        self.fall_check=fall_check
        self.init_ui()  # 初始化游戏界面
        self.g = Gomoku()  # 初始化游戏内容

        self.last_pos = (-1, -1)
        self.res = 0  # 记录那边获得了胜利
        self.operate_status = 0  # 游戏操作状态。0为游戏中（可操作），1为游戏结束闪烁过程中（不可操作）

    def tover(self):

        # 2. 根据操作结果进行一轮游戏循环
        res, self.flash_pieces = self.g.game_result(show=True)  # 判断游戏结果
        if res != 0:  # 如果游戏结果为“已经结束”，则显示游戏内容，并退出主循环
            self.repaint(0, 0, 650, 650)
            self.game_restart(res)
            return
        # self.g.ai_move_1step()  # 电脑下一步
        self.g.cur_step += 1
        # self.g.ai_play_1step()  # 电脑下一步

        self.mycolor +=1
        self.mycolor = self.mycolor % 2

        self.lable1.reset()
        # 电脑落子位置
        print('lastx', self.g.lastx, 'lasty', self.g.lasty)



    def init_ui(self):

        """初始化游戏界面"""
        # 1. 确定游戏界面的标题，大小和背景颜色
        self.setObjectName('MainWindow')
        self.setWindowTitle('五子棋')
        self.setFixedSize(650, 650)
        # self.setStyleSheet('#MainWindow{background-color: green}')

        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(QPixmap('imgs/muzm.jpg')))


        # 定时器 start tag
        self.lable1 = myLabel(self)
        self.lable1.setStyleSheet('font:13px;')
        self.lable1.startTimer(1000)

        self.lable1.setAutoFillBackground(True)
        self.lable1.setPalette(palette)
        self.lable1.setAlignment(Qt.AlignCenter)
        # end tag

        #悔棋
        self.regret = mybtn(self)
        self.regret.setStyleSheet('font:15px;border-width: 1px;border-style: solid;border - color: rgb(255, 170, 0);')
        self.regret.setAutoFillBackground(True)
        self.regret.setText('悔棋')
        self.regret.move(270, 615)
        self.regret.setAlignment(Qt.AlignCenter)

        self.regret.raise_()
        self.regret.setPalette(palette)

        #end tag

        #防沉迷
        if int(self.rec_age) <= 18:
            self.label_addicted = myLabel2(self)
            self.label_addicted.setStyleSheet('font:13px;width:100px;')
            self.label_addicted.startTimer(1000)
            self.label_addicted.setPalette(palette)
            self.label_addicted.setAlignment(Qt.AlignRight)
            self.label_addicted.move(400,10)





        self.setPalette(palette)
        # 2. 开启鼠标位置的追踪。并在鼠标位置移动时，使用特殊符号标记当前的位置
        self.setMouseTracking(True)
        # 3. 鼠标位置移动时，对鼠标位置的特殊标记
        self.corner_widget = CornerWidget(self)
        self.corner_widget.repaint()
        self.corner_widget.hide()
        # 4. 游戏结束时闪烁的定时器
        self.end_timer = QTimer(self)
        self.end_timer.timeout.connect(self.end_flash)
        self.flash_cnt = 0  # 游戏结束之前闪烁了多少次
        self.flash_pieces = ((-1, -1), )  # 哪些棋子需要闪烁
        # 5. 显示初始化的游戏界面
        self.show()

    @run_with_exc
    def paintEvent(self, e):
        """绘制游戏内容"""

        def draw_map():
            """绘制棋盘"""
            qp.setPen(QPen(QColor(0, 0, 0), 2, Qt.SolidLine))  # 棋盘的颜色为黑色
            # 绘制横线
            for x in range(15):
                qp.drawLine(40 * (x + 1), 40, 40 * (x + 1), 600)
            # 绘制竖线
            for y in range(15):
                qp.drawLine(40, 40 * (y + 1), 600, 40 * (y + 1))
            # 绘制棋盘中的黑点
            qp.setBrush(QColor(0, 0, 0))
            key_points = [(4, 4), (12, 4), (4, 12), (12, 12), (8, 8)]
            for t in key_points:
                qp.drawEllipse(QPoint(40 * t[0], 40 * t[1]), 5, 5)

        def draw_pieces():
            """绘制棋子"""
            # 绘制黑棋子
            qp.setPen(QPen(QColor(0, 0, 0), 1, Qt.SolidLine))
            # qp.setBrush(QColor(0, 0, 0))
            for x in range(15):
                for y in range(15):
                    if self.g.g_map[x][y] == 1:
                        if self.flash_cnt % 2 == 1 and (x, y) in self.flash_pieces:
                            continue
                        radial = QRadialGradient(40 * (x + 1), 40 * (y + 1), 15, 40 * x + 35, 40 * y + 35)  # 棋子的渐变效果
                        radial.setColorAt(0, QColor(96, 96, 96))
                        radial.setColorAt(1, QColor(0, 0, 0))
                        qp.setBrush(QBrush(radial))
                        qp.drawEllipse(QPoint(40 * (x + 1), 40 * (y + 1)), 15, 15)
            # 绘制白棋子
            qp.setPen(QPen(QColor(160, 160, 160), 1, Qt.SolidLine))
            # qp.setBrush(QColor(255, 255, 255))
            for x in range(15):
                for y in range(15):
                    if self.g.g_map[x][y] == 2:
                        if self.flash_cnt % 2 == 1 and (x, y) in self.flash_pieces:
                            continue
                        radial = QRadialGradient(40 * (x + 1), 40 * (y + 1), 15, 40 * x + 35, 40 * y + 35)  # 棋子的渐变效果
                        radial.setColorAt(0, QColor(255, 255, 255))
                        radial.setColorAt(1, QColor(160, 160, 160))
                        qp.setBrush(QBrush(radial))
                        qp.drawEllipse(QPoint(40 * (x + 1), 40 * (y + 1)), 15, 15)

        if hasattr(self, 'g'):  # 游戏还没开始的话，就不用画了
            qp = QPainter()
            qp.begin(self)
            draw_map()  # 绘制棋盘
            draw_pieces()  # 绘制棋子
            qp.end()

    @run_with_exc
    def mouseMoveEvent(self, e):
        # 1. 首先判断鼠标位置对应棋盘中的哪一个格子
        if self.regret.status == 1:  # 悔棋
            ans=QMessageBox.question(self,'游戏提醒','是否同意对方悔棋一次？',QMessageBox.Yes | QMessageBox.No)
            if ans==QMessageBox.Yes:
                self.g.g_map[int(self.last_place_x)][int(self.last_place_y)] = 0
                self.mycolor = int(self.mycolor)-1
                if int(self.mycolor)==-1:
                    self.mycolor=1
                # self.g.g_map[int(self.last_pc_x)][int(self.last_pc_y)] = 0
                self.repaint(0, 0, 650, 650)
                print('last_pc_x', self.last_pc_x, 'last_pc_y', self.last_pc_y)
                self.g.cur_step -= 2
                self.regret.status = 0
                self.recheck = self.recheck[0:-7]
            else:
                rej=QMessageBox.about(self,'对方拒绝了你的悔棋','棋如人生，没有回头路嗷')
                self.regret.status = 0


        mouse_x = e.windowPos().x()
        mouse_y = e.windowPos().y()
        if self.lable1.text()=='1':
            self.tover()
        # print(self.lable1.text)
        if 25 <= mouse_x <= 615 and 25 <= mouse_y <= 615 and (mouse_x % 40 <= 15 or mouse_x % 40 >= 25) and (mouse_y % 40 <= 15 or mouse_y % 40 >= 25):
            game_x = int((mouse_x + 15) // 40) - 1
            game_y = int((mouse_y + 15) // 40) - 1
            # print('x:',game_x,' y:',game_y)#这个代表鼠标移动的位置
        else:  # 鼠标当前的位置不对应任何一个游戏格子，将其标记为(01, 01
            game_x = -1
            game_y = -1

        # 2. 然后判断鼠标位置较前一时刻是否发生了变化
        pos_change = False  # 标记鼠标位置是否发生了变化
        if game_x != self.last_pos[0] or game_y != self.last_pos[1]:
            pos_change = True
        self.last_pos = (game_x, game_y)
        # 3. 最后根据鼠标位置的变化，绘制特殊标记
        if pos_change and game_x != -1:
            self.setCursor(Qt.PointingHandCursor)
        if pos_change and game_x == -1:
            self.setCursor(Qt.ArrowCursor)
        if pos_change and game_x != -1:
            self.corner_widget.move(25 + game_x * 40, 25 + game_y * 40)
            self.corner_widget.show()
        if pos_change and game_x == -1:
            self.corner_widget.hide()

    @run_with_exc
    def mousePressEvent(self, e):
        """根据鼠标的动作，确定落子位置"""
        if not (hasattr(self, 'operate_status') and self.operate_status == 0):
            return
        if e.button() == Qt.LeftButton:
            # 0. 首先判断确认落子是否打开
            if self.fall_check == '开':
                ans = QMessageBox.question(self, '落子提醒', '是否确认落子？', QMessageBox.Yes | QMessageBox.No)
                if ans == QMessageBox.No:
                    return
            # 1. 首先判断按下了哪个格子
            mouse_x = e.windowPos().x()
            mouse_y = e.windowPos().y()
            if (mouse_x % 40 <= 15 or mouse_x % 40 >= 25) and (mouse_y % 40 <= 15 or mouse_y % 40 >= 25):
                game_x = int((mouse_x + 15) // 40) - 1
                game_y = int((mouse_y + 15) // 40) - 1
                # 玩家1棋子位置
                if self.g.g_map[game_x][game_y] != 0:
                    return
                if int(self.mycolor)%2 == 0:
                    color='B'
                else:
                    color='W'
                print('x:', game_x, ' y:', game_y)
                if 15 > game_x >= 0 and 15 > game_y >= 0:
                    self.recheck = self.recheck + color + '(' + self.new_x[str(game_x)] + ',' + self.new_y[
                        str(game_y)] + ');'

                    self.last_place_x = str(game_x)
                    self.last_place_y = str(game_y)
                else:   # 鼠标点击位置不正确
                    return
                # 计时器更新
                self.lable1.reset()

            else:  # 鼠标点击的位置不正确
                return
            self.g.move_1step(True, game_x, game_y,int(self.mycolor)+1)
            self.mycolor +=1
            self.mycolor = self.mycolor%2

            # 2. 根据操作结果进行一轮游戏循环
            res, self.flash_pieces = self.g.game_result(show=True)  # 判断游戏结果
            if res != 0:  # 如果游戏结果为“已经结束”，则显示游戏内容，并退出主循环
                self.repaint(0, 0, 650, 650)
                self.game_restart(res)
                return


    @run_with_exc
    def end_flash(self):
        # 游戏结束时的闪烁操作
        if self.flash_cnt <= 5:
            # 执行闪烁
            self.flash_cnt += 1
            self.repaint()
        else:
            # 闪烁完毕，执行重新开始的操作
            self.end_timer.stop()
            #存好棋盘信息
            logs=strftime("%Y-%m-%d-at-%Hh%Mm%Ss", localtime())
            dir='./qipan/'+logs+'.txt'
            with open(dir,'w') as f1:
                f1.writelines(self.recheck[0:-2]+'}')
            # 1. 显示游戏结束的信息
            if self.res == 1:
                QMessageBox.about(self, '游戏结束', '黑棋获胜!')
            elif self.res == 2:
                QMessageBox.about(self, '游戏结束', '白棋获胜!')
            elif self.res == 3:
                QMessageBox.about(self, '游戏结束', '平局!')
            else:
                raise ValueError('当前游戏结束的标志位为' + self.res + '. 而游戏结束的标志位必须为1, 2 或 3')
            # 2. 游戏重新开始的操作
            self.res = 0
            self.mycolor=0
            self.operate_status = 0
            self.flash_cnt = 0
            self.g = Gomoku()  # 重新初始化游戏内容
            self.repaint(0, 0, 650, 650)  # 重新绘制游戏界面

    def game_restart(self, res):
        """游戏出现开始"""
        self.res = res  # 标记谁获胜了
        self.operate_status = 1  # 游戏结束时的闪烁过程中，不可操作
        self.end_timer.start(300)  # 开始结束时闪烁的计时器
