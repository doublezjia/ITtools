#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : zealous (doublezjia@163.com)
# @Date    : 2020/5/22
# @Link    : https://github.com/doublezjia
# @Desc    :

import sys
from ITL import Ui_Form,nWidget
from PyQt5 import QtWidgets

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    widget = nWidget()
    ui = Ui_Form()
    ui.setupUi(widget)
    # 禁止调整窗口大小
    widget.setFixedSize(widget.width(),widget.height())
    widget.show()
    sys.exit(app.exec_())