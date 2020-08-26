# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ITL.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import os,sys,psutil
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):

    def __init__(self):
        self.pingSubP_pid = 0
        self.otherSubP_pid = 0

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(486, 498)

        # 获取窗口图标路径
        iconfile = self.resource_path(os.path.join('img', 'rec.png'))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(iconfile), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        Form.setWindowIcon(icon)
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 471, 461))
        self.tabWidget.setObjectName("tabWidget")
        self.pingTab = QtWidgets.QWidget()
        self.pingTab.setObjectName("pingTab")
        self.pingplainTextEdit = QtWidgets.QPlainTextEdit(self.pingTab)
        self.pingplainTextEdit.setGeometry(QtCore.QRect(10, 230, 441, 201))
        self.pingplainTextEdit.setReadOnly(True)
        self.pingplainTextEdit.setObjectName("pingplainTextEdit")
        self.groupBox = QtWidgets.QGroupBox(self.pingTab)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 441, 211))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 20, 71, 21))
        self.label.setObjectName("label")
        self.pingAddressLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.pingAddressLineEdit.setGeometry(QtCore.QRect(90, 20, 161, 21))
        self.pingAddressLineEdit.setObjectName("pingAddressLineEdit")
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 120, 421, 81))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(30, 20, 41, 21))
        self.label_4.setObjectName("label_4")
        self.pingSendLabel = QtWidgets.QLabel(self.groupBox_2)
        self.pingSendLabel.setGeometry(QtCore.QRect(70, 20, 61, 21))
        self.pingSendLabel.setText("")
        self.pingSendLabel.setObjectName("pingSendLabel")
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(310, 20, 41, 21))
        self.label_6.setObjectName("label_6")
        self.pingLoseLabel = QtWidgets.QLabel(self.groupBox_2)
        self.pingLoseLabel.setGeometry(QtCore.QRect(350, 20, 54, 21))
        self.pingLoseLabel.setText("")
        self.pingLoseLabel.setObjectName("pingLoseLabel")
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setGeometry(QtCore.QRect(170, 20, 41, 21))
        self.label_8.setObjectName("label_8")
        self.pingReceptLabel = QtWidgets.QLabel(self.groupBox_2)
        self.pingReceptLabel.setGeometry(QtCore.QRect(210, 20, 61, 21))
        self.pingReceptLabel.setText("")
        self.pingReceptLabel.setObjectName("pingReceptLabel")
        self.pingLtimeLabel = QtWidgets.QLabel(self.groupBox_2)
        self.pingLtimeLabel.setGeometry(QtCore.QRect(210, 50, 61, 21))
        self.pingLtimeLabel.setText("")
        self.pingLtimeLabel.setObjectName("pingLtimeLabel")
        self.label_11 = QtWidgets.QLabel(self.groupBox_2)
        self.label_11.setGeometry(QtCore.QRect(290, 50, 61, 21))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.groupBox_2)
        self.label_12.setGeometry(QtCore.QRect(150, 50, 61, 21))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.groupBox_2)
        self.label_13.setGeometry(QtCore.QRect(10, 50, 61, 21))
        self.label_13.setObjectName("label_13")
        self.pingAtimeLabel = QtWidgets.QLabel(self.groupBox_2)
        self.pingAtimeLabel.setGeometry(QtCore.QRect(350, 50, 61, 21))
        self.pingAtimeLabel.setText("")
        self.pingAtimeLabel.setObjectName("pingAtimeLabel")
        self.pingStimeLabel = QtWidgets.QLabel(self.groupBox_2)
        self.pingStimeLabel.setGeometry(QtCore.QRect(70, 50, 61, 21))
        self.pingStimeLabel.setText("")
        self.pingStimeLabel.setObjectName("pingStimeLabel")
        self.pingPushButton = QtWidgets.QPushButton(self.groupBox)
        self.pingPushButton.setGeometry(QtCore.QRect(260, 20, 75, 21))
        self.pingPushButton.setObjectName("pingPushButton")
        self.groupBox_6 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_6.setGeometry(QtCore.QRect(10, 50, 421, 61))
        self.groupBox_6.setTitle("")
        self.groupBox_6.setObjectName("groupBox_6")
        self.label_3 = QtWidgets.QLabel(self.groupBox_6)
        self.label_3.setGeometry(QtCore.QRect(180, 30, 101, 21))
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.groupBox_6)
        self.label_2.setGeometry(QtCore.QRect(10, 30, 71, 21))
        self.label_2.setObjectName("label_2")
        self.pingByteLineEdit = QtWidgets.QLineEdit(self.groupBox_6)
        self.pingByteLineEdit.setGeometry(QtCore.QRect(290, 30, 113, 20))
        self.pingByteLineEdit.setObjectName("pingByteLineEdit")
        self.pingCheckBox = QtWidgets.QCheckBox(self.groupBox_6)
        self.pingCheckBox.setGeometry(QtCore.QRect(10, 10, 71, 21))
        self.pingCheckBox.setObjectName("pingCheckBox")
        self.pingCountLineEdit = QtWidgets.QLineEdit(self.groupBox_6)
        self.pingCountLineEdit.setGeometry(QtCore.QRect(80, 30, 61, 20))
        self.pingCountLineEdit.setObjectName("pingCountLineEdit")
        self.pingStoppushButton = QtWidgets.QPushButton(self.groupBox)
        self.pingStoppushButton.setGeometry(QtCore.QRect(350, 20, 75, 21))
        self.pingStoppushButton.setObjectName("pingStoppushButton")
        self.tabWidget.addTab(self.pingTab, "")
        self.otherTab = QtWidgets.QWidget()
        self.otherTab.setObjectName("otherTab")
        self.otherPlainTextEdit = QtWidgets.QPlainTextEdit(self.otherTab)
        self.otherPlainTextEdit.setGeometry(QtCore.QRect(10, 210, 441, 221))
        self.otherPlainTextEdit.setReadOnly(True)
        self.otherPlainTextEdit.setObjectName("otherPlainTextEdit")
        self.groupBox_3 = QtWidgets.QGroupBox(self.otherTab)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 10, 441, 61))
        self.groupBox_3.setObjectName("groupBox_3")
        self.ipconfigALLpushButton = QtWidgets.QPushButton(self.groupBox_3)
        self.ipconfigALLpushButton.setGeometry(QtCore.QRect(20, 20, 81, 23))
        self.ipconfigALLpushButton.setObjectName("ipconfigALLpushButton")
        self.ipconfigFlushdnspushButton = QtWidgets.QPushButton(self.groupBox_3)
        self.ipconfigFlushdnspushButton.setGeometry(QtCore.QRect(120, 20, 81, 23))
        self.ipconfigFlushdnspushButton.setObjectName("ipconfigFlushdnspushButton")
        self.ipconfigReleasepushButton = QtWidgets.QPushButton(self.groupBox_3)
        self.ipconfigReleasepushButton.setGeometry(QtCore.QRect(220, 20, 91, 23))
        self.ipconfigReleasepushButton.setObjectName("ipconfigReleasepushButton")
        self.ipconfigRenewpushButton = QtWidgets.QPushButton(self.groupBox_3)
        self.ipconfigRenewpushButton.setGeometry(QtCore.QRect(330, 20, 91, 23))
        self.ipconfigRenewpushButton.setObjectName("ipconfigRenewpushButton")
        self.groupBox_4 = QtWidgets.QGroupBox(self.otherTab)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 80, 441, 61))
        self.groupBox_4.setObjectName("groupBox_4")
        self.nslookupPushButton = QtWidgets.QPushButton(self.groupBox_4)
        self.nslookupPushButton.setGeometry(QtCore.QRect(20, 20, 81, 23))
        self.nslookupPushButton.setObjectName("nslookupPushButton")
        self.nslookupLineEdit = QtWidgets.QLineEdit(self.groupBox_4)
        self.nslookupLineEdit.setGeometry(QtCore.QRect(110, 20, 181, 21))
        self.nslookupLineEdit.setObjectName("nslookupLineEdit")
        self.nslookupCheckBox = QtWidgets.QCheckBox(self.groupBox_4)
        self.nslookupCheckBox.setGeometry(QtCore.QRect(300, 20, 101, 21))
        self.nslookupCheckBox.setObjectName("nslookupCheckBox")
        self.groupBox_5 = QtWidgets.QGroupBox(self.otherTab)
        self.groupBox_5.setGeometry(QtCore.QRect(10, 150, 441, 51))
        self.groupBox_5.setObjectName("groupBox_5")
        self.tracertLineEdit = QtWidgets.QLineEdit(self.groupBox_5)
        self.tracertLineEdit.setGeometry(QtCore.QRect(110, 20, 181, 21))
        self.tracertLineEdit.setObjectName("tracertLineEdit")
        self.tracertPushButton = QtWidgets.QPushButton(self.groupBox_5)
        self.tracertPushButton.setGeometry(QtCore.QRect(20, 20, 81, 23))
        self.tracertPushButton.setObjectName("tracertPushButton")
        self.tracertStoppushButton_2 = QtWidgets.QPushButton(self.groupBox_5)
        self.tracertStoppushButton_2.setGeometry(QtCore.QRect(310, 20, 91, 23))
        self.tracertStoppushButton_2.setObjectName("tracertStoppushButton_2")
        self.tabWidget.addTab(self.otherTab, "")
        self.copyrightlabel = QtWidgets.QLabel(Form)
        self.copyrightlabel.setGeometry(QtCore.QRect(0, 480, 481, 16))
        self.copyrightlabel.setObjectName("copyrightlabel")

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "ITtools"))
        self.groupBox.setToolTip(_translate("Form", "<html><head/><body><p>Ping 包测试</p></body></html>"))
        self.groupBox.setTitle(_translate("Form", "Ping"))
        self.label.setText(_translate("Form", "Ping包地址："))
        self.groupBox_2.setTitle(_translate("Form", "结果"))
        self.label_4.setText(_translate("Form", "发送："))
        self.label_6.setText(_translate("Form", "丢失："))
        self.label_8.setText(_translate("Form", "接收："))
        self.label_11.setText(_translate("Form", "平均时间："))
        self.label_12.setText(_translate("Form", "最长时间："))
        self.label_13.setText(_translate("Form", "最短时间："))
        self.pingPushButton.setText(_translate("Form", "Ping"))
        self.label_3.setText(_translate("Form", "Ping包大小(byte)："))
        self.label_2.setText(_translate("Form", "<html><head/><body><p>Ping包次数：</p></body></html>"))
        self.pingCheckBox.setText(_translate("Form", "附加功能"))
        self.pingStoppushButton.setText(_translate("Form", "Stop Ping"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.pingTab), _translate("Form", "Ping工具"))
        self.groupBox_3.setTitle(_translate("Form", "IPconfig"))
        self.ipconfigALLpushButton.setText(_translate("Form", "显示网卡信息"))
        self.ipconfigFlushdnspushButton.setText(_translate("Form", "刷新DNS"))
        self.ipconfigReleasepushButton.setText(_translate("Form", "释放网卡IP"))
        self.ipconfigRenewpushButton.setText(_translate("Form", "重新获取网卡IP"))
        self.groupBox_4.setTitle(_translate("Form", "查询域名解析"))
        self.nslookupPushButton.setText(_translate("Form", "nslookup"))
        self.nslookupCheckBox.setText(_translate("Form", "通过谷歌解析"))
        self.groupBox_5.setTitle(_translate("Form", "路由跟踪"))
        self.tracertPushButton.setText(_translate("Form", "tracert"))
        self.tracertStoppushButton_2.setText(_translate("Form", "Stop tracert"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.otherTab), _translate("Form", "其他工具"))
        self.copyrightlabel.setText(_translate("Form", "Copyright zealous"))

        # ping相关
        self.pingPushButton.clicked.connect(self.pingButtonClicked)
        self.pingCountLineEdit.setEnabled(False)
        self.pingByteLineEdit.setEnabled(False)
        self.pingCheckBox.stateChanged.connect(self.pingCheckboxStateChanged)
        self.pingStoppushButton.clicked.connect(self.pingStopButtonClicked)

        # ipconfig功能
        self.ipconfigALLpushButton.clicked.connect(self.ipconfigAllButtonClicked)
        self.ipconfigFlushdnspushButton.clicked.connect(self.ipconfigFlushDNSButtonClicked)
        self.ipconfigReleasepushButton.clicked.connect(self.ipconfigReleaseButtonClicked)
        self.ipconfigRenewpushButton.clicked.connect(self.ipconfigRenewButtonClicked)

        # nslookup功能
        self.nslookupPushButton.clicked.connect(self.nslookupButtonClicked)

        # tracert相关
        self.tracertPushButton.clicked.connect(self.tracertButtonClicked)
        self.tracertStoppushButton_2.clicked.connect(self.tracertStopButtonClick)

    # 生成窗口图标路径
    def resource_path(self, relative_path):
        if getattr(sys, 'frozen', False):
            # 这个sys._MEIPASS只在exe下有效
            base_path = sys._MEIPASS
        else:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)

    # pingcheckbox选择事件
    def pingCheckboxStateChanged(self):
        # 如果选中了就文本框启用
        if self.pingCheckBox.isChecked():
            self.pingCountLineEdit.setEnabled(True)
            self.pingByteLineEdit.setEnabled(True)
        else:
            self.pingCountLineEdit.setEnabled(False)
            self.pingByteLineEdit.setEnabled(False)

    # ping按钮事件
    def pingButtonClicked(self):
        # 设置ping包次数和包大小初始变量
        pingCount = ''
        pingByte = ''
        # 判断文本框是否为空
        if self.pingAddressLineEdit.text():
            # 获取文本内容
            pingAddress = self.pingAddressLineEdit.text()
            # 判断checkbox是否勾选了
            if self.pingCheckBox.isChecked():
                if self.pingCountLineEdit.text():
                    pingCount = '-n %s' % self.pingCountLineEdit.text()
                if self.pingByteLineEdit.text():
                    pingByte = '-l %s' % self.pingByteLineEdit.text()
            # cmd命令
            cmd = 'ping {pingAddress} {pingCount} {pingByte}'.format(pingAddress=pingAddress,
                                                                     pingCount=pingCount,
                                                                     pingByte=pingByte)
            # 发送到线程运行
            self.thread = pingThread(cmd)
            # 连接回调函数并接收结果
            self.thread.signal.connect(self.pingCallback)
            self.thread.signal_list.connect(self.pingResultcallback)
            self.thread.pidsignal.connect(self.pingSubPID)
            self.thread.start()

    # 获取ping线程PID
    def pingSubPID(self,subP_pid):
        self.pingSubP_pid = subP_pid


    # 文本框显示
    def pingCallback(self,msg):
        self.pingplainTextEdit.appendPlainText(str(msg))

    # 对应的label中显示结果
    def pingResultcallback(self,pinglist):
        if pinglist:
            # 根据最后一个结果是否有括号进行筛选
            if ')' not in pinglist[-1]:
                data_list = pinglist[-2].replace(',', '=').replace('，', '=').split('=')
                time_list = pinglist[-1].replace(',','=').replace('，','=').split('=')
                self.pingSendLabel.setText(data_list[1].strip())
                self.pingReceptLabel.setText(data_list[3].strip())
                self.pingLoseLabel.setText(data_list[5].split(' ')[1].strip())
                self.pingStimeLabel.setText(time_list[1].strip())
                self.pingLtimeLabel.setText(time_list[3].strip())
                self.pingAtimeLabel.setText(time_list[5].strip())
            else:
                data_list = pinglist[-1].replace(',', '=').replace('，', '=').split('=')
                self.pingSendLabel.setText(data_list[1].strip())
                self.pingReceptLabel.setText(data_list[3].strip())
                self.pingLoseLabel.setText(data_list[5].split(' ')[1].strip())
                self.pingStimeLabel.setText('')
                self.pingLtimeLabel.setText('')
                self.pingAtimeLabel.setText('')

    # ping 停止进程按钮
    def pingStopButtonClicked(self):
        # 判断进程id是否为True，默认为0
        if self.pingSubP_pid:
            rekill = self.kill(self.pingSubP_pid)
            self.pingplainTextEdit.appendPlainText(rekill)



    # ipconfig功能
    def ipconfigAllButtonClicked(self):
        self.otherPlainTextEdit.setPlainText('')
        cmd = 'ipconfig /all'
        self.thread = otherThreader(cmd)
        self.thread.signal.connect(self.ipconfigAllCallback)
        self.thread.start()

    def ipconfigAllCallback(self,msg):
        self.otherPlainTextEdit.appendPlainText(str(msg))

    # 刷新DNS功能
    def ipconfigFlushDNSButtonClicked(self):
        self.otherPlainTextEdit.setPlainText('')
        cmd = 'ipconfig /flushdns'
        self.thread = otherThreader(cmd)
        self.thread.signal.connect(self.ipconfigFlushDNSCallback)
        self.thread.start()

    def ipconfigFlushDNSCallback(self, msg):
        self.otherPlainTextEdit.appendPlainText(str(msg))

    # 释放网卡功能
    def ipconfigReleaseButtonClicked(self):
        self.otherPlainTextEdit.setPlainText('')
        cmd = 'ipconfig /release'
        self.thread = otherThreader(cmd)
        self.thread.signal.connect(self.ipconfigReleaseCallback)
        self.thread.start()

    def ipconfigReleaseCallback(self, msg):
        self.otherPlainTextEdit.appendPlainText(str(msg))

    # 更新网卡功能
    def ipconfigRenewButtonClicked(self):
        self.otherPlainTextEdit.setPlainText('')
        cmd = 'ipconfig /renew'
        self.thread = otherThreader(cmd)
        self.thread.signal.connect(self.ipconfigRenewCallback)
        self.thread.start()

    def ipconfigRenewCallback(self, msg):
        self.otherPlainTextEdit.appendPlainText(str(msg))

    # 查询域名解析
    def nslookupButtonClicked(self):
        self.otherPlainTextEdit.setPlainText('')
        nsAddress = self.nslookupLineEdit.text()
        if nsAddress:
            if self.nslookupCheckBox.isChecked():
                cmd = 'nslookup %s 8.8.8.8' % nsAddress
            else:
                cmd = 'nslookup %s' % nsAddress
            self.thread = otherThreader(cmd)
            self.thread.signal.connect(self.nslookupCallback)
            self.thread.start()

    def nslookupCallback(self, msg):
        self.otherPlainTextEdit.appendPlainText(str(msg))

    # 路由跟踪功能
    def tracertButtonClicked(self):
        self.otherPlainTextEdit.setPlainText('')
        tracertAddress = self.tracertLineEdit.text()
        if tracertAddress:
            cmd = 'tracert -d %s' % tracertAddress
            self.thread = otherThreader(cmd)
            self.thread.signal.connect(self.tracertCallback)
            self.thread.pidsignal.connect(self.tracertSubPID)
            self.thread.start()

    def tracertCallback(self, msg):
        self.otherPlainTextEdit.appendPlainText(str(msg))

    def tracertSubPID(self,subP_pid):
        self.otherSubP_pid = subP_pid

    # 路由跟踪停止功能
    def tracertStopButtonClick(self):
        # 判断进程id是否为True，默认为0
        if self.otherSubP_pid:
            rekill = self.kill(self.otherSubP_pid)
            self.otherPlainTextEdit.appendPlainText(rekill)


    # 终止线程
    def kill(self,proc_pid):
        try:
            parent_proc = psutil.Process(proc_pid)
            for child_proc in parent_proc.children(recursive=True):
                child_proc.kill()
            parent_proc.kill()
            return '已停止...'
        except:
            return 'Σσ(・Д・；)我我我什么都没做!!!'

