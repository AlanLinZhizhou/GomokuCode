# coding:utf-8
import os
import subprocess

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import qtawesome
from PyQt5.QtWidgets import QMessageBox

from playerVsplayer import GomokuWindow2
from window import GomokuWindow

class MainUi(QtWidgets.QMainWindow):
    age = 0

    def __init__(self, ages):
        super().__init__()
        self.age = ages
        self.fall_check = '关'
        # self.browser = None
        self.init_ui()

    def againstAI(self):
        ex = GomokuWindow(self.age, self.fall_check)

    def againstPeople(self):
        ex0 = GomokuWindow2(self.age, self.fall_check)

    def introRules(self):
        a = QMessageBox.about(self, '规则介绍', '请仔细阅读主界面上的规则哦')
        # self.browser = QWebEngineView()

    def restoreGame(self):
        dir = './exes/restoreGame.exe'
        # a = QMessageBox.about(self, '使用说明', '请打开qipan目录下对应的棋盘文件.txt')
        if os.path.exists(dir):
            os.system('start ' + dir)

    def noAddicted(self):
        a = QMessageBox.about(self, '防沉迷已开启', '未满18周岁游戏时间超过两小时会被强制下线')

    def userHelp(self):
        a = QMessageBox.about(self, '注册登录', '您已成功登录，若要重新登录，请单击左下角退出游戏')

    def advice(self):
        a = QMessageBox.about(self, '反馈建议', '请联系xxxxx@qq.com')

    def focusUs(self):
        # a = QMessageBox.about(self, '关注我们', '请关注github.com/xxx')
        if self.fall_check == '开':
            self.fall_check = '关'
        else:
            self.fall_check = '开'
        a = QMessageBox.about(self, '落子确认', '落子确认已' + self.fall_check)

    def quitGame(self):
        sys.exit()
        print('exit')

    def init_ui(self):
        self.setFixedSize(960, 700)
        self.main_widget = QtWidgets.QWidget()  # 创建窗口主部件
        self.main_layout = QtWidgets.QGridLayout()  # 创建主部件的网格布局
        self.main_widget.setLayout(self.main_layout)  # 设置窗口主部件布局为网格布局

        self.left_widget = QtWidgets.QWidget()  # 创建左侧部件
        self.left_widget.setObjectName('left_widget')
        self.left_layout = QtWidgets.QGridLayout()  # 创建左侧部件的网格布局层
        self.left_widget.setLayout(self.left_layout)  # 设置左侧部件布局为网格

        self.right_widget = QtWidgets.QWidget()  # 创建右侧部件
        self.right_widget.setObjectName('right_widget')
        self.right_layout = QtWidgets.QGridLayout()
        self.right_widget.setLayout(self.right_layout)  # 设置右侧部件布局为网格

        self.main_layout.addWidget(self.left_widget, 0, 0, 12, 2)  # 左侧部件在第0行第0列，占8行3列
        self.main_layout.addWidget(self.right_widget, 0, 2, 12, 10)  # 右侧部件在第0行第3列，占8行9列
        self.setCentralWidget(self.main_widget)  # 设置窗口主部件

        self.left_close = QtWidgets.QPushButton("")  # 关闭按钮
        self.left_visit = QtWidgets.QPushButton("")  # 空白按钮
        self.left_mini = QtWidgets.QPushButton("")  # 最小化按钮

        self.left_label_1 = QtWidgets.QPushButton("游戏模块")
        self.left_label_1.setObjectName('left_label')
        self.left_label_2 = QtWidgets.QPushButton("工具模块")
        self.left_label_2.setObjectName('left_label')
        self.left_label_3 = QtWidgets.QPushButton("联系与帮助")
        self.left_label_3.setObjectName('left_label')

        self.left_button_1 = QtWidgets.QPushButton(qtawesome.icon('fa.desktop', color='white'), "人机对战")
        self.left_button_1.setObjectName('left_button')
        self.left_button_1.clicked.connect(self.againstAI)
        self.left_button_2 = QtWidgets.QPushButton(qtawesome.icon('fa.user-circle', color='white'), "双人对战")
        self.left_button_2.setObjectName('left_button')
        self.left_button_2.clicked.connect(self.againstPeople)
        self.left_button_3 = QtWidgets.QPushButton(qtawesome.icon('fa.align-justify', color='white'), "规则介绍")
        self.left_button_3.setObjectName('left_button')
        self.left_button_3.clicked.connect(self.introRules)
        self.left_button_4 = QtWidgets.QPushButton(qtawesome.icon('fa.video-camera', color='white'), "对局还原")
        self.left_button_4.setObjectName('left_button')
        self.left_button_4.clicked.connect(self.restoreGame)
        self.left_button_5 = QtWidgets.QPushButton(qtawesome.icon('fa.hand-paper-o', color='white'), "防止沉迷")
        self.left_button_5.setObjectName('left_button')
        self.left_button_5.clicked.connect(self.noAddicted)
        self.left_button_6 = QtWidgets.QPushButton(qtawesome.icon('fa.hand-o-right', color='white'), "注册登录")
        self.left_button_6.setObjectName('left_button')
        self.left_button_6.clicked.connect(self.userHelp)
        self.left_button_7 = QtWidgets.QPushButton(qtawesome.icon('fa.comment', color='white'), "反馈建议")
        self.left_button_7.setObjectName('left_button')
        self.left_button_7.clicked.connect(self.advice)
        self.left_button_8 = QtWidgets.QPushButton(qtawesome.icon('fa.star', color='white'), "落子确认")
        self.left_button_8.setObjectName('left_button')
        self.left_button_8.clicked.connect(self.focusUs)
        self.left_button_9 = QtWidgets.QPushButton(qtawesome.icon('fa.stop', color='white'), "退出游戏")
        self.left_button_9.setObjectName('left_button')
        self.left_button_9.clicked.connect(self.quitGame)
        self.left_xxx = QtWidgets.QPushButton(" ")

        self.left_layout.addWidget(self.left_mini, 0, 0, 1, 1)
        self.left_layout.addWidget(self.left_close, 0, 2, 1, 1)
        self.left_layout.addWidget(self.left_visit, 0, 1, 1, 1)
        self.left_layout.addWidget(self.left_label_1, 1, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_1, 2, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_2, 3, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_3, 4, 0, 1, 3)
        self.left_layout.addWidget(self.left_label_2, 5, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_4, 6, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_5, 7, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_6, 8, 0, 1, 3)
        self.left_layout.addWidget(self.left_label_3, 9, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_7, 10, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_8, 11, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_9, 12, 0, 1, 3)

        self.right_bar_widget = QtWidgets.QWidget()  # 右侧顶部搜索框部件
        self.right_bar_layout = QtWidgets.QGridLayout()  # 右侧顶部搜索框网格布局
        self.right_bar_widget.setLayout(self.right_bar_layout)
        self.search_icon = QtWidgets.QLabel(chr(0xf002) + ' ' + '搜索 ')
        self.search_icon.setFont(qtawesome.font('fa', 16))
        self.right_bar_widget_search_input = QtWidgets.QLineEdit()
        self.right_bar_widget_search_input.setPlaceholderText("五子棋游戏----尝试进行人机对战，难度较大嗷")

        self.right_bar_layout.addWidget(self.search_icon, 0, 0, 1, 1)
        self.right_bar_layout.addWidget(self.right_bar_widget_search_input, 0, 1, 1, 8)

        self.right_layout.addWidget(self.right_bar_widget, 0, 0, 1, 9)

        self.right_recommend_label = QtWidgets.QLabel("高分玩家")
        self.right_recommend_label.setObjectName('right_lable')

        self.right_recommend_widget = QtWidgets.QWidget()  # 推荐封面部件
        self.right_recommend_layout = QtWidgets.QGridLayout()  # 推荐封面网格布局
        self.right_recommend_widget.setLayout(self.right_recommend_layout)

        self.recommend_button_1 = QtWidgets.QToolButton()
        self.recommend_button_1.setText("可馨HANM")  # 设置按钮文本
        self.recommend_button_1.setIcon(QtGui.QIcon('./imgs/r1.jpg'))  # 设置按钮图标
        self.recommend_button_1.setIconSize(QtCore.QSize(100, 100))  # 设置图标大小
        self.recommend_button_1.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)  # 设置按钮形式为上图下文

        self.recommend_button_2 = QtWidgets.QToolButton()
        self.recommend_button_2.setText("岳麓山山妖")
        self.recommend_button_2.setIcon(QtGui.QIcon('./imgs/r2.jpg'))
        self.recommend_button_2.setIconSize(QtCore.QSize(100, 100))
        self.recommend_button_2.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)

        self.recommend_button_3 = QtWidgets.QToolButton()
        self.recommend_button_3.setText("乱杀")
        self.recommend_button_3.setIcon(QtGui.QIcon('./imgs/r3.jpg'))
        self.recommend_button_3.setIconSize(QtCore.QSize(100, 100))
        self.recommend_button_3.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)

        self.recommend_button_4 = QtWidgets.QToolButton()
        self.recommend_button_4.setText("半落")
        self.recommend_button_4.setIcon(QtGui.QIcon('./imgs/r4.jpg'))
        self.recommend_button_4.setIconSize(QtCore.QSize(100, 100))
        self.recommend_button_4.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)

        self.recommend_button_5 = QtWidgets.QToolButton()
        self.recommend_button_5.setText("渔樵老鹅")
        self.recommend_button_5.setIcon(QtGui.QIcon('./imgs/r5.jpg'))
        self.recommend_button_5.setIconSize(QtCore.QSize(100, 100))
        self.recommend_button_5.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)

        self.right_recommend_layout.addWidget(self.recommend_button_1, 0, 0)
        self.right_recommend_layout.addWidget(self.recommend_button_2, 0, 1)
        self.right_recommend_layout.addWidget(self.recommend_button_3, 0, 2)
        self.right_recommend_layout.addWidget(self.recommend_button_4, 0, 3)
        self.right_recommend_layout.addWidget(self.recommend_button_5, 0, 4)

        self.right_layout.addWidget(self.right_recommend_label, 1, 0, 1, 9)
        self.right_layout.addWidget(self.right_recommend_widget, 2, 0, 2, 9)

        self.right_newsong_lable = QtWidgets.QLabel("五子棋基本规则")
        self.right_newsong_lable.setObjectName('right_lable')

        self.right_playlist_lable = QtWidgets.QLabel("五子棋———缘起")
        self.right_playlist_lable.setObjectName('right_lable')

        self.right_newsong_widget = QtWidgets.QWidget()  # 最新歌曲部件
        self.right_newsong_layout = QtWidgets.QGridLayout()  # 最新歌曲部件网格布局
        self.right_newsong_widget.setLayout(self.right_newsong_layout)

        self.newsong_button_1 = QtWidgets.QPushButton("1.胜负规则\n最先在棋盘横/竖/斜向形成连续的相同色五个棋子的一方为胜。")
        self.newsong_button_2 = QtWidgets.QPushButton("2.行棋顺序\n黑先(Start)、白后,从天元(h8)开始相互顺序落子")
        self.newsong_button_3 = QtWidgets.QPushButton("3.棋盘\n五子棋专用棋盘为15×15,盘面有纵横各十五条等距离垂直交叉的平行线构成")
        self.newsong_button_4 = QtWidgets.QPushButton("4.禁手\n对局中如果使用将被判负的行棋手段。")
        self.newsong_button_5 = QtWidgets.QPushButton("5.建议I\n一般当敌方棋子三个相连时，你就要堵住其路，否者很可能会输掉棋局")
        self.newsong_button_6 = QtWidgets.QPushButton("6.建议II\n棋局中有很多的连环局，要时刻注意")
        self.right_newsong_layout.addWidget(self.newsong_button_1, 0, 1, )
        self.right_newsong_layout.addWidget(self.newsong_button_2, 1, 1, )
        self.right_newsong_layout.addWidget(self.newsong_button_3, 2, 1, )
        self.right_newsong_layout.addWidget(self.newsong_button_4, 3, 1, )
        self.right_newsong_layout.addWidget(self.newsong_button_5, 4, 1, )
        self.right_newsong_layout.addWidget(self.newsong_button_6, 5, 1, )

        self.right_playlist_widget = QtWidgets.QWidget()  # 播放歌单部件
        self.right_playlist_layout = QtWidgets.QGridLayout()  # 播放歌单网格布局
        self.right_playlist_widget.setLayout(self.right_playlist_layout)

        self.playlist_button_1 = QtWidgets.QToolButton()
        self.playlist_button_1.setText("五色而文状鹑卵")
        self.playlist_button_1.setIcon(QtGui.QIcon('./imgs/p1.png'))
        self.playlist_button_1.setIconSize(QtCore.QSize(100, 100))
        self.playlist_button_1.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)

        self.playlist_button_2 = QtWidgets.QToolButton()
        self.playlist_button_2.setText("棋局，纵横各十七道")
        self.playlist_button_2.setIcon(QtGui.QIcon('./imgs/p2.png'))
        self.playlist_button_2.setIconSize(QtCore.QSize(100, 100))
        self.playlist_button_2.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)

        self.playlist_button_3 = QtWidgets.QToolButton()
        self.playlist_button_3.setText("车如流水马如龙")
        self.playlist_button_3.setIcon(QtGui.QIcon('./imgs/p3.png'))
        self.playlist_button_3.setIconSize(QtCore.QSize(100, 100))
        self.playlist_button_3.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)

        self.playlist_button_4 = QtWidgets.QToolButton()
        self.playlist_button_4.setText("云归恒星白，霜下天地肃")
        self.playlist_button_4.setIcon(QtGui.QIcon('./imgs/p4.png'))
        self.playlist_button_4.setIconSize(QtCore.QSize(100, 100))
        self.playlist_button_4.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)

        self.right_playlist_layout.addWidget(self.playlist_button_1, 0, 0)
        self.right_playlist_layout.addWidget(self.playlist_button_2, 0, 1)
        self.right_playlist_layout.addWidget(self.playlist_button_3, 1, 0)
        self.right_playlist_layout.addWidget(self.playlist_button_4, 1, 1)

        self.right_layout.addWidget(self.right_newsong_lable, 4, 0, 1, 5)
        self.right_layout.addWidget(self.right_playlist_lable, 4, 5, 1, 4)
        self.right_layout.addWidget(self.right_newsong_widget, 5, 0, 1, 5)
        self.right_layout.addWidget(self.right_playlist_widget, 5, 5, 1, 4)

        self.right_process_bar = QtWidgets.QProgressBar()  # 播放进度部件
        self.right_process_bar.setValue(49)
        self.right_process_bar.setFixedHeight(3)  # 设置进度条高度
        self.right_process_bar.setTextVisible(False)  # 不显示进度条文字

        self.right_playconsole_widget = QtWidgets.QWidget()  # 播放控制部件
        self.right_playconsole_layout = QtWidgets.QGridLayout()  # 播放控制部件网格布局层
        self.right_playconsole_widget.setLayout(self.right_playconsole_layout)

        self.console_button_1 = QtWidgets.QPushButton(qtawesome.icon('fa.backward', color='#F76677'), "")
        self.console_button_2 = QtWidgets.QPushButton(qtawesome.icon('fa.forward', color='#F76677'), "")
        self.console_button_3 = QtWidgets.QPushButton(qtawesome.icon('fa.pause', color='#F76677', font=18), "")
        self.console_button_3.setIconSize(QtCore.QSize(30, 30))

        # self.right_playconsole_layout.addWidget(self.console_button_1, 0, 0)
        # self.right_playconsole_layout.addWidget(self.console_button_2, 0, 2)
        # self.right_playconsole_layout.addWidget(self.console_button_3, 0, 1)
        # self.right_playconsole_layout.setAlignment(QtCore.Qt.AlignCenter)  # 设置布局内部件居中显示

        self.right_layout.addWidget(self.right_process_bar, 9, 0, 1, 9)
        self.right_layout.addWidget(self.right_playconsole_widget, 10, 0, 1, 9)

        self.left_close.setFixedSize(15, 15)  # 设置关闭按钮的大小
        self.left_visit.setFixedSize(15, 15)  # 设置按钮大小
        self.left_mini.setFixedSize(15, 15)  # 设置最小化按钮大小

        self.left_close.setStyleSheet(
            '''QPushButton{background:#F76677;border-radius:5px;}QPushButton:hover{background:red;}''')
        self.left_visit.setStyleSheet(
            '''QPushButton{background:#F7D674;border-radius:5px;}QPushButton:hover{background:yellow;}''')
        self.left_mini.setStyleSheet(
            '''QPushButton{background:#6DDF6D;border-radius:5px;}QPushButton:hover{background:green;}''')

        self.left_widget.setStyleSheet('''
          QPushButton{border:none;color:white;}
          QPushButton#left_label{
            border:none;
            border-bottom:1px solid white;
            font-size:18px;
            font-weight:700;
            font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
          }
          QPushButton#left_button:hover{border-left:4px solid red;font-weight:700;}
        ''')

        self.right_bar_widget_search_input.setStyleSheet(
            '''QLineEdit{
                border:1px solid gray;
                width:300px;
                border-radius:10px;
                padding:2px 4px;
            }''')

        self.right_widget.setStyleSheet('''
          QWidget#right_widget{
            color:#232C51;
            background:white;
            border-top:1px solid darkGray;
            border-bottom:1px solid darkGray;
            border-right:1px solid darkGray;
            border-top-right-radius:10px;
            border-bottom-right-radius:10px;
          }
          QLabel#right_lable{
            border:none;
            font-size:16px;
            font-weight:700;
            font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
          }
        ''')

        self.right_recommend_widget.setStyleSheet(
            '''
              QToolButton{border:none;}
              QToolButton:hover{border-bottom:2px solid #F76677;}
            ''')
        self.right_playlist_widget.setStyleSheet(
            '''
              QToolButton{border:none;}
              QToolButton:hover{border-bottom:2px solid #F76677;}
            ''')

        self.right_newsong_widget.setStyleSheet('''
          QPushButton{
            border:none;
            color:gray;
            font-size:12px;
            height:40px;
            padding-left:5px;
            padding-right:10px;
            text-align:left;
          }
          QPushButton:hover{
            color:black;
            border:1px solid #F3F3F5;
            border-radius:10px;
            background:LightGray;
          }
        ''')

        self.right_process_bar.setStyleSheet('''
          QProgressBar::chunk {
            background-color: #F76677;
          }
        ''')

        self.right_playconsole_widget.setStyleSheet('''
          QPushButton{
            border:none;
          }
        ''')

        self.setWindowOpacity(1.0)  # 设置窗口透明度
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 设置窗口背景透明

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框

        self.main_widget.setStyleSheet('''
        QWidget#left_widget{
        background:gray;
        border-top:1px solid white;
        border-bottom:1px solid white;
        border-left:1px solid white;
        border-top-left-radius:10px;
        border-bottom-left-radius:10px;
        }
        ''')

        self.main_layout.setSpacing(0)


def main():
    app = QtWidgets.QApplication(sys.argv)
    gui = MainUi()
    gui.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
