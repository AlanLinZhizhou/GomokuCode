# coding:utf-8
import os
import pickle
import subprocess
import time

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import qtawesome
from PyQt5.QtWidgets import QMessageBox, QApplication

from mainframe import MainUi
from playerVsplayer import GomokuWindow2
from window import GomokuWindow


class MainUi0(QtWidgets.QMainWindow):
    age = 0
    newsong_lab_72 = None
    newsong_lab_82 = None
    newsong_lab_12 = None
    newsong_lab_22 = None
    newsong_lab_32 = None
    newsong_lab_42 = None

    status = 0
    def __init__(self):
        super().__init__()
        self.login = 0
        self.gui = MainUi(self.age)
        # self.age=ages
        self.init_ui()

    def usr_log_in(self):
        # 输入框获取用户名密码
        usr_name = self.newsong_lab_72.text()
        usr_pwd = self.newsong_lab_82.text()
        # 从本地字典获取用户信息，如果没有则新建本地数据库
        try:
            with open('usr_info.pickle', 'rb') as usr_file:
                usrs_info = pickle.load(usr_file)
        except FileNotFoundError:
            with open('usr_info.pickle', 'wb') as usr_file:
                usrs_info = {'admin': 'admin'}
                pickle.dump(usrs_info, usr_file)

        # 从本地字典获取用户年龄信息，如果没有则新建本地数据库
        try:
            with open('usr_age_info.pickle', 'rb') as usr_file:
                usrs_age_info = pickle.load(usr_file)
        except FileNotFoundError:
            with open('usr_age_info.pickle', 'wb') as usr_file:
                usrs_age_info = {'admin': '99'}
                pickle.dump(usrs_info, usr_file)
        # 判断用户名和密码是否匹配
        if usr_name in usrs_info:
            if usr_pwd == usrs_info[usr_name]:
                message='欢迎您：' + usr_name
                QMessageBox.about(self, 'welcome', message)
                self.age=usrs_age_info[usr_name]
                self.status = 1
                self.login = 1

                # gui = MainUi(self.age)
                self.gui.login = 1
                self.gui.show()
                # time.sleep(0.5)
                self.hide()
                # app = QApplication(sys.argv)
                # sys.exit(app.exec_())
                # self.setVisible(False)

                # time.sleep(0.5)
                # sys.exit()

                # self.window.destroy()

                # self.usr_sign_quit()
            else:
                QMessageBox.about(self, 'info', '密码错误')
        # 用户名密码不能为空
        elif usr_name == '' or usr_pwd == '':
            QMessageBox.about(self, 'info', '用户名或密码为空')

        # 不在数据库中弹出是否注册的框
        else:
            QMessageBox.about(self, 'info', '您还没注册，请先注册')
            # if is_signup:
            #     self.usr_sign_up()

    def usr_sign_up(self):
        # 确认注册时的相应函数
        # 获取输入框内的内容
        nn = self.newsong_lab_12.text()
        np = self.newsong_lab_32.text()
        npf = self.newsong_lab_42.text()
        na = self.newsong_lab_22.text()

        # 本地加载已有用户信息,如果没有则已有用户信息为空
        try:
            with open('usr_info.pickle', 'rb') as usr_file:
                exist_usr_info = pickle.load(usr_file)
        except FileNotFoundError:
            exist_usr_info = {}

        try:
            with open('usr_age_info.pickle', 'rb') as usr_file:
                exist_usr_age_info = pickle.load(usr_file)
        except FileNotFoundError:
            exist_usr_age_info = {}

            # 检查用户名存在、密码为空、密码前后不一致
        if nn in exist_usr_info:
            QMessageBox.about(self, '错误', '用户名已存在')
            # tk.messagebox.showerror('错误', '用户名已存在')
        elif np == '' or nn == '':
            QMessageBox.about(self, '错误', '用户名或密码为空')
            # tk.messagebox.showerror('错误', '用户名或密码为空')
        elif np != npf:
            QMessageBox.about(self, '错误', '密码前后不一致')
            # tk.messagebox.showerror('错误', '密码前后不一致')
        # 注册信息没有问题则将用户名密码写入数据库
        else:
            exist_usr_info[nn] = np
            exist_usr_age_info[nn] = na
            with open('usr_info.pickle', 'wb') as usr_file:
                pickle.dump(exist_usr_info, usr_file)
            with open('usr_age_info.pickle', 'wb') as usr_age_file:
                pickle.dump(exist_usr_age_info, usr_age_file)
            QMessageBox.about(self, '欢迎', '注册成功,请登录')
            # tk.messagebox.showinfo('欢迎', '注册成功')




    def againstAI(self):
        # ex = GomokuWindow(self.age)
        a = QMessageBox.about(self, '未登录提示', '请注册登录后使用')

    def againstPeople(self):
        a = QMessageBox.about(self, '未登录提示', '请注册登录后使用')

    def introRules(self):
        a = QMessageBox.about(self, '未登录提示', '请注册登录后使用')

    def restoreGame(self):
        a = QMessageBox.about(self, '未登录提示', '请注册登录后使用')

    def noAddicted(self):
        a = QMessageBox.about(self, '未登录提示', '请注册登录后使用')

    def userHelp(self):
        a = QMessageBox.about(self, '未登录提示', '请注册登录后使用')

    def advice(self):
        a = QMessageBox.about(self, '未登录提示', '请注册登录后使用')

    def focusUs(self):
        a = QMessageBox.about(self, '未登录提示', '请注册登录后使用')

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
        self.left_button_6 = QtWidgets.QPushButton(qtawesome.icon('fa.hand-o-right', color='white'), "用户帮助")
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
        self.right_bar_widget_search_input.setPlaceholderText("未登录，请登录后使用")

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

        self.right_newsong_lable = QtWidgets.QLabel("注册登录模块")
        self.right_newsong_lable.setObjectName('right_lable')

        self.right_playlist_lable = QtWidgets.QLabel("五子棋----缘起")
        self.right_playlist_lable.setObjectName('right_lable')

        self.right_newsong_widget = QtWidgets.QWidget()  # 最新歌曲部件
        self.right_newsong_layout = QtWidgets.QGridLayout()  # 最新歌曲部件网格布局
        self.right_newsong_widget.setLayout(self.right_newsong_layout)

        self.newsong_button_1 = QtWidgets.QPushButton("Register")
        self.newsong_button_1.setStyleSheet('color:rgb(20,20,20,255);font-size:20px;font-weight:bold;')
        self.newsong_lab_11 = QtWidgets.QLabel('用户名：')
        self.newsong_lab_12 = QtWidgets.QLineEdit()
        self.newsong_lab_21 = QtWidgets.QLabel('年龄：')
        self.newsong_lab_22 = QtWidgets.QLineEdit()
        self.newsong_lab_31 = QtWidgets.QLabel('密码：')
        self.newsong_lab_32 = QtWidgets.QLineEdit()
        self.newsong_lab_32.setEchoMode(2)
        self.newsong_lab_41 = QtWidgets.QLabel('确认密码：')
        self.newsong_lab_42 = QtWidgets.QLineEdit()
        self.newsong_lab_42.setEchoMode(2)
        self.newsong_tab_52 = QtWidgets.QPushButton('确认注册')
        self.newsong_tab_52.setStyleSheet('color:rgb(20,20,20,255);font-weight:bold;border:1px solid;text-align:center')
        self.newsong_tab_52.clicked.connect(self.usr_sign_up)

        self.newsong_button_6 = QtWidgets.QPushButton("Login")
        self.newsong_button_6.setStyleSheet('color:rgb(20,20,20,255);font-size:20px;font-weight:bold;')
        self.newsong_lab_71 = QtWidgets.QLabel('用户名：')
        self.newsong_lab_72 = QtWidgets.QLineEdit()
        self.newsong_lab_81 = QtWidgets.QLabel('密码：')
        self.newsong_lab_82 = QtWidgets.QLineEdit()
        self.newsong_lab_82.setEchoMode(2)
        self.newsong_lab_9 = QtWidgets.QPushButton('登录')
        self.newsong_lab_9.setStyleSheet('color:rgb(20,20,20,255);font-weight:bold;border:1px solid;text-align:center')
        self.newsong_lab_9.clicked.connect(self.usr_log_in)
        # self.newsong_button_4 = QtWidgets.QPushButton("4.禁手\n对局中如果使用将被判负的行棋手段。")
        # self.newsong_button_5 = QtWidgets.QPushButton("5.建议I\n一般当敌方棋子三个相连时，你就要堵住其路，否者很可能会输掉棋局")
        # self.newsong_button_6 = QtWidgets.QPushButton("6.建议II\n棋局中有很多的连环局，要时刻注意")
        self.right_newsong_layout.addWidget(self.newsong_button_1, 0, 1, )
        self.right_newsong_layout.addWidget(self.newsong_lab_11, 1, 1, )
        self.right_newsong_layout.addWidget(self.newsong_lab_12, 1, 2, )
        self.right_newsong_layout.addWidget(self.newsong_lab_21, 2, 1, )
        self.right_newsong_layout.addWidget(self.newsong_lab_22, 2, 2, )
        self.right_newsong_layout.addWidget(self.newsong_lab_31, 3, 1, )
        self.right_newsong_layout.addWidget(self.newsong_lab_32, 3, 2, )
        self.right_newsong_layout.addWidget(self.newsong_lab_41, 4, 1, )
        self.right_newsong_layout.addWidget(self.newsong_lab_42, 4, 2, )
        self.right_newsong_layout.addWidget(self.newsong_tab_52, 5, 2, )
        self.right_newsong_layout.addWidget(self.newsong_button_6, 6, 1, )
        self.right_newsong_layout.addWidget(self.newsong_lab_71, 7, 1, )
        self.right_newsong_layout.addWidget(self.newsong_lab_72, 7, 2, )
        self.right_newsong_layout.addWidget(self.newsong_lab_81, 8, 1, )
        self.right_newsong_layout.addWidget(self.newsong_lab_82, 8, 2, )
        self.right_newsong_layout.addWidget(self.newsong_lab_9, 9, 2, )


        # self.right_newsong_layout.addWidget(self.newsong_button_4, 3, 1, )
        # self.right_newsong_layout.addWidget(self.newsong_button_5, 4, 1, )
        # self.right_newsong_layout.addWidget(self.newsong_button_6, 5, 1, )

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
        # self.right_playlist_layout.addWidget(self.playlist_button_22, 2, 1)
        # self.right_playlist_layout.addWidget(self.playlist_button_32, 3, 1)

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
            color:white;
            font-size:12px;
            height:40px;
            padding-left:5px;
            padding-right:10px;
            text-align:left;
          }
          QPushButton:hover{
            color:white;
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
    gui = MainUi0(0)
    gui.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()