# 重写关闭窗口函数
class nWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

    def closeEvent(self,event):
        import sys
        sys.exit(0)

# ping多线程
class pingThread(QtCore.QThread):
    # 创建信号,括号里填写信号传递的参数
    signal = QtCore.pyqtSignal(str)
    signal_list = QtCore.pyqtSignal(list)
    pidsignal = QtCore.pyqtSignal(int)
    # 创建线程锁
    qmut = QtCore.QMutex()
    pinglist = []
    def __init__(self,cmd):
        super().__init__()
        self.cmd = cmd

    def run(self):
        import subprocess
        self.qmut.lock()
        subP = subprocess.Popen(self.cmd,
                                stdin=subprocess.PIPE,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE,
                                bufsize=0,
                                shell=True)
        self.pidsignal.emit(subP.pid)
        for line in iter(subP.stdout.readline, b''):
            line = line.strip().decode('gbk')
            # 把ping输出的结果中的主要信息添加到列表中
            if 'ms' in line or ')，' in line or '),' in line:
                if 'TTL' not in line:
                    self.pinglist.append(line)
            # 发送信号
            self.signal.emit(str(line))
        self.qmut.unlock()
        subP.kill()
        # 发送列表
        self.signal_list.emit(self.pinglist)


class otherThreader(QtCore.QThread):
    # 创建信号,括号里填写信号传递的参数
    signal = QtCore.pyqtSignal(str)
    pidsignal = QtCore.pyqtSignal(int)
    # 创建线程锁
    qmut = QtCore.QMutex()
    def __init__(self,cmd):
        super().__init__()
        self.cmd = cmd

    def run(self):
        import subprocess
        self.qmut.lock()
        subP = subprocess.Popen(self.cmd,
                                stdin=subprocess.PIPE,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE,
                                bufsize=0,
                                shell=True)
        self.pidsignal.emit(subP.pid)
        for i in iter(subP.stdout.readline,b''):
            line = i.strip().decode('GBK')
            self.signal.emit(str(line))
        self.qmut.unlock()
        subP.kill()