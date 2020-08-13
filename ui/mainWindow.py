# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindowUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(662, 411)
        MainWindow.setMinimumSize(QtCore.QSize(662, 411))
        MainWindow.setMaximumSize(QtCore.QSize(662, 411))
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 661, 411))
        self.tabWidget.setObjectName("tabWidget")
        self.most_use_name = QtWidgets.QWidget()
        self.most_use_name.setObjectName("most_use_name")
        self.tabWidget.addTab(self.most_use_name, "")
        self.less_use_name = QtWidgets.QWidget()
        self.less_use_name.setObjectName("less_use_name")
        self.tabWidget.addTab(self.less_use_name, "")
        self.fiind_by_name = QtWidgets.QWidget()
        self.fiind_by_name.setObjectName("fiind_by_name")
        self.frame = QtWidgets.QFrame(self.fiind_by_name)
        self.frame.setGeometry(QtCore.QRect(0, 0, 651, 51))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(10, 10, 451, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit.setFont(font)
        self.lineEdit.setInputMask("")
        self.lineEdit.setText("")
        self.lineEdit.setMaxLength(32767)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(480, 10, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.tabWidget.addTab(self.fiind_by_name, "")
        self.compare_by_name = QtWidgets.QWidget()
        self.compare_by_name.setObjectName("compare_by_name")
        self.tabWidget.addTab(self.compare_by_name, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Fenètre principale"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.most_use_name), _translate("MainWindow", "Nom les plus utilisés"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.less_use_name), _translate("MainWindow", "Nom les moins utilisés"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Entrez le nom à tester"))
        self.pushButton.setText(_translate("MainWindow", "Envoyer"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.fiind_by_name), _translate("MainWindow", "Chercher par nom"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.compare_by_name), _translate("MainWindow", "Comparer des noms"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
