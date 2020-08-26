# ITtools 工具

>环境：Windows+python3.7+pyqt5+pyinstaller


## 工具说明

Windows下小工具，通过其可以实现`ping、tracert、nslookup、ipconfig /all、ipconfig /flushdns、ipconfig /release、ipconfig /renew`功能

工具界面

![ITtools](https://github.com/doublezjia/ITtools/blob/master/ScreenShots/ittools.png)

工具通过`pyqt5`设计界面，然后生成python文件进行功能实现，最后通过`pyinstaller`打包成exe文件。


## 目录下文件说明

- ITL.ui  pyqt5保存的设计界面文件

- ITL.py  ITL.ui转换的python文件

- itTools.py 运行程序

- itTools.spec pyinstaller打包文件

- img目录 存放的是程序窗口的图标

- dist和build目录 通过pyinstaller生成的文件夹，其中exe文件存放在dist中

- venv 虚拟环境


## 笔记

### 运行原理

通过按键点击事件发送对应的命令到对应的线程进行处理，在线程中通过`subprocess.Popen`来运行命令，重定向`subprocess.Popen`输出结果，以信号的方式把结果和`pid`发送出去，然后在点击事件中接收信号并处理。

为了一个线程运行完在运行下一个线程，通过`QtCore.QMutex()`对线程加锁和解锁。

### 界面中的label和文本框内容显示

通过`QtCore.pyqtSignal()`来发送信号和接收信号处理实现


### 程序窗口图标不见的问题

通过`pyinstaller`打包的exe把程序窗口等图标都丢失了，是因为路径不对的原因，需要通过以下代码获取路径,注意这个`sys._MEIPASS`只在`exe`下有效，所以代码直接写上去就可以了。

```
# 生成窗口图标路径
    def resource_path(self, relative_path):
        if getattr(sys, 'frozen', False):
            # 这个sys._MEIPASS只在exe下有效
            base_path = sys._MEIPASS
        else:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)
```

然后在窗口代码中对应位置中使用

```
# 获取窗口图标路径
        iconfile = self.resource_path(os.path.join('img', 'rec.png'))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(iconfile), QtGui.QIcon.Normal, QtGui.QIcon.Off)
```

>以上代码都在ITL.py中写的 


### 禁用窗口最大化按钮

在`itTools.py`文件中的对应位置写如下代码

```
# 禁止调整窗口大小,这里的widget为该程序的用户界面基本控件的名称
widget.setFixedSize(widget.width(), widget.height())
```

### 退出程序把线程都关闭

通过重写窗口关闭函数实现

```
class nWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

    def closeEvent(self,event):
        import sys
        sys.exit(0)

```

>以上代码都在ITL.py中写的 

重写完之后要在`itTools.py`主程序中调用新的窗口函数

```
widget = nWidget()
```

### 通过按键关闭线程方法

这里通过`psutil`实现，先通过运行程序时候把线程的`pid`通过信号来获取到，然后通过按钮点击事件把`pid`传递到以下代码中处理。

```
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

```

>以上代码都在ITL.py中写的 


2020.5.27
